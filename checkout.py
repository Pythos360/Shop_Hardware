from PySide6.QtWidgets import (
    QPushButton, QComboBox, QLabel, QLineEdit,
    QTableWidgetItem, QMessageBox, QProgressDialog
)
from PySide6.QtCore import QCoreApplication, QSize, Qt
from datetime import datetime
import PySide6.QtSql as Sql
import json
import requests

class checkout():
    def __init__(self, ui, db, sql):
        self.ui = ui
        self.sql = sql
        self.db = db
        self.tabtime = datetime.now()
        self.ui.checkoutTable.model().dataChanged.connect(self.updateAdd)
        self.ui.memButton.clicked.connect(self.exportToArchive)
        self.ui.clearButton.clicked.connect(self.clearTable)
        self.ui.undoScan.clicked.connect(self.removeItem)
        self._last_extra_run: datetime|None = None
        self.ui.instructionButton_2.clicked.connect(self.emergencyMonday)

    def removeItem(self):
        selected = {item.row() for item in self.ui.checkoutTable.selectedItems()}
        for row in sorted(selected, reverse=True):
            print(self.ui.checkoutTable.item(row, 0).text())
            self.ui.checkoutTable.removeRow(row)
        self.ui.calculate_totals()

    def updateAdd(self):
        self.ui.calculate_totals()

    def exportToArchive(self):
        self.updateQuantity()
        model = self.ui.checkoutTable
        for row in range(model.rowCount()):
            m = model.item(row, 0).text() or ""
            s = model.item(row, 1).text() or ""
            h = model.item(row, 2).text() or ""
            l = model.item(row, 3).text() or ""
            q = int(model.item(row, 4).text() or "0")
            p = float(model.item(row, 5).text() or "0")
            dt = model.item(row, 6).text() or ""
            try:
                m_, d, y = dt.split('/')
                iso = f"{int(y):04d}-{int(m_):02d}-{int(d):02d}"
            except:
                iso = dt

            qry = Sql.QSqlQuery(self.db)
            sql = """
                INSERT INTO hardware_archive
                  (mcmaster_number, size, head, length, quantity, price, checkout_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            if not qry.prepare(sql):
                print("Prepare failed:", qry.lastError().text())
                continue
            qry.addBindValue(m)
            qry.addBindValue(s)
            qry.addBindValue(h)
            qry.addBindValue(l)
            qry.addBindValue(q)
            qry.addBindValue(q * p)
            qry.addBindValue(iso)
            if not qry.exec():
                print("Insert failed:", qry.lastError().text())
            else:
                print("Archived", m)

        self.clearTable()

    def updateQuantity(self):
        row_count = self.ui.checkoutTable.rowCount()
        to_push = []

        # first pass: adjust quantities, collect those needing a Monday push
        for row in range(row_count):
            mcm = self.ui.checkoutTable.item(row, 0)
            qty_i = self.ui.checkoutTable.item(row, 4)
            if not mcm or not qty_i:
                continue

            mcmaster = mcm.text().strip()
            try:
                qty_sub = int(qty_i.text().strip())
            except:
                qty_sub = 0

            # fetch current data
            q = Sql.QSqlQuery(self.db)
            q.prepare("SELECT quantity, ordernumber, is_active FROM active_hardware WHERE mcmaster_number = ?")
            q.addBindValue(mcmaster)

            if not q.exec() or not q.first():
                print("Error selecting record for", mcmaster, q.lastError().text())
                continue

            cur = q.value(0); pkg = q.value(1); act = q.value(2)
            try: cur = int(cur)
            except: cur = 0
            try: pkg = int(pkg)
            except: pkg = 0

            if isinstance(act, (bytes, bytearray)):
                active = 1 if int.from_bytes(act, 'little') else 0
            else:
                active = 1 if str(act).lower() in ('1','true','t','y','yes') else 0

            new_qty = cur - qty_sub
            if new_qty <= 0:
                new_qty = 1
            print(cur, pkg, new_qty)
            # if we dip below package and weren't already active, mark and queue
            if new_qty < pkg and active == 0:
                upd1 = Sql.QSqlQuery(self.db)
                upd1.prepare("UPDATE active_hardware SET is_active = 1 WHERE mcmaster_number = ?")
                upd1.addBindValue(mcmaster)
                if not upd1.exec():
                    print("Error updating active flag for", mcmaster, upd1.lastError().text())
                else:
                    to_push.append(mcmaster)

            # always update quantity
            upd2 = Sql.QSqlQuery(self.db)
            upd2.prepare("UPDATE active_hardware SET quantity = ? WHERE mcmaster_number = ?")
            upd2.addBindValue(new_qty)
            upd2.addBindValue(mcmaster)
            if not upd2.exec():
                print("Error updating quantity for", mcmaster, upd2.lastError().text())
            else:
                print("Updated quantity for", mcmaster, "new quantity:", new_qty)

        # second pass: if any, show one progress dialog and push them
        if to_push:
            dlg = QProgressDialog(
                "Pushing parts to Monday…",  # labelText
                "",                          # cancelButtonText (empty → no button)
                0,                           # minimum
                len(to_push),               # maximum
                None                      # parent
            )
            dlg.setWindowModality(Qt.WindowModal)
            dlg.setAutoClose(True)
            dlg.show()

            for idx, part in enumerate(to_push, start=1):
                self.pushMonday(part)
                dlg.setValue(idx)
                QCoreApplication.processEvents()

            dlg.close()

    def pushMonday(self, mcmaster_txt):
        #if updateQuantity says we have less then what comes in a package, it send the informatino to monday for ordering
        url = "https://api.monday.com/v2"
        apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjMyNjMyNjcxNCwiYWFpIjoxMSwidWlkIjoxNjAxOTcyOCwiaWFkIjoiMjAyNC0wMi0yN1QyMjo0Njo1MC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6NTE5MDQ5NywicmduIjoidXNlMSJ9.Ca4x2N9zYK7v5QFEv52RaxOT3bWBI0jozI90vXsi4Ro"  # Replace with your actual API key
        board_id = 8737946972

        # Execute your SQL query to fetch hardware details for mcmaster_txt
        self.sql.exec("SELECT * FROM active_hardware WHERE mcmaster_number = '" + mcmaster_txt + "';")
        self.sql.first()
        item = self.sql
        size = QTableWidgetItem(item.value(0)).text()
        head = QTableWidgetItem(item.value(1)).text()
        length = QTableWidgetItem(item.value(2)).text()

        # Build column_values dictionary
        column_values = {
            "text_mkp66zdd": str(size),
            "text_mkp6b4j2": str(head),
            "text_mkp6ksv8": str(length)
        }
        # Double encode the column values to properly escape the JSON for GraphQL.
        column_values_str = json.dumps(json.dumps(column_values))

        # Build the GraphQL mutation string. Notice that column_values_str is inserted without extra quotes.
        mutation = (
            f'mutation {{ create_item(board_id: {board_id}, '
            f'item_name: "{mcmaster_txt}", '
            f'column_values: {column_values_str} '
            f') {{ id }} }}'
        )
        payload = json.dumps({"query": mutation})
        print("Payload", payload)

        headers = {
            "Content-Type": "application/json",
            "Authorization": apiKey
        }
        try:
            response = requests.post(url, headers=headers, data=payload)
            if response.ok:
                print("API push successful. Response:", response.text)
            else:
                print("API push failed. Status code:", response.status_code, "Response:", response.text)
        except Exception as e:
            print("Exception during API call:", e)

    def emergencyMonday(self):
        # Get all mcmaster_numbers where quantity is 2 or less
        query = Sql.QSqlQuery(self.db)
        query.prepare("SELECT mcmaster_number FROM active_hardware WHERE quantity <= 2")
        if not query.exec():
            print("Error querying emergency Monday items:", query.lastError().text())
            return

        to_push = []
        while query.next():
            mcmaster = query.value(0)
            to_push.append(mcmaster)

        if not to_push:
            QMessageBox.information(None, "Emergency Monday", "No parts with quantity ≤ 2.")
            return

        # Show progress dialog
        dlg = QProgressDialog(
            "Pushing emergency parts to Monday…",
            "",  # No cancel button
            0,
            len(to_push),
            None
        )
        dlg.setWindowModality(Qt.WindowModal)
        dlg.setAutoClose(True)
        dlg.show()

        for idx, part in enumerate(to_push, start=1):
            self.pushMonday(part)
            dlg.setValue(idx)
            QCoreApplication.processEvents()

        dlg.close()


    def clearTable(self):
        self.ui.checkoutTable.setRowCount(0)
        self.ui.calculate_totals()
