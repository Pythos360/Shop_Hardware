from PySide6.QtWidgets import QPushButton, QComboBox, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import QCoreApplication, QSize
from emailClass import emailClass

class fakeClass():

    #this is just a class for testing functionality
    def __init__(self, ui, number):
        self.ui = ui
        self.number = number
        self.emailer = emailClass(self.ui)
        # List to hold all dynamic widgets (could be multiple labels and combo boxes)
        self.dynamicWidgets = []

        # self.ui.clearButton.clicked.connect(self.fakefunction)
        # self.ui.undoScan.clicked.connect(self.creationfunction)
        self.ui.stockDrop.currentIndexChanged.connect(self.dropdown)
        self.ui.selectPartButton.clicked.connect(self.widgetTest)



    def messageBox(self):

        msgBox = QMessageBox()
        msgBox.setText("You Suck Majorly")
        msgBox.exec()

    def widgetTest(self):
        self.ui.hardwareCheck()

    def fakefunction(self):
        self.ui.clearButton.setText("Hi mom")

    # def creationfunction(self):
    #     self.createdButton = QPushButton(self.ui.buyHardware)
    #     self.createdButton.setObjectName("createdButton")
    #     self.ui.gridLayout_3.addWidget(self.createdButton, 3, 1, 1, 1)
    #     self.createdButton.setText(QCoreApplication.translate("MainWindow", "Button Has Been Created", None))

    def clearDynamicWidgets(self):
        # Remove all widgets in the dynamicWidgets list from the layout and delete them.
        for widget in self.dynamicWidgets:
            self.ui.verticalLayout.removeWidget(widget)
            widget.deleteLater()
        self.dynamicWidgets.clear()

    def dropdown(self):
        # Clear any existing dynamic widgets
        self.clearDynamicWidgets()
        self.emailer.on_test1()

        # Example: Create two pairs of label and combo box if metal is "Brass"
        if self.ui.stockDrop.currentText() == "Round Bar":
            # Temporarily remove the spacer from the layout.
            self.ui.verticalLayout.removeItem(self.ui.verticalSpacer_3)

            # Create first pair:
            label1 = QLabel(self.ui.buyStock)
            label1.setText("Choose Diameter")
            combo1 = QComboBox(self.ui.buyStock)
            combo1.setObjectName("brassDiameter")
            # Populate combo1
            combo1.addItem("")
            combo1.addItem("")
            combo1.setItemText(0, QCoreApplication.translate("MainWindow", "3/16", None))
            combo1.setItemText(1, QCoreApplication.translate("MainWindow", "1/4", None))

            # Create second pair:
            label2 = QLabel(self.ui.buyStock)
            label2.setText("Enter Length")
            brassLength = QLineEdit(self.ui.buyStock)
            brassLength.setObjectName("brassLength")
            #
            brassLength.setMaximumSize(QSize(150,40))

            # Append them to our dynamicWidgets list so we can remove them later
            self.dynamicWidgets.extend([label1, combo1, label2, brassLength])

            # Determine current count in the layout
            index = self.ui.verticalLayout.count()
            # Insert the new widgets
            self.ui.verticalLayout.insertWidget(index, label1)
            self.ui.verticalLayout.insertWidget(index + 1, combo1)
            self.ui.verticalLayout.insertWidget(index + 2, label2)
            self.ui.verticalLayout.insertWidget(index + 3, brassLength)

            # Re-add the spacer at the end
            self.ui.verticalLayout.addItem(self.ui.verticalSpacer_3)
