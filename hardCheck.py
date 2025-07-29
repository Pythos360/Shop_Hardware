from PySide6.QtWidgets import QPushButton, QComboBox, QLabel, QLineEdit, QTableWidgetItem
from PySide6.QtCore import QCoreApplication, QSize, Qt
from datetime import datetime
import PySide6.QtSql as Sql
import json
import requests
class hardCheck():
    def __init__(self, widget, ui, db, sql, hcbl):

        self.popup = widget
        self.eui = widget.eui
        self.ui = ui
        self.db = db
        self.sql = sql
        self.hcbl = hcbl

        self.ui.checkButton.clicked.connect(self.addInfo)
        self.eui.hardClear.clicked.connect(self.Clear)
        self.eui.hardSearch.clicked.connect(self.Search)
        self.eui.widgetMcNumber.returnPressed.connect(self.Search)
        self.eui.hardwareCheckTableNum.textChanged.connect(self.otherSearch)
        self.eui.hardwareCheckClear.clicked.connect(self.otherClear)

    def otherClear(self):
        self.eui.hardwareCheckTableNum.clear()


    def otherSearch(self):

        partText = self.eui.hardwareCheckTableNum.text().strip()
        self.hcbl.setFilter(f"mcmaster_number LIKE '%{partText}%'")
        self.hcbl.select()


    def Search(self):
        McNumber = self.eui.widgetMcNumber.text().strip()
        self.Clear()
        self.addInfo(McNumber)



    def addInfo(self, McNumber):
        selected = set()
        McNumber = str(McNumber)

        print(McNumber, "this one")

        if len(self.ui.checkoutTable.selectedItems()) == 0:
            self.eui.tabWidget.setCurrentIndex(1)
            mcmaster_txt = "noItem"
            self.eui.hardwareCheckTableNum.setFocus()
        elif len(self.ui.checkoutTable.selectedItems()) == 1:
            for item in self.ui.checkoutTable.selectedItems():
                selected.add(item.row())
            gridRow = list(selected)[0]
            mcmaster_txt = self.ui.checkoutTable.item(gridRow, 0).text()
            self.eui.widgetMcNumber.setFocus()
        else:
            print("Error: Please select exactly one row.")
            return  # Exit function or handle the case as needed

        if McNumber != 'False':
            mcmaster_txt = McNumber

        # Execute SQL query
        self.sql.exec("SELECT * FROM active_hardware WHERE mcmaster_number = '" + mcmaster_txt + "';")
        self.sql.first()
        item = self.sql
        # Get data from SQL result and populate the hardwareCheck UI
        size = QTableWidgetItem(item.value(0)).text()
        head = QTableWidgetItem(item.value(1)).text()
        length = QTableWidgetItem(item.value(2)).text()
        mcmaster = QTableWidgetItem(item.value(3)).text()
        ourPrice = self.sql.value(4)
        pkg = self.sql.value(5)
        threading = QTableWidgetItem(item.value(6)).text()
        order = self.sql.value(9)
        quantity = self.sql.value(7)
        activity = self.sql.value(8)
        ourPrice = str(ourPrice)
        quantity = str(quantity)
        order = str(order)
        pkg = str(pkg)
        print("first activity")
        if activity == 0:
            activity = "No"
        if activity == 1:
            activity = "Yes"
        print("second activity")

        multiplier = self.ui.getPrice()
        multiplier = str(multiplier)

        print(size, head, length, mcmaster, ourPrice, pkg, threading, activity)

        # Assuming item.value(1) is the head
        self.eui.widgetHead.setText(head)  # Update lineEdit_3 in the hardwareCheck window
        self.eui.widgetSize.setText(size)
        self.eui.widgetLength.setText(length)
        self.eui.widgetOurPrice.setText(multiplier)
        self.eui.widgetPKG.setText(pkg)
        self.eui.widgetThread.setText(threading)
        self.eui.widgetActive.setText(activity)
        self.eui.widgetInventory.setText(quantity)
        self.eui.widgetOrder.setText(order)
        self.eui.widgetMcPrice.setText(ourPrice)

        # Call the hardwareCheck method to show the new window
        self.popup.show()
        self.setTable()


    def setTable(self):
        # Set up the model to point to the 'inventory' table and select its data.
        self.hcbl.setTable('active_hardware')
        self.hcbl.select()

        # Define the header labels for only the columns you want to display.
        header_labels = ["Size", "Head Type", "Length", "McMaster Number", "Our Price", "PKG QTY", "Threading", "Quantity", "On Order", "Number Per Order" ]

        # Set header labels for the first few columns.
        for i, label in enumerate(header_labels):
            self.hcbl.setHeaderData(i, Qt.Horizontal, label)

        # Set the model on the table view.
        self.eui.hardwareCheckTable.setModel(self.hcbl)

        # Debug: print out the total number of columns in the model.
        total_columns = self.hcbl.columnCount()
        print("Total columns in model:", total_columns)




    def Clear(self):
        self.eui.widgetHead.clear()  # Update lineEdit_3 in the hardwareCheck window
        self.eui.widgetSize.clear()
        self.eui.widgetLength.clear()
        self.eui.widgetOurPrice.clear()
        self.eui.widgetPKG.clear()
        self.eui.widgetThread.clear()
        self.eui.widgetActive.clear()
        self.eui.widgetInventory.clear()
        self.eui.widgetOrder.clear()
        self.eui.widgetMcPrice.clear()
        self.eui.widgetMcNumber.clear()


