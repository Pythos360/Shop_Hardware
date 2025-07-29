import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QMessageBox, QPlainTextEdit
from PySide6.QtSql import QSqlDatabase
from ui_mainwindow import Ui_MainWindow
from fakeClass import fakeClass
from mcmaster import mcmaster
from monday import monday
from emailClass import emailClass
from hardCheck import hardCheck
import PySide6.QtSql as Sql
from hardwareSearch import hardwareSearch
from checkout import checkout
from datetime import datetime
from addHardware import addHardware
from PySide6.QtCore import QDate, Qt, QObject, Signal
import requests
import resources_rc

from ui_hardwareCheck import Ui_Form

#This class works with the append_log function to write out print statements to the "Log Viewer"
class EmittingStream(QObject):
    textWritten = Signal(str)
    def write(self, text):
        self.textWritten.emit(text)
    def flush(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        QApplication.addLibraryPath(r"C:\Users\Benja\SQL")

        #Connects to the BYU Caedm MySql Database we have through ODBC
        self.db = QSqlDatabase.addDatabase('QODBC')
        self.db.setDatabaseName(
            "Driver={MySQL ODBC 9.3 Unicode Driver};"
            "Server=caedmdb.et.byu.edu;"
            "Database=prldatabase;"
            "Uid=prldatabase;"
            "Pwd=byume;"
        )
        if not self.db.open():
            print("ERROR")
            print(Sql.QSqlDatabase.lastError(self.db))

        if not self.db.open():
            print("Failed to open database:", self.db.lastError().text())
        else:
            print("Database connection successful")

        # Initialize the UI first
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.hardwareCheckWidget = HardwareCheck()
        self.ui.getPrice = self.getPrice
        self.ui.pushItem = self.pushItem #wraps functions into UI for access in other functions.
        self.ui.calculate_totals = self.calculate_totals

        stream = EmittingStream()
        stream.textWritten.connect(self.append_log)
        sys.stdout = stream
        sys.stderr = stream

        # 2) Make sure the logViewer is visible from the start
        self.ui.logViewer.show()
        self.ui.logViewer.clear()




        # Now initialize the SQL models
        self.htbl = Sql.QSqlTableModel(db=self.db) #just makes accessing tables easier
        self.hcbl = Sql.QSqlTableModel(db=self.db)
        self.sql = Sql.QSqlQuery()
        self.ctbl = Sql.QSqlTableModel(db=self.db)
        self.ptble = Sql.QSqlTableModel(db=self.db)
        self.mctble = Sql.QSqlTableModel(db = self.db)

        # Now that ui and htbl are defined, initialize hardwareSearch
        self.hardwareSearch = hardwareSearch(self.ui, self.htbl) #makes all other python files accessable for use
        self.checkout = checkout(self.ui, self.db, self.sql)
        self.addHardware = addHardware(self.ui, self.db, self.sql)
        self.fake = fakeClass(self.ui, 8)
        self.monday = monday(self.ui, self.db, self.sql, self.mctble)
        self.mcmaster = mcmaster(self.ui, self.sql)
        self.emailClass = emailClass(self.ui)
        self.hardCheck = hardCheck(widget=self.hardwareCheckWidget, ui = self.ui, db = self.db, sql = self.sql, hcbl = self.hcbl)
        #Make the cursor start on the search bar
        self.ui.partEntry.setFocus()



    #Makes the "more information" button work
    def hardwareCheck(self):
        self.hardwareCheckWidget.show()

    def pushItem(self, pushID):
        # Query active_hardware using the provided pushID
        self.sql.exec("SELECT * FROM active_hardware WHERE mcmaster_number = '"+pushID+"';")
        self.sql.first()
        item = self.sql
        item0 = QTableWidgetItem(item.value(3))
        repeatFlag = False
        for row in range(self.ui.checkoutTable.rowCount()): #checks the checkout table to see if that item is already there
            current = self.ui.checkoutTable.item(row,0)
            if(current.text().lower()==item0.text().lower()):
                repeatFlag = True #flags this entry as a repeat
        if not(repeatFlag): #if the selected item is NOT a repeat, pushes ME Number and Description to checkout table
            self.ui.checkoutTable.insertRow(self.ui.checkoutTable.rowCount()) #add new row to checkout table
            #this is a lot of code, but it just pulls cells from the SQL table, and inserts them into the checkoutTable
            self.ui.checkoutTable.setItem(self.ui.checkoutTable.rowCount()-1,0,item0)
            item2 = QTableWidgetItem(item.value(0))
            self.ui.checkoutTable.setItem(self.ui.checkoutTable.rowCount()-1,1,item2)
            item3 = QTableWidgetItem(item.value(1))
            item4 = QTableWidgetItem(item.value(2))
            self.ui.checkoutTable.setItem(self.ui.checkoutTable.rowCount()-1,2,item3)
            self.ui.checkoutTable.setItem(self.ui.checkoutTable.rowCount()-1,3,item4)
            #find the multiplier from the table and use it to find the actual price
            multiplier = self.getPrice()
            item51 = QTableWidgetItem(str(item.value(4)))
            item51 = float(item51.text())
            item5float = (multiplier+.25) * item51
            item5 = QTableWidgetItem("{:.2f}".format(item5float))
            item5.setData(Qt.UserRole, item5float)
            self.ui.checkoutTable.setItem(self.ui.checkoutTable.rowCount()-1,4,QTableWidgetItem(str(1)))
            self.ui.checkoutTable.setItem(self.ui.checkoutTable.rowCount()-1,5,item5)
            self.ui.checkoutTable.setItem(self.ui.checkoutTable.rowCount()-1,6, QTableWidgetItem(QDate.currentDate().toString('M/d/yyyy')))
            self.calculate_totals()

    def getPrice(self):
        #this function pulls the competative price multiplier from it's own table
        query = Sql.QSqlQuery(self.db)
        query.exec("SELECT multiplier FROM pricemulti LIMIT 1;")
        if query.lastError().isValid():
            print("SQL Error", query.lastError().text())
            return 1.0  # Default multiplier
        else:
            if query.first():
                try:
                    multiplier = float(query.value(0))
                except Exception as e:
                    print("Error converting multiplier:", e)
                    multiplier = 1.0
                return multiplier
            else:
                print("No value found in table")
                return 0

    def calculate_totals(self):
        #this updates the Total price and number of parts in the checkoutTable
        # Define the column indexes for price and quantity
        price_column = 5   # price is stored in column 5
        quantity_column = 4  # quantity is stored in column 4

        row_count = self.ui.checkoutTable.rowCount()
        total_value = 0.0
        total_quantity = 0.0  # This will hold the sum of all quantities (i.e., number of parts)

        for row in range(row_count):
            price_item = self.ui.checkoutTable.item(row, price_column)
            quantity_item = self.ui.checkoutTable.item(row, quantity_column)

            if price_item is not None and quantity_item is not None:
                try:
                    price = float(price_item.text().strip())
                    quantity = float(quantity_item.text().strip())
                except ValueError:
                    # Skip rows with invalid data
                    continue

                total_value += price * quantity
                total_quantity += quantity

        # Set the UI widgets with the computed totals:
        # Format total_value to two decimal places and total_quantity as an integer.
        self.ui.currPrice.setText(f"${total_value:.2f}")
        self.ui.numPart.setText(str(int(total_quantity)))

        return row_count, total_value, total_quantity


    def append_log(self, text: str):
        # Append incoming text to the QPlainTextEdit
        self.ui.logViewer.insertPlainText(text)
        sb = self.ui.logViewer.verticalScrollBar()
        sb.setValue(sb.maximum())



class HardwareCheck(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.eui = Ui_Form()
        self.eui.setupUi(self)








if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget1 = HardwareCheck()
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
