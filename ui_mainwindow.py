# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStatusBar, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1184, 967)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.purchaseTab = QTabWidget(self.splitter)
        self.purchaseTab.setObjectName(u"purchaseTab")
        self.purchaseTab.setMaximumSize(QSize(695, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 85, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(127, 170, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(63, 127, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(0, 42, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(0, 57, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 42, 127, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        brush10 = QBrush(QColor(76, 136, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush10)
        self.purchaseTab.setPalette(palette)
        self.purchaseTab.setStyleSheet(u"\n"
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
"\n"
"\n"
"QTableView {\n"
"  background-color: #9DB4C9;\n"
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
"  width: 8px; background: #"
                        "eee; margin: 2px 0;\n"
"}\n"
"QTableView QScrollBar::handle:vertical {\n"
"  background: #ccc; min-height: 60px; border-radius: 4px;\n"
"}\n"
"QTableView QScrollBar::add-line, QTableView QScrollBar::sub-line { height: 0; }\n"
"\n"
"QPushButton#clearSearch{\n"
"    background-color: #CE1010;\n"
"    color: white;\n"
"    border: 2px solid #800;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#clearSearch:hover {\n"
"    background-color: #A10000;\n"
"}\n"
"QPushButton#clearSearch:pressed {\n"
"    background-color: #800;\n"
"}\n"
"\n"
"/* 1) The main QComboBox widget */\n"
"QComboBox {\n"
"    background-color: #FFF;\n"
"    border: 2px solid #9DB4C9;\n"
"    border-top-left-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    padding: 4px 24px 4px 8px; /* leave room on the right for the arrow */\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"/* 2) Hover / focus states on the closed combo */\n"
"QComboBox:hover {\n"
"  border-color: #2934CD;\n"
"  /* remove the invalid 'border: 8p"
                        "x;' */\n"
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
"/* 7) Individual items in the popup */\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 4px 8px;\n"
"}\n"
"QComboBox QAbs"
                        "tractItemView::item:hover {\n"
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
"\n"
"")
        self.purchaseTab.setTabPosition(QTabWidget.TabPosition.North)
        self.purchaseTab.setTabShape(QTabWidget.TabShape.Triangular)
        self.buyHardware = QWidget()
        self.buyHardware.setObjectName(u"buyHardware")
        self.gridLayout_3 = QGridLayout(self.buyHardware)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.QRscan = QLabel(self.buyHardware)
        self.QRscan.setObjectName(u"QRscan")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QRscan.sizePolicy().hasHeightForWidth())
        self.QRscan.setSizePolicy(sizePolicy)
        self.QRscan.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.QRscan.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.QRscan, 0, 1, 1, 2)

        self.clearSearch = QPushButton(self.buyHardware)
        self.clearSearch.setObjectName(u"clearSearch")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush11 = QBrush(QColor(206, 16, 16, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush11)
        brush12 = QBrush(QColor(255, 0, 0, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush12)
        brush13 = QBrush(QColor(212, 0, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        brush14 = QBrush(QColor(85, 0, 0, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush14)
        brush15 = QBrush(QColor(113, 0, 0, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush16 = QBrush(QColor(212, 127, 127, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush16)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush16)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush17 = QBrush(QColor(170, 0, 0, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush18 = QBrush(QColor(85, 0, 0, 127))
        brush18.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        brush19 = QBrush(QColor(221, 0, 0, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.clearSearch.setPalette(palette1)

        self.gridLayout_3.addWidget(self.clearSearch, 5, 1, 1, 2)

        self.lengthSearch = QComboBox(self.buyHardware)
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.addItem("")
        self.lengthSearch.setObjectName(u"lengthSearch")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush6)
        brush20 = QBrush(QColor(255, 127, 127, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush20)
        brush21 = QBrush(QColor(255, 63, 63, 255))
        brush21.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush21)
        brush22 = QBrush(QColor(127, 0, 0, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush22)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush17)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush20)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush20)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush21)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush22)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush17)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush20)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush20)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush21)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush17)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush23 = QBrush(QColor(127, 0, 0, 127))
        brush23.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush23)
#endif
        brush24 = QBrush(QColor(255, 76, 76, 255))
        brush24.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush24)
        self.lengthSearch.setPalette(palette2)

        self.gridLayout_3.addWidget(self.lengthSearch, 3, 1, 1, 2)

        self.partEntry = QLineEdit(self.buyHardware)
        self.partEntry.setObjectName(u"partEntry")

        self.gridLayout_3.addWidget(self.partEntry, 1, 1, 1, 2)

        self.sizeSearch = QComboBox(self.buyHardware)
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.addItem("")
        self.sizeSearch.setObjectName(u"sizeSearch")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush6)
        brush25 = QBrush(QColor(255, 255, 254, 255))
        brush25.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush25)
        brush26 = QBrush(QColor(255, 255, 190, 255))
        brush26.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush26)
        brush27 = QBrush(QColor(127, 127, 63, 255))
        brush27.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush27)
        brush28 = QBrush(QColor(170, 170, 85, 255))
        brush28.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush28)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush29 = QBrush(QColor(255, 255, 191, 255))
        brush29.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush29)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush25)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush26)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush27)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush28)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush29)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush27)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush25)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush26)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush27)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush28)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush27)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush27)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush30 = QBrush(QColor(255, 255, 127, 255))
        brush30.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush30)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush31 = QBrush(QColor(127, 127, 63, 127))
        brush31.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush31)
