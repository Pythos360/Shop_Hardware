import os
import time
import truststore
truststore.inject_into_ssl()
import requests
from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from emailClass import emailClass


class mcmaster:
    def __init__(self, ui, sql):
        self.ui = ui
        self.sql = sql
        self.emailClass = emailClass(ui)
        # one combined PEM with both cert + key
        here = os.path.dirname(__file__)
        self.cert = os.path.join(here, "combined.pem")

        # your McMaster API credentials
        self.username = "byuprototypinglab@gmail.com"
        self.password = "byuengineeringisawesome"

        # token storage
        self.token = None
        self.token_expires = 0

        # base URL
        self.BASE_URL = "https://api.mcmaster.com/v1"

        # wire up your buttons
        self.ui.priceMultiUpdate.clicked.connect(self.update_PriceMulti)


    def update_PriceMulti(self):
        self.login()
        multipliers = []
        i = 0
        for i in range(10):
            loopOurPrice, loopPartNumber = self.OurPrice()

            self.subscribeItem(loopPartNumber)
            McMasterPrice = self.getPrice(loopPartNumber)
            print(McMasterPrice)
            loopOurPrice = float(loopOurPrice)
            McMasterPrice = float(McMasterPrice)
            print(loopOurPrice, McMasterPrice)
            multiplier = McMasterPrice / loopOurPrice
            multipliers.append(multiplier)
            print(multiplier)

        average_multiplier = sum(multipliers) / len(multipliers)
        current_multiplier = self.ui.getPrice()


        if current_multiplier < average_multiplier:
            self.sql.prepare("""
            
            
            update pricemulti
            set multiplier = :mult
            """)
            self.sql.bindValue(":mult", average_multiplier)
            if not self.sql.exec():
                print("SQL Error", self.sql.lastError().text())
            body = f"""\
            The Price Multiplier has been updated from {current_multiplier:.3f} \
            to {average_multiplier:.3f}\
            """
            self.emailClass.createEmail("prototypinglab.hardware@gmail.com","byuprototypinglab@gmail.com", "Price Multiplier Updated", body)
        else:
            body = f"""\
            The Price Multiplier has not been updated. Current multiplier is {current_multiplier:.3f}\
            the proposed multiplier was {average_multiplier:.3f}\
            """
            self.emailClass.createEmail("prototypinglab.hardware@gmail.com", "byuprototypinglab@gmail.com", "Price Multiplier Updated", body)
            return None

        print(average_multiplier, current_multiplier)



    def login(self):
        # quick sanity check on the combined PEM
        print(f"Looking for cert: {self.cert} exists? {os.path.exists(self.cert)}")
        with open(self.cert, 'r') as f:
            print("PEM header:", f.readline().strip())

        url = f"{self.BASE_URL}/login"
        payload = {"UserName": self.username, "Password": self.password}
        headers = {"Accept-Encoding": "br"}

        try:
            resp = requests.post(
                url,
                json=payload,
                cert=self.cert,       # now points at combined.pem
                headers=headers
            )
        except Exception as e:
            print("Login exception:", e)
            return

        print("Status code:", resp.status_code)
        print("Response body:", resp.text)

        if not resp.ok:
            QMessageBox.warning(self.ui, "Login Failed", f"{resp.status_code} – {resp.text}")
            return

        data = resp.json()
        self.token = data.get("AuthToken")
        exp_ts = data.get("ExpirationTS", "")
        try:
            exp_dt = datetime.fromisoformat(exp_ts.rstrip("Z"))
            self.token_expires = exp_dt.timestamp()
        except Exception:
            self.token_expires = time.time() + 24*3600

        print("Got AuthToken:", self.token)
        print("Expires at:", datetime.fromtimestamp(self.token_expires))
        return self.token

    def subscribeItem(self, partNumber):

        url = f"{self.BASE_URL}/products"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        payload = {
            "URL": f"https://mcmaster.com/{partNumber}"
        }

        try:
            resp = requests.put(
                url,
                json=payload,
                headers=headers,
                cert=self.cert       # your client cert/key pair
            )
        except Exception as e:
            print("Subscription exception:", e)
            return None

        # Debug output
        #print("Status code:", resp.status_code)
        #print("Response body:", resp.text)

        if not resp.ok:
            QMessageBox.warning(
                self.ui,
                "Subscribe Failed",
                f"{resp.status_code} – {resp.text}"
            )
            return None

        product_info = resp.json()
        #print("Subscription worked:", product_info)
        return None

    def getPrice(self, partNumber):
            """
            GET /v1/products/{partNumber}/price
            Retrieves the current price for the given McMaster part.
            """
            url = f"{self.BASE_URL}/products/{partNumber}/price"
            headers = {
                "Authorization": f"Bearer {self.token}"
            }


            try:
                resp = requests.get(
                    url,
                    headers=headers,
                    cert=self.cert       # your client cert/key pair
                )
            except Exception as e:
                print("Price exception:", e)
                return None

            # Debug output
            print("Status code:", resp.status_code)
            print("Response body:", resp.text)

            if not resp.ok:
                QMessageBox.warning(
                    self.ui,
                    "Price Lookup Failed",
                    f"{resp.status_code} – {resp.text}"
                )
                return None

            data = resp.json()

            # Expecting a list like [{"Amount":14.76, ...}]
            if not isinstance(data, list) or not data:
                print("Unexpected JSON shape for price:", data)
                return None

            price_info = data[0]
            amount = price_info.get("Amount")

            if amount is None:
                print("No 'Amount' key found in price response:", price_info)
                return None

            return amount

    def OurPrice(self):

        if not self.sql.exec("SELECT * FROM active_hardware ORDER BY RAND() LIMIT 1;"):
            print(self.sql.lastError().text())
        self.sql.first()
        item = self.sql
        mcmaster_number = self.sql.value(3)
        price = self.sql.value(10)
        print(price, mcmaster_number)
        return price, mcmaster_number
