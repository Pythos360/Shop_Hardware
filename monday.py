from PySide6.QtWidgets import QPushButton, QComboBox, QLabel, QLineEdit, QTableWidgetItem
from PySide6.QtCore import QCoreApplication, QSize, Qt
from datetime import datetime
import PySide6.QtSql as Sql
import json
import requests
from PySide6.QtSql import QSqlQuery
from emailClass import emailClass
from mcmaster import mcmaster


class monday():
    def __init__(self, ui,db, sql, mctble):
        self.ui = ui
        self.sql = sql
        self.db = db
        self.mctble = mctble
        self.emailClass = emailClass(ui)
        self.ui.priceMultiUpdate.clicked.connect(self.query_group_items)
        self.mcmaster = mcmaster
        self.ui.mondayButton.clicked.connect(self.query_group_items)

    def query_group_items(self):
        self.orderList()
        """
        Queries a specific group on a Monday board and returns a list of items,
        each as a dictionary containing 'id' and 'name'.
        """
        board_id = 8737946972
        group_id = 'group_title'
        column_id = 'formula_mkp7j6qz'
        apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjMyNjMyNjcxNCwiYWFpIjoxMSwidWlkIjoxNjAxOTcyOCwiaWFkIjoiMjAyNC0wMi0yN1QyMjo0Njo1MC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6NTE5MDQ5NywicmduIjoidXNlMSJ9.Ca4x2N9zYK7v5QFEv52RaxOT3bWBI0jozI90vXsi4Ro"
        url = "https://api.monday.com/v2"

        query = f"""
        query {{
          boards(ids: [{board_id}]) {{
            groups(ids: ["{group_id}"]) {{
              items_page {{
                items {{
                  id
                  name
                  column_values(ids: ["{column_id}"]) {{
                    id
                    text
                  }}
                }}
              }}
            }}
          }}
        }}
        """

        payload = json.dumps({"query": query})
        headers = {
            "Content-Type": "application/json",
            "Authorization": apiKey
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.ok:
            data = response.json()
            try:
                boards = data["data"]["boards"]
                if not boards:
                    print("No boards returned.")
                    items = []
                else:
                    # Since we filter groups by group_id, we expect only one group in the list
                    group = boards[0].get("groups", [])[0]
                    items = group.get("items_page", {}).get("items", [])
                print("Items in group:", items)
            except Exception as e:
                print("Error parsing response:", e)
        else:
            print("Error querying board items:", response.text)
        for item in items:
            self.update_item_checkbox(item['id'])
            self.update_item_quantity(item['name'])


    def update_item_checkbox(self, item_id):
        """
        Updates the checkbox column for a given item to be checked.
        The Monday API expects the column value to be a JSON string.
        For a checkbox column, we typically send a JSON value like: {"checked": true}
        """
        url = "https://api.monday.com/v2"
        board_id = 8737946972
        apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjMyNjMyNjcxNCwiYWFpIjoxMSwidWlkIjoxNjAxOTcyOCwiaWFkIjoiMjAyNC0wMi0yN1QyMjo0Njo1MC4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6NTE5MDQ5NywicmduIjoidXNlMSJ9.Ca4x2N9zYK7v5QFEv52RaxOT3bWBI0jozI90vXsi4Ro"
        column_id = 'boolean_mkpbed48'
        # Create the value payload for a checked checkbox
        # Note: We double-encode or escape quotes so that the mutation is valid.
        column_value = json.dumps({"checked": True})
        # Escape quotes inside the JSON string
        escaped_value = column_value.replace('"', '\\"')

        mutation = f"""
        mutation {{
          change_column_value(
            board_id: {board_id},
            item_id: {item_id},
            column_id: "{column_id}",
            value: "{escaped_value}"
          ) {{
            id
          }}
        }}
        """
        payload = json.dumps({"query": mutation})
        headers = {"Content-Type": "application/json", "Authorization": apiKey}

        response = requests.post(url, headers=headers, data=payload)
        if response.ok:
            print(f"Item {item_id} updated successfully.")
        else:
            print(f"Error updating item {item_id}: {response.text}")

    def update_item_quantity(self, name):

        query = Sql.QSqlQuery(self.db)
        query.prepare("SELECT quantity, pkg_qty, is_active FROM active_hardware WHERE mcmaster_number = ?")
        query.addBindValue(name)
        if not query.exec():
            print("Error selecting quantity for", mcmaster, query.lastError().text())

        if not query.first():
            print("No record found for", name)

        current_quantity = query.value(0)
        pkg = query.value(1)
        active = query.value(2)
        try:
            current_quantity = int(current_quantity)
        except (ValueError, TypeError):
            current_quantity = 0
        try:
            pkg = int(pkg)
        except (ValueError, TypeError):
            pkg = 0
        try:
            active = int(active)
        except (ValueError, TypeError):
            print("error with active column")
        print("This is the current quantitiy")
        print(current_quantity)

        new_quantity = current_quantity + pkg
        query_update = Sql.QSqlQuery(self.db)
        query_update.prepare("UPDATE active_hardware SET quantity = ?, is_active = 0 WHERE mcmaster_number = ?")
        query_update.addBindValue(new_quantity)
        query_update.addBindValue(name)
        if not query_update.exec():
            print("Error updating quantity for", name, query_update.lastError().text())
        else:
            print("Updated quantity for", name, "new quantity:", new_quantity)
            from PySide6.QtSql import QSqlQuery
            from PySide6.QtCore import QDateTime, Qt



            from PySide6.QtSql import QSqlQuery
            from PySide6.QtCore import QDateTime, Qt

    def orderList(self):
        # ─── 1) Cleanup inactive first ─────────────────────────────────
        to_delete = self.getToDelete()
        if to_delete:
            print("Removing from on_order:", to_delete)
            for name in to_delete:
                self.deleteOnOrder(name)
        else:
            print("No inactive items to remove from on_order.")

        # ─── 2) Count actives ───────────────────────────────────────────
        active_count = self.countActive()
        if active_count < 10:
            print(f"Only {active_count} active items—no action needed.")
        else:
            # ─── 3) Gather new to-order items ────────────────────────────
            to_order = self.getToOrder()
            print(f"Found {len(to_order)} new items to order:", to_order)

            if len(to_order) >= 10:
                # 4) Send email
                body = "\n".join(f"{num} 1" for num in to_order)
                self.emailClass.createEmail(
                    sender="prototypinglab.hardware@gmail.com",
                    to="nick.hawkins@byu.edu",
                    subject="Order Alert",
                    body=body
                )

                # 5) Insert into on_order
                for num in to_order:
                    self.insertOnOrder(num)

        print("Order sync complete.")

    def countActive(self):
        self.sql.exec_("SELECT COUNT(*) FROM active_hardware WHERE is_active = 1;")
        if self.sql.next():
            return self.sql.value(0)
        print("Error counting active_hardware:", self.sql.lastError().text())
        return 0

    def getToOrder(self):
        self.sql.exec_("""
            SELECT mcmaster_number
              FROM active_hardware
             WHERE is_active = 1
               AND mcmaster_number NOT IN (
                     SELECT Name FROM on_order
                 );
        """)
        items = []
        while self.sql.next():
            items.append(self.sql.value(0))
        return items

    def insertOnOrder(self, mcmaster_number):
        self.sql.prepare("INSERT INTO on_order (Name) VALUES (?);")
        self.sql.addBindValue(mcmaster_number)
        if not self.sql.exec_():
            print("Failed to insert on_order for", mcmaster_number, self.sql.lastError().text())

    def getToDelete(self):
        self.sql.exec_("""
            SELECT Name
              FROM on_order
             WHERE Name IN (
                   SELECT mcmaster_number
                     FROM active_hardware
                    WHERE is_active = 0
                 );
        """)
        items = []
        while self.sql.next():
            items.append(self.sql.value(0))
        return items

    def deleteOnOrder(self, name):
        self.sql.prepare("DELETE FROM on_order WHERE Name = ?;")
        self.sql.addBindValue(name)
        if not self.sql.exec_():
            print("Failed to delete on_order for", name, self.sql.lastError().text())