#endif
        brush32 = QBrush(QColor(255, 255, 203, 255))
        brush32.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.Accent, brush32)
        self.sizeSearch.setPalette(palette3)
        self.sizeSearch.setIconSize(QSize(14, 16))

        self.gridLayout_3.addWidget(self.sizeSearch, 4, 1, 1, 2)

        self.purchaseTable = QTableView(self.buyHardware)
        self.purchaseTable.setObjectName(u"purchaseTable")
        self.purchaseTable.setMinimumSize(QSize(0, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush33 = QBrush(QColor(157, 180, 201, 255))
        brush33.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush33)
        brush34 = QBrush(QColor(212, 234, 255, 255))
        brush34.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush34)
        brush35 = QBrush(QColor(148, 202, 255, 255))
        brush35.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush35)
        brush36 = QBrush(QColor(42, 85, 127, 255))
        brush36.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush36)
        brush37 = QBrush(QColor(57, 113, 170, 255))
        brush37.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush37)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush33)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush33)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush38 = QBrush(QColor(246, 246, 246, 255))
        brush38.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush38)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette4.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush33)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush34)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush35)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush36)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush37)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush33)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush33)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush38)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush36)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush33)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush34)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush35)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush36)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush37)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush36)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush36)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush33)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush33)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush38)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush39 = QBrush(QColor(42, 85, 127, 127))
        brush39.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush39)
#endif
        brush40 = QBrush(QColor(161, 208, 255, 255))
        brush40.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.Accent, brush40)
        self.purchaseTable.setPalette(palette4)
        self.purchaseTable.horizontalHeader().setDefaultSectionSize(120)

        self.gridLayout_3.addWidget(self.purchaseTable, 0, 0, 7, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 6, 2, 1, 1)

        self.headSearch = QComboBox(self.buyHardware)
        self.headSearch.addItem("")
        self.headSearch.addItem("")
        self.headSearch.addItem("")
        self.headSearch.addItem("")
        self.headSearch.addItem("")
        self.headSearch.addItem("")
        self.headSearch.addItem("")
        self.headSearch.addItem("")
        self.headSearch.setObjectName(u"headSearch")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush25)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush26)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush27)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush28)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush29)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette5.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush25)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush26)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush27)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush28)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush29)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush27)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush25)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush26)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush27)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush28)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush27)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush27)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush30)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush31)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.Accent, brush32)
        self.headSearch.setPalette(palette5)
        self.headSearch.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.headSearch.setAutoFillBackground(False)
        self.headSearch.setStyleSheet(u"background-color: #3755CB6\n"
"\n"
"    /* replace with the path inside your .qrc, e.g. \":/icons/arrow-white.svg\" */\n"
"    image: url(\":/icons/arrow-white.svg\");\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"")
        self.headSearch.setIconSize(QSize(90, 90))

        self.gridLayout_3.addWidget(self.headSearch, 2, 1, 1, 2)

        icon = QIcon()
        icon.addFile(u"../../../Downloads/2027187.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.purchaseTab.addTab(self.buyHardware, icon, "")
        self.buyStock = QWidget()
        self.buyStock.setObjectName(u"buyStock")
        self.gridLayout_5 = QGridLayout(self.buyStock)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableView_3 = QTableView(self.buyStock)
        self.tableView_3.setObjectName(u"tableView_3")

        self.gridLayout_5.addWidget(self.tableView_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stockLabel = QLabel(self.buyStock)
        self.stockLabel.setObjectName(u"stockLabel")
        self.stockLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.stockLabel)

        self.stockDrop = QComboBox(self.buyStock)
        self.stockDrop.addItem("")
        self.stockDrop.addItem("")
        self.stockDrop.addItem("")
        self.stockDrop.addItem("")
        self.stockDrop.addItem("")
        self.stockDrop.addItem("")
        self.stockDrop.addItem("")
        self.stockDrop.addItem("")
        self.stockDrop.setObjectName(u"stockDrop")
        self.stockDrop.setMinimumSize(QSize(125, 36))
        self.stockDrop.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout.addWidget(self.stockDrop)

        self.matDrop = QLabel(self.buyStock)
        self.matDrop.setObjectName(u"matDrop")
        self.matDrop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.matDrop)

        self.metalDrop = QComboBox(self.buyStock)
        self.metalDrop.addItem("")
        self.metalDrop.addItem("")
        self.metalDrop.addItem("")
        self.metalDrop.addItem("")
        self.metalDrop.setObjectName(u"metalDrop")

        self.verticalLayout.addWidget(self.metalDrop)

        self.instructionButton = QPushButton(self.buyStock)
        self.instructionButton.setObjectName(u"instructionButton")

        self.verticalLayout.addWidget(self.instructionButton)

        self.Test1 = QPushButton(self.buyStock)
        self.Test1.setObjectName(u"Test1")

        self.verticalLayout.addWidget(self.Test1)

        self.McTest = QPushButton(self.buyStock)
        self.McTest.setObjectName(u"McTest")

        self.verticalLayout.addWidget(self.McTest)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.purchaseTab.addTab(self.buyStock, "")
        self.splitter.addWidget(self.purchaseTab)
        self.checkoutTab = QTabWidget(self.splitter)
        self.checkoutTab.setObjectName(u"checkoutTab")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush41 = QBrush(QColor(170, 85, 255, 255))
        brush41.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush41)
        brush42 = QBrush(QColor(234, 212, 255, 255))
        brush42.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush42)
        brush43 = QBrush(QColor(202, 148, 255, 255))
        brush43.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush43)
        brush44 = QBrush(QColor(85, 42, 127, 255))
        brush44.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush44)
        brush45 = QBrush(QColor(113, 57, 170, 255))
        brush45.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush45)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush41)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush46 = QBrush(QColor(212, 170, 255, 255))
        brush46.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush46)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush41)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush42)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush43)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush44)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush45)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush41)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush46)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush44)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush41)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush42)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush43)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush44)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush45)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush44)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush44)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush41)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush41)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush41)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush47 = QBrush(QColor(85, 42, 127, 127))
        brush47.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush47)
