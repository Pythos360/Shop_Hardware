import os
import base64
import json
import urllib.request
import urllib.error

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from email.mime.text import MIMEText
from google.auth.exceptions import RefreshError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

class emailClass:
    def __init__(self, ui):
        self.ui = ui

    def createEmail(self, sender, to, subject, body):
        creds = self.get_credentials()
        msg_body = self._build_message(sender, to, subject, body)
        self.send_email(creds, msg_body)

    def get_credentials(self):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if creds and creds.expired:
            try:
                creds.refresh(Request())
            except RefreshError:
                print("Stored credentials expired or revoked, removing token.json")
                os.remove('token.json')
                creds = None

        if not creds:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token_file:
                token_file.write(creds.to_json())

        return creds

    def _build_message(self, sender, to, subject, body_text):
        message = MIMEText(body_text, 'plain')
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes())
        return {'raw': raw.decode('utf-8')}

    def send_email(self, creds, message_body):
        url = 'https://gmail.googleapis.com/gmail/v1/users/me/messages/send'
        headers = {
            'Authorization': f'Bearer {creds.token}',
            'Content-Type': 'application/json'
        }
        data = json.dumps(message_body).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')

        try:
            with urllib.request.urlopen(req) as resp:
                resp_data = resp.read().decode('utf-8')
                resp_json = json.loads(resp_data)
                sent_id = resp_json.get('id')
                print(f"Message sent! Message ID: {sent_id}")
        except urllib.error.HTTPError as e:
            err_body = e.read().decode('utf-8') if e.fp else ''
            print("Send failed:", e.code, err_body)
