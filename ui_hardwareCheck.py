# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hardwareCheck.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1208, 417)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1201, 411))
        self.tabWidget.setStyleSheet(u"\n"
"QLineEdit{\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
"padding: 4px 8px;\n"
"background-color: white;\n"
"color: black;\n"
"selection-background-color: gray;\n"
"selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border-color: blue;\n"
"}\n"
"\n"
"QTableView {\n"
"  background-color: #89B284;\n"
"  alternate-background-color: #f6f6f6;\n"
"  gridline-color: #ddd;\n"
"  outline: none;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"  background-color: #3399ff;\n"
"  color: white;\n"
"}\n"
"QTableView::item:selected:!active {\n"
"  background-color: #aaccee;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #555;\n"
"  color: white;\n"
"  padding: 4px;\n"
"  border: 1px solid #666;\n"
"  border-top-left-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"}\n"
"QTableCornerButton::section {\n"
"  background-color: #444;\n"
"  border: 1px solid #666;\n"
"}\n"
"\n"
"/* optional scrollbar styling */\n"
"QTableView QScrollBar:vertical {\n"
"  width: 8px; background: #eee; margi"
                        "n: 2px 0;\n"
"}\n"
"QTableView QScrollBar::handle:vertical {\n"
"  background: #ccc; min-height: 60px; border-radius: 4px;\n"
"}\n"
"QTableView QScrollBar::add-line, QTableView QScrollBar::sub-line { height: 0; }\n"
"\n"
"QPushButton#clearButton{\n"
"    background-color: #CE1010;\n"
"    color: white;\n"
"    border: 2px solid #800;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#clearButton:hover {\n"
"    background-color: #A10000;\n"
"}\n"
"QPushButton#clearButton:pressed {\n"
"    background-color: #800;\n"
"}\n"
"\n"
"QPushButton#memButton{\n"
"    background-color: #caca16;\n"
"    color: white;\n"
"    border: 2px solid #b3b315;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#memButton:hover {\n"
"    background-color: #8e8e12;\n"
"}\n"
"QPushButton#memButton:pressed {\n"
"    background-color: #6c6c0e;\n"
"}\n"
"\n"
"QPushButton#undoScan{\n"
"    background-color: #857885;\n"
"    color: white;\n"
"    border: 2px solid #553D36;\n"
"    border-"
                        "radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#undoScan:hover {\n"
"    background-color: #6C616C;\n"
"}\n"
"QPushButton#undoScan:pressed {\n"
"    background-color: #453e45;\n"
"}\n"
"\n"
"\n"
"QPushButton#checkButton{\n"
"    background-color: #white;\n"
"    color: black;\n"
"    border: 2px solid #553D36;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#checkButton:hover {\n"
"    background-color: #959595;\n"
"}\n"
"QPushButton#checkButton:pressed {\n"
"    background-color: #5a5a5a;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"    color: black;\n"
"    border: 2px solid #553D36;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #FFF;\n"
"    border: 2px solid #9DB4C9;\n"
"    border-top-left-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    padding: 4px 24px 4px 8px; /* leave room on the right for the arrow */\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"/* 2) Hover / focus states on the closed combo"
                        " */\n"
"QComboBox:hover {\n"
"  border-color: #2934CD;\n"
"  /* remove the invalid 'border: 8px;' */\n"
"}\n"
"\n"
"/*\n"
"QComboBox:focus {\n"
"    border-color: #337ab7;\n"
"    box-shadow: 0 0 3px rgba(51,122,183,0.5);\n"
"}\n"
" */\n"
"/* 3) The drop-down arrow container */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 2px solid #FFFF;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"/* 4) The arrow itself */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/icons/arrow.png);\n"
"    width: 12px; height: 12px;\n"
"}\n"
"\n"
"/* 6) The popup list view */\n"
"/* popup list */\n"
"QComboBox QAbstractItemView {\n"
"  background-color: #FFFFFF;    /* or simply 'white' */\n"
"  border: 2px solid #9DB4C9;\n"
"  selection-background-color: #D5EAEB;\n"
"  selection-color: white;\n"
"  padding: 2px;\n"
"  outline: none;\n"
"}\n"
"\n"
"/* 7) Individual items in the popup"
                        " */\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 4px 8px;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #28323A;\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #86B3DB;\n"
"    color: white;\n"
"}\n"
"\n"
"/* 8) Custom scrollbar in the popup (optional) */\n"
"QComboBox QAbstractItemView QScrollBar:vertical {\n"
"    background: #f0f0f0;\n"
"    width: 8px;\n"
"    margin: 0px 2px 0px 2px;\n"
"}\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical {\n"
"    background: #bbb;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"QComboBox QAbstractItemView QScrollBar::add-line,\n"
"QComboBox QAbstractItemView QScrollBar::sub-line {\n"
"    height: 0px;  /* hide arrow buttons */\n"
"}\n"
"QComboBox QAbstractItemView QScrollBar::add-page,\n"
"QComboBox QAbstractItemView QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QPushButton#addHardwareButton{\n"
"    background-color: #white;\n"
"    color: black;\n"
""
                        "    border: 2px solid #553D36;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#addHardwareButton:hover {\n"