#endif
        brush48 = QBrush(QColor(208, 161, 255, 255))
        brush48.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Disabled, QPalette.Accent, brush48)
        self.checkoutTab.setPalette(palette6)
        self.checkoutTab.setStyleSheet(u"\n"
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
        self.checkoutTab.setTabShape(QTabWidget.TabShape.Triangular)
        self.checkout = QWidget()
        self.checkout.setObjectName(u"checkout")
        self.checkout.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.checkout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.numPart = QLabel(self.checkout)
        self.numPart.setObjectName(u"numPart")
        self.numPart.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.numPart, 3, 1, 1, 1)

        self.partLabel = QLabel(self.checkout)
        self.partLabel.setObjectName(u"partLabel")
        self.partLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.partLabel, 2, 1, 1, 1)

        self.currPrice = QLabel(self.checkout)
        self.currPrice.setObjectName(u"currPrice")
        self.currPrice.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.currPrice, 1, 1, 1, 1)

        self.checkoutTable = QTableWidget(self.checkout)
        if (self.checkoutTable.columnCount() < 7):
            self.checkoutTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.checkoutTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.checkoutTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.checkoutTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.checkoutTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.checkoutTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.checkoutTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.checkoutTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.checkoutTable.setObjectName(u"checkoutTable")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush49 = QBrush(QColor(137, 178, 132, 255))
        brush49.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush49)
        brush50 = QBrush(QColor(205, 255, 228, 255))
        brush50.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush50)
        brush51 = QBrush(QColor(167, 224, 193, 255))
        brush51.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush51)
        brush52 = QBrush(QColor(64, 96, 79, 255))
        brush52.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush52)
        brush53 = QBrush(QColor(86, 129, 105, 255))
        brush53.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush53)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush49)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush49)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush38)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush49)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush50)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush51)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush52)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush53)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush49)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush49)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush38)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush52)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush49)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush50)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush51)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush52)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush53)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush52)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush52)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush49)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush49)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush38)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush54 = QBrush(QColor(64, 96, 79, 127))
        brush54.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush54)
#endif
        brush55 = QBrush(QColor(168, 251, 205, 255))
        brush55.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Disabled, QPalette.Accent, brush55)
        self.checkoutTable.setPalette(palette7)
        self.checkoutTable.horizontalHeader().setDefaultSectionSize(120)

        self.gridLayout_4.addWidget(self.checkoutTable, 0, 0, 10, 1)

        self.memButton = QPushButton(self.checkout)
        self.memButton.setObjectName(u"memButton")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush56 = QBrush(QColor(202, 202, 22, 255))
        brush56.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush56)
        brush57 = QBrush(QColor(0, 0, 190, 255))
        brush57.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush57)
        brush58 = QBrush(QColor(0, 0, 158, 255))
        brush58.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush58)
        brush59 = QBrush(QColor(0, 0, 63, 255))
        brush59.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush59)
        brush60 = QBrush(QColor(0, 0, 85, 255))
        brush60.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush60)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush56)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush56)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush59)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush61 = QBrush(QColor(255, 255, 255, 127))
        brush61.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush61)
#endif
        palette8.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush56)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush57)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush58)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush59)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush60)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush56)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush56)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush59)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush61)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush59)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush56)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush57)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush58)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush59)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush60)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush59)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush59)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush56)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush56)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush62 = QBrush(QColor(0, 0, 127, 255))
        brush62.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush62)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush63 = QBrush(QColor(0, 0, 63, 127))
        brush63.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush63)
#endif
        brush64 = QBrush(QColor(0, 0, 89, 255))
        brush64.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Disabled, QPalette.Accent, brush64)
        self.memButton.setPalette(palette8)
        self.memButton.setAutoFillBackground(False)
        self.memButton.setCheckable(False)
        self.memButton.setChecked(False)

        self.gridLayout_4.addWidget(self.memButton, 4, 1, 1, 1)

        self.checkButton = QPushButton(self.checkout)
        self.checkButton.setObjectName(u"checkButton")

        self.gridLayout_4.addWidget(self.checkButton, 8, 1, 1, 1)

        self.undoScan = QPushButton(self.checkout)
        self.undoScan.setObjectName(u"undoScan")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush65 = QBrush(QColor(133, 120, 133, 255))
        brush65.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush65)
        brush66 = QBrush(QColor(107, 150, 141, 255))
        brush66.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush66)
        brush67 = QBrush(QColor(89, 125, 117, 255))
        brush67.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush67)
        brush68 = QBrush(QColor(36, 50, 47, 255))
        brush68.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush68)
        brush69 = QBrush(QColor(47, 67, 63, 255))
        brush69.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush69)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush65)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush65)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush70 = QBrush(QColor(35, 50, 47, 255))
        brush70.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush70)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush61)
#endif
        palette9.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush65)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush66)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush67)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush68)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush69)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush65)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush65)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush70)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush61)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush68)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush65)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush66)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush67)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush68)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush69)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush68)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush68)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush65)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush65)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush71 = QBrush(QColor(71, 100, 94, 255))
        brush71.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush71)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush72 = QBrush(QColor(36, 50, 47, 127))
        brush72.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush72)
