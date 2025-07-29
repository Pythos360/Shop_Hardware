
from PySide6.QtWidgets import QPushButton, QComboBox, QLabel, QLineEdit, QTableWidgetItem
from PySide6.QtCore import QCoreApplication, QSize, Qt
from datetime import datetime
import PySide6.QtSql as Sql
import smtplib
from email.message import EmailMessage

class hardwareSearch():
    #this class makes the dropdown box and mcmaster number search functinality work
    def __init__(self, ui, htbl):
        self.ui = ui
        self.htbl = htbl
        self.tabtime = datetime.now()

        self.setupTable()

        self.ui.partEntry.textChanged.connect(self.updateFilters)
        self.ui.headSearch.currentIndexChanged.connect(self.updateFilters)
        self.ui.sizeSearch.currentIndexChanged.connect(self.updateFilters)
        self.ui.lengthSearch.currentIndexChanged.connect(self.updateFilters)
        self.ui.clearSearch.clicked.connect(self.clearSearch)
        self.ui.purchaseTable.clicked.connect(self.push)
        self.ui.partEntry.returnPressed.connect(self.enterPressed)



    def enterPressed(self):
        #this moves the part over to checkoutTable
        if not(self.ui.partEntry.text()==''):

            # Use self.htbl (the model) instead of self.tbl
            pushID = self.htbl.record(0).value('mcmaster_number')  # finds item id to push
            self.ui.pushItem(pushID)
            print(pushID)
            # self.ui.displayTabs.setCurrentIndex(1)
            self.clearSearch()
            print("enter pressed")


    def push(self):
        if (self.ui.purchaseTable.selectionModel().hasSelection() == True):
            row = self.ui.purchaseTable.currentIndex().row()
            # Use self.htbl (the model) instead of self.tbl
            pushID = self.htbl.record(row).value('mcmaster_number')  # finds item id to push
            self.ui.pushItem(pushID)
            print(pushID)
            # self.ui.displayTabs.setCurrentIndex(1)
            self.clearSearch()
            print("enter pressed")



    def updateFilters(self):
        conditions = []

        # 1) mcmaster_number contains partEntry text
        partText = self.ui.partEntry.text().strip()
        if partText:
            conditions.append(f"mcmaster_number LIKE '%{partText}%'")

        # 2) head contains headSearch text
        if self.ui.headSearch.currentIndex() != 0:
            headText = self.ui.headSearch.currentText().strip()
            conditions.append(f"head LIKE '%{headText}%'")

        # 3) size contains sizeSearch text
        if self.ui.sizeSearch.currentIndex() != 0:
            sizeText = self.ui.sizeSearch.currentText().strip()
            conditions.append(f"size LIKE '%{sizeText}%'")

        # 4) length exactly equals lengthSearch text
        if self.ui.lengthSearch.currentIndex() != 0:
            lengthText = self.ui.lengthSearch.currentText().strip()
            # assuming your column is literally named `length`
            conditions.append(f"`length` = '{lengthText}'")

        # combine with AND
        filter_str = " AND ".join(conditions)
        self.htbl.setFilter(filter_str)

        # *** critical: re-run the query so the view updates ***
        self.htbl.select()

        # debug output
        if self.htbl.lastError().isValid():
            self.ui.consoleOutput.insertPlainText(self.htbl.lastError().text() + "\n")
            self.ui.consoleOutput.insertPlainText("Filter was: " + filter_str + "\n")


    def clearSearch(self):
        # Reset the QLineEdit text (if you want to clear partEntry)
        self.ui.partEntry.clear()

        # Reset combo boxes to their default (first) index
        self.ui.headSearch.setCurrentIndex(0)
        self.ui.sizeSearch.setCurrentIndex(0)
        self.ui.lengthSearch.setCurrentIndex(0)
        self.ui.partEntry.clear()

        # Optionally, update filters after clearing
        self.updateFilters()



    def setupTable(self):
        # Set up the model to point to the 'inventory' table and select its data.
        self.htbl.setTable('active_hardware')
        self.htbl.select()

        # Define the header labels for only the columns you want to display.
        header_labels = ["Size", "Head Type", "Length", "McMaster Number"]

        # Set header labels for the first few columns.
        for i, label in enumerate(header_labels):
            self.htbl.setHeaderData(i, Qt.Horizontal, label)

        # Set the model on the table view.
        self.ui.purchaseTable.setModel(self.htbl)

        # Debug: print out the total number of columns in the model.
        total_columns = self.htbl.columnCount()
        print("Total columns in model:", total_columns)

        # Hide any extra columns beyond the first 5.
        for col in range(len(header_labels), total_columns):
            self.ui.purchaseTable.hideColumn(col)