"    background-color: #959595;\n"
"}\n"
"QPushButton#addHardwareButton:pressed {\n"
"    background-color: #5a5a5a;\n"
"}\n"
"\n"
"QPushButton#priceMultiUpdate{\n"
"    background-color: #white;\n"
"    color: black;\n"
"    border: 2px solid #553D36;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#priceMultiUpdate:hover {\n"
"    background-color: #959595;\n"
"}\n"
"QPushButton#priceMultiUpdate:pressed {\n"
"    background-color: #5a5a5a;\n"
"}\n"
"\n"
"QPushButton#mondayButton{\n"
"    background-color: #white;\n"
"    color: black;\n"
"    border: 2px solid #553D36;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#mondayButton:hover {\n"
"    background-color: #959595;\n"
"}\n"
"QPushButton#mondayButton:pressed {\n"
"    background-color: #5a5a5a;\n"
"}\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(60, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.widgetHead = QLineEdit(self.tab)
        self.widgetHead.setObjectName(u"widgetHead")

        self.verticalLayout_2.addWidget(self.widgetHead)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_8)

        self.widgetLength = QLineEdit(self.tab)
        self.widgetLength.setObjectName(u"widgetLength")

        self.verticalLayout_2.addWidget(self.widgetLength)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_9)

        self.widgetSize = QLineEdit(self.tab)
        self.widgetSize.setObjectName(u"widgetSize")

        self.verticalLayout_2.addWidget(self.widgetSize)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_10)

        self.widgetThread = QLineEdit(self.tab)
        self.widgetThread.setObjectName(u"widgetThread")

        self.verticalLayout_2.addWidget(self.widgetThread)

        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_11)

        self.widgetActive = QLineEdit(self.tab)
        self.widgetActive.setObjectName(u"widgetActive")

        self.verticalLayout_2.addWidget(self.widgetActive)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_12)

        self.widgetMcNumber = QLineEdit(self.tab)
        self.widgetMcNumber.setObjectName(u"widgetMcNumber")

        self.verticalLayout_4.addWidget(self.widgetMcNumber)

        self.hardSearch = QPushButton(self.tab)
        self.hardSearch.setObjectName(u"hardSearch")

        self.verticalLayout_4.addWidget(self.hardSearch)

        self.hardClear = QPushButton(self.tab)
        self.hardClear.setObjectName(u"hardClear")

        self.verticalLayout_4.addWidget(self.hardClear)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 3, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.widgetInventory = QLineEdit(self.tab)
        self.widgetInventory.setObjectName(u"widgetInventory")

        self.verticalLayout_3.addWidget(self.widgetInventory)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.widgetOrder = QLineEdit(self.tab)
        self.widgetOrder.setObjectName(u"widgetOrder")

        self.verticalLayout_3.addWidget(self.widgetOrder)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.widgetPKG = QLineEdit(self.tab)
        self.widgetPKG.setObjectName(u"widgetPKG")

        self.verticalLayout_3.addWidget(self.widgetPKG)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.widgetMcPrice = QLineEdit(self.tab)
        self.widgetMcPrice.setObjectName(u"widgetMcPrice")

        self.verticalLayout_3.addWidget(self.widgetMcPrice)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)

        self.widgetOurPrice = QLineEdit(self.tab)
        self.widgetOurPrice.setObjectName(u"widgetOurPrice")

        self.verticalLayout_3.addWidget(self.widgetOurPrice)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hardwareCheckTable = QTableView(self.tab_2)
        self.hardwareCheckTable.setObjectName(u"hardwareCheckTable")
        self.hardwareCheckTable.setMinimumSize(QSize(1000, 0))

        self.horizontalLayout.addWidget(self.hardwareCheckTable)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.hardwareCheckTableNum = QLineEdit(self.tab_2)
        self.hardwareCheckTableNum.setObjectName(u"hardwareCheckTableNum")

        self.verticalLayout.addWidget(self.hardwareCheckTableNum)

        self.hardwareCheckClear = QPushButton(self.tab_2)
        self.hardwareCheckClear.setObjectName(u"hardwareCheckClear")

        self.verticalLayout.addWidget(self.hardwareCheckClear)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Head ", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Length", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Size", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Threading", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"On Order?", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"McMaster Number", None))
        self.hardSearch.setText(QCoreApplication.translate("Form", u"Search", None))
        self.hardClear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Number In Inventory", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Order Limit", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"McMaster PKG QTY", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Base Price", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Multiplier", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Grid View", None))
        self.label.setText(QCoreApplication.translate("Form", u"McMaster Number", None))
        self.hardwareCheckClear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Table View", None))
    # retranslateUi