#endif
        brush73 = QBrush(QColor(50, 70, 66, 255))
        brush73.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Disabled, QPalette.Accent, brush73)
        self.undoScan.setPalette(palette9)

        self.gridLayout_4.addWidget(self.undoScan, 5, 1, 1, 1)

        self.clearButton = QPushButton(self.checkout)
        self.clearButton.setObjectName(u"clearButton")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush12)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush14)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush16)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette10.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush12)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush16)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush17)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.Accent, brush19)
        self.clearButton.setPalette(palette10)
        self.clearButton.setAutoFillBackground(False)
        self.clearButton.setCheckable(False)
        self.clearButton.setAutoDefault(False)

        self.gridLayout_4.addWidget(self.clearButton, 6, 1, 1, 1)

        self.priceLabel = QLabel(self.checkout)
        self.priceLabel.setObjectName(u"priceLabel")
        self.priceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.priceLabel, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 7, 1, 1, 1)

        self.checkoutTab.addTab(self.checkout, "")
        self.addHardware = QWidget()
        self.addHardware.setObjectName(u"addHardware")
        self.gridLayout = QGridLayout(self.addHardware)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.addHardware)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)

        self.label_7 = QLabel(self.addHardware)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 2)

        self.label_8 = QLabel(self.addHardware)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.addHardwareButton = QPushButton(self.addHardware)
        self.addHardwareButton.setObjectName(u"addHardwareButton")

        self.gridLayout.addWidget(self.addHardwareButton, 11, 2, 1, 1)

        self.headEdit = QLineEdit(self.addHardware)
        self.headEdit.setObjectName(u"headEdit")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush6)
        brush74 = QBrush(QColor(101, 132, 204, 255))
        brush74.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush74)
        brush75 = QBrush(QColor(84, 110, 170, 255))
        brush75.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush75)
        brush76 = QBrush(QColor(34, 44, 68, 255))
        brush76.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush76)
        brush77 = QBrush(QColor(45, 59, 91, 255))
        brush77.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush77)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush78 = QBrush(QColor(128, 128, 128, 255))
        brush78.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Highlight, brush78)
        palette11.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        brush79 = QBrush(QColor(161, 171, 195, 255))
        brush79.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush79)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette11.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush74)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush75)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush76)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush77)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Highlight, brush78)
        palette11.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush79)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush76)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush74)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush75)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush76)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush77)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush76)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush76)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Highlight, brush78)
        palette11.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
        brush80 = QBrush(QColor(67, 88, 136, 255))
        brush80.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush80)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush81 = QBrush(QColor(34, 44, 68, 127))
        brush81.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush81)
#endif
        brush82 = QBrush(QColor(87, 114, 177, 255))
        brush82.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Disabled, QPalette.Accent, brush82)
        self.headEdit.setPalette(palette11)
        self.headEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.headEdit, 1, 2, 1, 1)

        self.priceMultiUpdate = QPushButton(self.addHardware)
        self.priceMultiUpdate.setObjectName(u"priceMultiUpdate")

        self.gridLayout.addWidget(self.priceMultiUpdate, 12, 2, 1, 1)

        self.lengthEdit = QLineEdit(self.addHardware)
        self.lengthEdit.setObjectName(u"lengthEdit")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush74)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush75)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush76)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush77)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette12.setBrush(QPalette.Active, QPalette.Highlight, brush78)
        palette12.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush79)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette12.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush74)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush75)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush76)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush77)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Highlight, brush78)
        palette12.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush79)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush76)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush74)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush75)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush76)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush77)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush76)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush76)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Highlight, brush78)
        palette12.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush80)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush81)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.Accent, brush82)
        self.lengthEdit.setPalette(palette12)

        self.gridLayout.addWidget(self.lengthEdit, 3, 2, 1, 1)

        self.pkgEdit = QLineEdit(self.addHardware)
        self.pkgEdit.setObjectName(u"pkgEdit")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush74)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush75)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush76)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush77)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette13.setBrush(QPalette.Active, QPalette.Highlight, brush78)
        palette13.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush79)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette13.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush74)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush75)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush76)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush77)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Highlight, brush78)
        palette13.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush79)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush76)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush74)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush75)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush76)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush77)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush76)
        palette13.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush76)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Highlight, brush78)
        palette13.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush80)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush81)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.Accent, brush82)
        self.pkgEdit.setPalette(palette13)

        self.gridLayout.addWidget(self.pkgEdit, 6, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 10, 2, 1, 1)

        self.priceEdit = QLineEdit(self.addHardware)
        self.priceEdit.setObjectName(u"priceEdit")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush74)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush75)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush76)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush77)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette14.setBrush(QPalette.Active, QPalette.Highlight, brush78)
        palette14.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush79)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette14.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush74)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush75)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush76)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush77)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Highlight, brush78)
        palette14.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush79)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush76)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush74)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush75)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush76)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush77)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush76)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush76)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Highlight, brush78)
        palette14.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush80)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush81)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.Accent, brush82)
        self.priceEdit.setPalette(palette14)

        self.gridLayout.addWidget(self.priceEdit, 5, 2, 1, 1)

        self.reorder = QLineEdit(self.addHardware)
        self.reorder.setObjectName(u"reorder")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush74)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush75)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush76)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush77)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette15.setBrush(QPalette.Active, QPalette.Highlight, brush78)
        palette15.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush79)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette15.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush74)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush75)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush76)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush77)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Highlight, brush78)
        palette15.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush79)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush76)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush74)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush75)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush76)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush77)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush76)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush76)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Highlight, brush78)
        palette15.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush80)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush81)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.Accent, brush82)
        self.reorder.setPalette(palette15)

        self.gridLayout.addWidget(self.reorder, 9, 2, 1, 1)

        self.sizeEdit = QLineEdit(self.addHardware)
        self.sizeEdit.setObjectName(u"sizeEdit")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush74)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush75)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush76)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush77)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette16.setBrush(QPalette.Active, QPalette.Highlight, brush78)
        palette16.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush79)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette16.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush74)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush75)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush76)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush77)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Highlight, brush78)
        palette16.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush79)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush76)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush74)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush75)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush76)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush77)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush76)
        palette16.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush76)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Highlight, brush78)
        palette16.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush80)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush81)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.Accent, brush82)
        self.sizeEdit.setPalette(palette16)

        self.gridLayout.addWidget(self.sizeEdit, 2, 2, 1, 1)

        self.mcmasterEdit = QLineEdit(self.addHardware)
        self.mcmasterEdit.setObjectName(u"mcmasterEdit")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush74)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush75)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush76)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush77)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette17.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette17.setBrush(QPalette.Active, QPalette.Highlight, brush78)
        palette17.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush79)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette17.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette17.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush74)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush75)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush76)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush77)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Highlight, brush78)
        palette17.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush79)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette17.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush76)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush74)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush75)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush76)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush77)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush76)
        palette17.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush76)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Highlight, brush78)
        palette17.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush80)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette17.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush81)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.Accent, brush82)
        self.mcmasterEdit.setPalette(palette17)

        self.gridLayout.addWidget(self.mcmasterEdit, 4, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_7, 14, 2, 1, 1)

        self.mondayButton = QPushButton(self.addHardware)
        self.mondayButton.setObjectName(u"mondayButton")

        self.gridLayout.addWidget(self.mondayButton, 13, 2, 1, 1)

        self.label_4 = QLabel(self.addHardware)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_6 = QLabel(self.addHardware)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 2)

        self.label_9 = QLabel(self.addHardware)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.label_10 = QLabel(self.addHardware)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 2)

        self.label_3 = QLabel(self.addHardware)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 14, 0, 1, 1)

        self.quantityEdit = QLineEdit(self.addHardware)
        self.quantityEdit.setObjectName(u"quantityEdit")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush74)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush75)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush76)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush77)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette18.setBrush(QPalette.Active, QPalette.Highlight, brush78)
        palette18.setBrush(QPalette.Active, QPalette.HighlightedText, brush6)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush79)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette18.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette18.setBrush(QPalette.Active, QPalette.Accent, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush74)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush75)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush76)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush77)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Highlight, brush78)
        palette18.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush79)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette18.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.Accent, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush76)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush74)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush75)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush76)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush77)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush76)
        palette18.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush76)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Highlight, brush78)
        palette18.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush6)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush80)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette18.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush81)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.Accent, brush82)
        self.quantityEdit.setPalette(palette18)

        self.gridLayout.addWidget(self.quantityEdit, 8, 2, 1, 1)

        self.threadEdit = QComboBox(self.addHardware)
        self.threadEdit.addItem("")
        self.threadEdit.addItem("")
        self.threadEdit.addItem("")
        self.threadEdit.setObjectName(u"threadEdit")

        self.gridLayout.addWidget(self.threadEdit, 7, 2, 1, 1)

        self.label_5 = QLabel(self.addHardware)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)

        self.label_2 = QLabel(self.addHardware)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.checkoutTab.addTab(self.addHardware, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.logViewer = QPlainTextEdit(self.tab)
        self.logViewer.setObjectName(u"logViewer")

        self.gridLayout_6.addWidget(self.logViewer, 0, 0, 1, 1)

        self.checkoutTab.addTab(self.tab, "")
        self.updateStockPrice = QWidget()
        self.updateStockPrice.setObjectName(u"updateStockPrice")
        self.gridLayout_7 = QGridLayout(self.updateStockPrice)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.resetButton_2 = QPushButton(self.updateStockPrice)
        self.resetButton_2.setObjectName(u"resetButton_2")

        self.gridLayout_7.addWidget(self.resetButton_2, 11, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_5, 6, 1, 1, 1)

        self.stockTable = QListWidget(self.updateStockPrice)
        self.stockTable.setObjectName(u"stockTable")

        self.gridLayout_7.addWidget(self.stockTable, 0, 0, 12, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.instructionButton_2 = QPushButton(self.updateStockPrice)
        self.instructionButton_2.setObjectName(u"instructionButton_2")

        self.gridLayout_7.addWidget(self.instructionButton_2, 8, 1, 1, 1)

        self.selectPartButton = QPushButton(self.updateStockPrice)
        self.selectPartButton.setObjectName(u"selectPartButton")

        self.gridLayout_7.addWidget(self.selectPartButton, 9, 1, 1, 1)

        self.typeBox = QComboBox(self.updateStockPrice)
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.setObjectName(u"typeBox")
        self.typeBox.setMinimumSize(QSize(125, 36))
        self.typeBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_7.addWidget(self.typeBox, 1, 1, 1, 1)

        self.stockTypeLabel = QLabel(self.updateStockPrice)
        self.stockTypeLabel.setObjectName(u"stockTypeLabel")
        self.stockTypeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.stockTypeLabel, 0, 1, 1, 1)

        self.materialLabel = QLabel(self.updateStockPrice)
        self.materialLabel.setObjectName(u"materialLabel")
        self.materialLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.materialLabel, 2, 1, 1, 1)

        self.priceUpdateValue = QLabel(self.updateStockPrice)
        self.priceUpdateValue.setObjectName(u"priceUpdateValue")
        self.priceUpdateValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.priceUpdateValue, 5, 1, 1, 1)

        self.calcButton_2 = QPushButton(self.updateStockPrice)
        self.calcButton_2.setObjectName(u"calcButton_2")

        self.gridLayout_7.addWidget(self.calcButton_2, 10, 1, 1, 1)

        self.matBox = QComboBox(self.updateStockPrice)
        self.matBox.addItem("")
        self.matBox.addItem("")
        self.matBox.addItem("")
        self.matBox.addItem("")
        self.matBox.setObjectName(u"matBox")

        self.gridLayout_7.addWidget(self.matBox, 3, 1, 1, 1)

        self.checkoutTab.addTab(self.updateStockPrice, "")
        self.splitter.addWidget(self.checkoutTab)

        self.gridLayout_2.addWidget(self.splitter, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1184, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.purchaseTab.setCurrentIndex(0)
        self.checkoutTab.setCurrentIndex(3)
        self.memButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.QRscan.setText(QCoreApplication.translate("MainWindow", u"McMaster Part Number", None))
        self.clearSearch.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lengthSearch.setItemText(0, QCoreApplication.translate("MainWindow", u"Length", None))
        self.lengthSearch.setItemText(1, QCoreApplication.translate("MainWindow", u"1/16\"", None))
        self.lengthSearch.setItemText(2, QCoreApplication.translate("MainWindow", u"3/32\"", None))
        self.lengthSearch.setItemText(3, QCoreApplication.translate("MainWindow", u"5/32\"", None))
        self.lengthSearch.setItemText(4, QCoreApplication.translate("MainWindow", u"9/32\"", None))
        self.lengthSearch.setItemText(5, QCoreApplication.translate("MainWindow", u"1/8\"", None))
        self.lengthSearch.setItemText(6, QCoreApplication.translate("MainWindow", u"3/16\"", None))
        self.lengthSearch.setItemText(7, QCoreApplication.translate("MainWindow", u"1/4\"", None))
        self.lengthSearch.setItemText(8, QCoreApplication.translate("MainWindow", u"5/16\"", None))
        self.lengthSearch.setItemText(9, QCoreApplication.translate("MainWindow", u"3/8\"", None))
        self.lengthSearch.setItemText(10, QCoreApplication.translate("MainWindow", u"7/16\"", None))
        self.lengthSearch.setItemText(11, QCoreApplication.translate("MainWindow", u"1/2\"", None))
        self.lengthSearch.setItemText(12, QCoreApplication.translate("MainWindow", u"9/16\"", None))
        self.lengthSearch.setItemText(13, QCoreApplication.translate("MainWindow", u"5/8\"", None))
        self.lengthSearch.setItemText(14, QCoreApplication.translate("MainWindow", u"3/4\"", None))
        self.lengthSearch.setItemText(15, QCoreApplication.translate("MainWindow", u"7/8\"", None))
        self.lengthSearch.setItemText(16, QCoreApplication.translate("MainWindow", u"1\"", None))
        self.lengthSearch.setItemText(17, QCoreApplication.translate("MainWindow", u"1 1/8\"", None))
        self.lengthSearch.setItemText(18, QCoreApplication.translate("MainWindow", u"1 1/4\"", None))
        self.lengthSearch.setItemText(19, QCoreApplication.translate("MainWindow", u"1 3/8\"", None))
        self.lengthSearch.setItemText(20, QCoreApplication.translate("MainWindow", u"1 1/2\"", None))
        self.lengthSearch.setItemText(21, QCoreApplication.translate("MainWindow", u"1 5/8\"", None))
        self.lengthSearch.setItemText(22, QCoreApplication.translate("MainWindow", u"1 3/4\"", None))
        self.lengthSearch.setItemText(23, QCoreApplication.translate("MainWindow", u"1 7/8\"", None))
        self.lengthSearch.setItemText(24, QCoreApplication.translate("MainWindow", u"2\"", None))
        self.lengthSearch.setItemText(25, QCoreApplication.translate("MainWindow", u"2 1/4\"", None))
        self.lengthSearch.setItemText(26, QCoreApplication.translate("MainWindow", u"2 1/2\"", None))
        self.lengthSearch.setItemText(27, QCoreApplication.translate("MainWindow", u"2 3/4\"", None))
        self.lengthSearch.setItemText(28, QCoreApplication.translate("MainWindow", u"2 3/4\"", None))
        self.lengthSearch.setItemText(29, QCoreApplication.translate("MainWindow", u"3\"", None))
        self.lengthSearch.setItemText(30, QCoreApplication.translate("MainWindow", u"3 1/4\"", None))
        self.lengthSearch.setItemText(31, QCoreApplication.translate("MainWindow", u"3 1/2\"", None))
        self.lengthSearch.setItemText(32, QCoreApplication.translate("MainWindow", u"3 3/4\"", None))
        self.lengthSearch.setItemText(33, QCoreApplication.translate("MainWindow", u"4\"", None))
        self.lengthSearch.setItemText(34, QCoreApplication.translate("MainWindow", u"5\"", None))
        self.lengthSearch.setItemText(35, QCoreApplication.translate("MainWindow", u"6\"", None))
        self.lengthSearch.setItemText(36, QCoreApplication.translate("MainWindow", u"3", None))
        self.lengthSearch.setItemText(37, QCoreApplication.translate("MainWindow", u"4", None))
        self.lengthSearch.setItemText(38, QCoreApplication.translate("MainWindow", u"5", None))
        self.lengthSearch.setItemText(39, QCoreApplication.translate("MainWindow", u"6", None))
        self.lengthSearch.setItemText(40, QCoreApplication.translate("MainWindow", u"8", None))
        self.lengthSearch.setItemText(41, QCoreApplication.translate("MainWindow", u"10", None))
        self.lengthSearch.setItemText(42, QCoreApplication.translate("MainWindow", u"12", None))
        self.lengthSearch.setItemText(43, QCoreApplication.translate("MainWindow", u"14", None))
        self.lengthSearch.setItemText(44, QCoreApplication.translate("MainWindow", u"15", None))
        self.lengthSearch.setItemText(45, QCoreApplication.translate("MainWindow", u"16", None))
        self.lengthSearch.setItemText(46, QCoreApplication.translate("MainWindow", u"18", None))
        self.lengthSearch.setItemText(47, QCoreApplication.translate("MainWindow", u"20", None))
        self.lengthSearch.setItemText(48, QCoreApplication.translate("MainWindow", u"22", None))
        self.lengthSearch.setItemText(49, QCoreApplication.translate("MainWindow", u"25", None))
        self.lengthSearch.setItemText(50, QCoreApplication.translate("MainWindow", u"30", None))
        self.lengthSearch.setItemText(51, QCoreApplication.translate("MainWindow", u"35", None))
        self.lengthSearch.setItemText(52, QCoreApplication.translate("MainWindow", u"40", None))
        self.lengthSearch.setItemText(53, QCoreApplication.translate("MainWindow", u"45", None))
        self.lengthSearch.setItemText(54, QCoreApplication.translate("MainWindow", u"50", None))
        self.lengthSearch.setItemText(55, QCoreApplication.translate("MainWindow", u"55", None))
        self.lengthSearch.setItemText(56, QCoreApplication.translate("MainWindow", u"60", None))
        self.lengthSearch.setItemText(57, QCoreApplication.translate("MainWindow", u"65", None))
        self.lengthSearch.setItemText(58, QCoreApplication.translate("MainWindow", u"70", None))
        self.lengthSearch.setItemText(59, QCoreApplication.translate("MainWindow", u"75", None))
        self.lengthSearch.setItemText(60, QCoreApplication.translate("MainWindow", u"80", None))
        self.lengthSearch.setItemText(61, QCoreApplication.translate("MainWindow", u"90", None))
        self.lengthSearch.setItemText(62, QCoreApplication.translate("MainWindow", u"100", None))
        self.lengthSearch.setItemText(63, QCoreApplication.translate("MainWindow", u"110", None))
        self.lengthSearch.setItemText(64, QCoreApplication.translate("MainWindow", u"120", None))

        self.sizeSearch.setItemText(0, QCoreApplication.translate("MainWindow", u"Size", None))
        self.sizeSearch.setItemText(1, QCoreApplication.translate("MainWindow", u"1x64", None))
        self.sizeSearch.setItemText(2, QCoreApplication.translate("MainWindow", u"2x56", None))
        self.sizeSearch.setItemText(3, QCoreApplication.translate("MainWindow", u"3x48", None))
        self.sizeSearch.setItemText(4, QCoreApplication.translate("MainWindow", u"4x40", None))
        self.sizeSearch.setItemText(5, QCoreApplication.translate("MainWindow", u"5x40", None))
        self.sizeSearch.setItemText(6, QCoreApplication.translate("MainWindow", u"6x40", None))
        self.sizeSearch.setItemText(7, QCoreApplication.translate("MainWindow", u"6x32", None))
        self.sizeSearch.setItemText(8, QCoreApplication.translate("MainWindow", u"8x32", None))
        self.sizeSearch.setItemText(9, QCoreApplication.translate("MainWindow", u"10x24", None))
        self.sizeSearch.setItemText(10, QCoreApplication.translate("MainWindow", u"10x32", None))
        self.sizeSearch.setItemText(11, QCoreApplication.translate("MainWindow", u"1/4x20", None))
        self.sizeSearch.setItemText(12, QCoreApplication.translate("MainWindow", u"1/4x28", None))
        self.sizeSearch.setItemText(13, QCoreApplication.translate("MainWindow", u"5/16x18", None))
        self.sizeSearch.setItemText(14, QCoreApplication.translate("MainWindow", u"5/16x28", None))
        self.sizeSearch.setItemText(15, QCoreApplication.translate("MainWindow", u"3/8x16", None))
        self.sizeSearch.setItemText(16, QCoreApplication.translate("MainWindow", u"3/8x24", None))
        self.sizeSearch.setItemText(17, QCoreApplication.translate("MainWindow", u"7/16x14", None))
        self.sizeSearch.setItemText(18, QCoreApplication.translate("MainWindow", u"7/16x20", None))
        self.sizeSearch.setItemText(19, QCoreApplication.translate("MainWindow", u"1/2x20", None))
        self.sizeSearch.setItemText(20, QCoreApplication.translate("MainWindow", u"1/2x13", None))
        self.sizeSearch.setItemText(21, QCoreApplication.translate("MainWindow", u"M2 x .4mm", None))
        self.sizeSearch.setItemText(22, QCoreApplication.translate("MainWindow", u"M2.5 x 0.45mm", None))
        self.sizeSearch.setItemText(23, QCoreApplication.translate("MainWindow", u"M3 x .5mm", None))
        self.sizeSearch.setItemText(24, QCoreApplication.translate("MainWindow", u"M4 x 0.7mm", None))
        self.sizeSearch.setItemText(25, QCoreApplication.translate("MainWindow", u"M5 x 0.8mm", None))
        self.sizeSearch.setItemText(26, QCoreApplication.translate("MainWindow", u"M6 x 1mm ", None))
        self.sizeSearch.setItemText(27, QCoreApplication.translate("MainWindow", u"M8 x 1.25mm", None))
        self.sizeSearch.setItemText(28, QCoreApplication.translate("MainWindow", u"M10 x 1.5mm", None))
        self.sizeSearch.setItemText(29, QCoreApplication.translate("MainWindow", u"M12 x 1.75mm", None))
        self.sizeSearch.setItemText(30, QCoreApplication.translate("MainWindow", u"No. 1", None))
        self.sizeSearch.setItemText(31, QCoreApplication.translate("MainWindow", u"No. 2", None))
        self.sizeSearch.setItemText(32, QCoreApplication.translate("MainWindow", u"No. 3", None))
        self.sizeSearch.setItemText(33, QCoreApplication.translate("MainWindow", u"No. 4", None))
        self.sizeSearch.setItemText(34, QCoreApplication.translate("MainWindow", u"No. 5", None))
        self.sizeSearch.setItemText(35, QCoreApplication.translate("MainWindow", u"No. 6", None))
        self.sizeSearch.setItemText(36, QCoreApplication.translate("MainWindow", u"No. 8", None))
        self.sizeSearch.setItemText(37, QCoreApplication.translate("MainWindow", u"No. 10", None))
        self.sizeSearch.setItemText(38, QCoreApplication.translate("MainWindow", u"1/4\"", None))
        self.sizeSearch.setItemText(39, QCoreApplication.translate("MainWindow", u"5/16\"", None))
        self.sizeSearch.setItemText(40, QCoreApplication.translate("MainWindow", u"3/8\"", None))
        self.sizeSearch.setItemText(41, QCoreApplication.translate("MainWindow", u"7/16\"", None))
        self.sizeSearch.setItemText(42, QCoreApplication.translate("MainWindow", u"1/2\"", None))
        self.sizeSearch.setItemText(43, QCoreApplication.translate("MainWindow", u"M2", None))
        self.sizeSearch.setItemText(44, QCoreApplication.translate("MainWindow", u"M2.5", None))
        self.sizeSearch.setItemText(45, QCoreApplication.translate("MainWindow", u"M3", None))
        self.sizeSearch.setItemText(46, QCoreApplication.translate("MainWindow", u"M4", None))
        self.sizeSearch.setItemText(47, QCoreApplication.translate("MainWindow", u"M5", None))
        self.sizeSearch.setItemText(48, QCoreApplication.translate("MainWindow", u"M6", None))
        self.sizeSearch.setItemText(49, QCoreApplication.translate("MainWindow", u"M8", None))
        self.sizeSearch.setItemText(50, QCoreApplication.translate("MainWindow", u"M10", None))
        self.sizeSearch.setItemText(51, QCoreApplication.translate("MainWindow", u"M12", None))

        self.headSearch.setItemText(0, QCoreApplication.translate("MainWindow", u"Head Type", None))
        self.headSearch.setItemText(1, QCoreApplication.translate("MainWindow", u"Flat", None))
        self.headSearch.setItemText(2, QCoreApplication.translate("MainWindow", u"Button", None))
        self.headSearch.setItemText(3, QCoreApplication.translate("MainWindow", u"Socket", None))
        self.headSearch.setItemText(4, QCoreApplication.translate("MainWindow", u"Hex", None))
        self.headSearch.setItemText(5, QCoreApplication.translate("MainWindow", u"Set Screw", None))
        self.headSearch.setItemText(6, QCoreApplication.translate("MainWindow", u"Washer", None))
        self.headSearch.setItemText(7, QCoreApplication.translate("MainWindow", u"Nut", None))

        self.purchaseTab.setTabText(self.purchaseTab.indexOf(self.buyHardware), QCoreApplication.translate("MainWindow", u"Buy Hardware", None))
        self.stockLabel.setText(QCoreApplication.translate("MainWindow", u"Stock Type", None))
        self.stockDrop.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose Stock Type", None))
        self.stockDrop.setItemText(1, QCoreApplication.translate("MainWindow", u"Round Bar", None))
        self.stockDrop.setItemText(2, QCoreApplication.translate("MainWindow", u"Rectangular Bar/Plate", None))
        self.stockDrop.setItemText(3, QCoreApplication.translate("MainWindow", u"Round Tubing", None))
        self.stockDrop.setItemText(4, QCoreApplication.translate("MainWindow", u"Angle", None))
        self.stockDrop.setItemText(5, QCoreApplication.translate("MainWindow", u"Mesh", None))
        self.stockDrop.setItemText(6, QCoreApplication.translate("MainWindow", u"Structural (T-Slot)", None))
        self.stockDrop.setItemText(7, QCoreApplication.translate("MainWindow", u"All Thread", None))

        self.matDrop.setText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.metalDrop.setItemText(0, QCoreApplication.translate("MainWindow", u"Aluminum", None))
        self.metalDrop.setItemText(1, QCoreApplication.translate("MainWindow", u"Brass", None))
        self.metalDrop.setItemText(2, QCoreApplication.translate("MainWindow", u"Mild Steel", None))
        self.metalDrop.setItemText(3, QCoreApplication.translate("MainWindow", u"Stainless Steel", None))

        self.instructionButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Test1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.McTest.setText(QCoreApplication.translate("MainWindow", u"mcTest", None))
        self.purchaseTab.setTabText(self.purchaseTab.indexOf(self.buyStock), QCoreApplication.translate("MainWindow", u"Buy Stock", None))
        self.numPart.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.partLabel.setText(QCoreApplication.translate("MainWindow", u"# Parts", None))
        self.currPrice.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem = self.checkoutTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"McMaster Number", None));
        ___qtablewidgetitem1 = self.checkoutTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtablewidgetitem2 = self.checkoutTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Head", None));
        ___qtablewidgetitem3 = self.checkoutTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem4 = self.checkoutTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem5 = self.checkoutTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem6 = self.checkoutTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Checkout Date", None));
        self.memButton.setText(QCoreApplication.translate("MainWindow", u"Push to Memory", None))
        self.checkButton.setText(QCoreApplication.translate("MainWindow", u"Additional Info", None))
        self.undoScan.setText(QCoreApplication.translate("MainWindow", u"Removed Selected", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.priceLabel.setText(QCoreApplication.translate("MainWindow", u"Total Price", None))
        self.checkoutTab.setTabText(self.checkoutTab.indexOf(self.checkout), QCoreApplication.translate("MainWindow", u"Checkout", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"This format must match exactly the format in the \"Buy Hardware\" tab", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Package Quantity", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Thread", None))
        self.addHardwareButton.setText(QCoreApplication.translate("MainWindow", u"Add Hardware", None))
        self.priceMultiUpdate.setText(QCoreApplication.translate("MainWindow", u"Update Price Multiplier", None))
        self.mondayButton.setText(QCoreApplication.translate("MainWindow", u"Run Monday Automations", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"McMaster Price", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Our Quantity", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Reorder Quantity", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.threadEdit.setItemText(0, QCoreApplication.translate("MainWindow", u"Fully Threaded", None))
        self.threadEdit.setItemText(1, QCoreApplication.translate("MainWindow", u"Partially Threaded", None))
        self.threadEdit.setItemText(2, QCoreApplication.translate("MainWindow", u"N/A", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"McMaster Number", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Head", None))
        self.checkoutTab.setTabText(self.checkoutTab.indexOf(self.addHardware), QCoreApplication.translate("MainWindow", u"Add hardware", None))
        self.checkoutTab.setTabText(self.checkoutTab.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Log Viewer", None))
        self.resetButton_2.setText(QCoreApplication.translate("MainWindow", u"Reset Table", None))
        self.instructionButton_2.setText(QCoreApplication.translate("MainWindow", u"Click For Instructions", None))
        self.selectPartButton.setText(QCoreApplication.translate("MainWindow", u"Select Parts", None))
        self.typeBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Round Bar", None))
        self.typeBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Rectangular Bar/Plate", None))
        self.typeBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Round Tubing", None))
        self.typeBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Angle", None))
        self.typeBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Mesh", None))
        self.typeBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Structural (T-Slot)", None))
        self.typeBox.setItemText(6, QCoreApplication.translate("MainWindow", u"All Thread", None))

        self.stockTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Stock Type", None))
        self.materialLabel.setText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.priceUpdateValue.setText(QCoreApplication.translate("MainWindow", u"Price Update Value", None))
        self.calcButton_2.setText(QCoreApplication.translate("MainWindow", u"Calculate Price", None))
        self.matBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Aluminum", None))
        self.matBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Brass", None))
        self.matBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Mild Steel", None))
        self.matBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Stainless Steel", None))

        self.checkoutTab.setTabText(self.checkoutTab.indexOf(self.updateStockPrice), QCoreApplication.translate("MainWindow", u"Update Hardware Price", None))
    # retranslateUi

