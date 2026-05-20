# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Github\music\AIMG_GUI\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 803)
        MainWindow.setStyleSheet(" QScrollBar:vertical {\n"
"    border: none;\n"
"    margin: 15px 0 15px 0;\n"
"    background-color: rgb(57, 65, 85);\n"
"    width: 14px;\n"
"    border-radius: 0px;\n"
"    \n"
" }\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(138, 104, 171);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"border: none;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    \n"
"    background-color: rgb(255, 37, 208);\n"
"\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(138, 104, 171);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(138, 104, 171);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"border: none;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.User = QtWidgets.QFrame(self.centralwidget)
        self.User.setGeometry(QtCore.QRect(0, 50, 151, 171))
        self.User.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.User.setFrameShadow(QtWidgets.QFrame.Raised)
        self.User.setObjectName("User")
        self.Tab_2 = QtWidgets.QLabel(self.User)
        self.Tab_2.setGeometry(QtCore.QRect(-120, -120, 260, 260))
        self.Tab_2.setStyleSheet("background-color: rgb(35, 39, 51);\n"
"border-radius: 130px;\n"
"")
        self.Tab_2.setText("")
        self.Tab_2.setObjectName("Tab_2")
        self.icon_twitch = QtWidgets.QLabel(self.User)
        self.icon_twitch.setGeometry(QtCore.QRect(12, 12, 86, 86))
        self.icon_twitch.setStyleSheet("")
        self.icon_twitch.setText("")
        self.icon_twitch.setTextFormat(QtCore.Qt.AutoText)
        self.icon_twitch.setPixmap(QtGui.QPixmap(":/Icons/assets/twitch_profile.jpg"))
        self.icon_twitch.setScaledContents(True)
        self.icon_twitch.setObjectName("icon_twitch")
        self.Menu = QtWidgets.QFrame(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(0, 210, 111, 491))
        self.Menu.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(114, 66, 228, 103), stop:0.619318 rgba(210, 62, 176, 90), stop:1 rgba(68, 244, 255, 90));\n"
"}\n"
"QPushButton:pressed{\n"
"border:2px solid white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.971591, y2:1, stop:0 rgba(0, 0, 0, 125), stop:1 rgba(255, 255, 255, 98));\n"
"}\n"
"QPushButton:checked{\n"
"border-left:10px solid qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.523, y2:1, stop:0 rgba(169, 62, 210, 255), stop:1 rgba(68, 244, 255, 255));\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.517, stop:0 rgba(34, 34, 34, 112), stop:1 rgba(143, 143, 143, 98));\n"
"}")
        self.Menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menu.setObjectName("Menu")
        self.Tab = QtWidgets.QLabel(self.Menu)
        self.Tab.setGeometry(QtCore.QRect(-40, 30, 140, 391))
        self.Tab.setStyleSheet("background-color: rgb(35, 39, 51);\n"
"border-bottom-right-radius:100;")
        self.Tab.setText("")
        self.Tab.setObjectName("Tab")
        self.btn_File_Browser = QtWidgets.QPushButton(self.Menu)
        self.btn_File_Browser.setEnabled(True)
        self.btn_File_Browser.setGeometry(QtCore.QRect(0, 30, 100, 100))
        self.btn_File_Browser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_File_Browser.setStyleSheet("")
        self.btn_File_Browser.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/assets/file_alt2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_File_Browser.setIcon(icon)
        self.btn_File_Browser.setIconSize(QtCore.QSize(50, 50))
        self.btn_File_Browser.setCheckable(True)
        self.btn_File_Browser.setChecked(True)
        self.btn_File_Browser.setAutoRepeat(False)
        self.btn_File_Browser.setAutoExclusive(True)
        self.btn_File_Browser.setAutoDefault(False)
        self.btn_File_Browser.setFlat(False)
        self.btn_File_Browser.setObjectName("btn_File_Browser")
        self.btn_Option = QtWidgets.QPushButton(self.Menu)
        self.btn_Option.setGeometry(QtCore.QRect(0, 130, 100, 100))
        self.btn_Option.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/assets/Option_alt.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/Icons/assets/Option_alt2.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.btn_Option.setIcon(icon1)
        self.btn_Option.setIconSize(QtCore.QSize(50, 50))
        self.btn_Option.setCheckable(True)
        self.btn_Option.setAutoExclusive(True)
        self.btn_Option.setFlat(False)
        self.btn_Option.setObjectName("btn_Option")
        self.btn_ChatnPlayer = QtWidgets.QPushButton(self.Menu)
        self.btn_ChatnPlayer.setGeometry(QtCore.QRect(0, 230, 100, 100))
        self.btn_ChatnPlayer.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/assets/ChatnPlay_alt2.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.btn_ChatnPlayer.setIcon(icon2)
        self.btn_ChatnPlayer.setIconSize(QtCore.QSize(50, 50))
        self.btn_ChatnPlayer.setCheckable(True)
        self.btn_ChatnPlayer.setAutoExclusive(True)
        self.btn_ChatnPlayer.setFlat(False)
        self.btn_ChatnPlayer.setObjectName("btn_ChatnPlayer")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setEnabled(True)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1280, 760))
        self.Background.setAutoFillBackground(False)
        self.Background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.5, y2:1, stop:0 rgba(170, 97, 212, 255), stop:1 rgba(156, 194, 255, 255));\n"
"border-radius:25px;")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.Titlebar = QtWidgets.QFrame(self.centralwidget)
        self.Titlebar.setGeometry(QtCore.QRect(0, 0, 1281, 51))
        self.Titlebar.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid white;\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 88), stop:1 rgba(127, 127, 127, 98));\n"
"}\n"
"QPushButton:pressed{\n"
"border:2px solid white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(36, 212, 243, 76), stop:1 rgba(62, 157, 210, 105));\n"
"}")
        self.Titlebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Titlebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Titlebar.setObjectName("Titlebar")
        self.Logo = QtWidgets.QLabel(self.Titlebar)
        self.Logo.setGeometry(QtCore.QRect(10, 0, 50, 50))
        self.Logo.setStyleSheet("color: rgb(255, 255, 255); \n"
"font: 14pt \"Agency FB\";")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/Icons/assets/LOGO.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo.setObjectName("Logo")
        self.bg_Titlebar = QtWidgets.QLabel(self.Titlebar)
        self.bg_Titlebar.setGeometry(QtCore.QRect(0, 0, 1280, 50))
        self.bg_Titlebar.setStyleSheet("background-color: rgb(35, 39, 51);\n"
"border-bottom-right-radius:35px;\n"
"border-top-left-radius:25px")
        self.bg_Titlebar.setText("")
        self.bg_Titlebar.setObjectName("bg_Titlebar")
        self.name_Titlebar = QtWidgets.QLabel(self.Titlebar)
        self.name_Titlebar.setGeometry(QtCore.QRect(70, 5, 401, 36))
        self.name_Titlebar.setStyleSheet("font:16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.name_Titlebar.setObjectName("name_Titlebar")
        self.btn_Exit = QtWidgets.QPushButton(self.Titlebar)
        self.btn_Exit.setGeometry(QtCore.QRect(1200, 0, 50, 50))
        self.btn_Exit.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/assets/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Exit.setIcon(icon3)
        self.btn_Exit.setIconSize(QtCore.QSize(32, 32))
        self.btn_Exit.setFlat(True)
        self.btn_Exit.setObjectName("btn_Exit")
        self.btn_Min = QtWidgets.QPushButton(self.Titlebar)
        self.btn_Min.setGeometry(QtCore.QRect(1150, 0, 50, 50))
        self.btn_Min.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/assets/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Min.setIcon(icon4)
        self.btn_Min.setIconSize(QtCore.QSize(32, 32))
        self.btn_Min.setObjectName("btn_Min")
        self.bg_Titlebar.raise_()
        self.name_Titlebar.raise_()
        self.Logo.raise_()
        self.btn_Exit.raise_()
        self.btn_Min.raise_()
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(160, 80, 1071, 651))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.Pages_Channel = QtWidgets.QFrame(self.page)
        self.Pages_Channel.setGeometry(QtCore.QRect(0, 0, 1071, 651))
        self.Pages_Channel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pages_Channel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Pages_Channel.setObjectName("Pages_Channel")
        self.Page_icon_Channel = QtWidgets.QLabel(self.Pages_Channel)
        self.Page_icon_Channel.setGeometry(QtCore.QRect(20, 20, 60, 60))
        self.Page_icon_Channel.setStyleSheet("background-image: url(:/Icons/12423272.png);\n"
"color: rgb(255, 255, 255);")
        self.Page_icon_Channel.setText("")
        self.Page_icon_Channel.setPixmap(QtGui.QPixmap(":/Icons/assets/file_alt2.png"))
        self.Page_icon_Channel.setScaledContents(True)
        self.Page_icon_Channel.setAlignment(QtCore.Qt.AlignCenter)
        self.Page_icon_Channel.setObjectName("Page_icon_Channel")
        self.Title_Channel = QtWidgets.QLabel(self.Pages_Channel)
        self.Title_Channel.setGeometry(QtCore.QRect(110, 20, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title_Channel.setFont(font)
        self.Title_Channel.setStyleSheet("font: 25pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.Title_Channel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Title_Channel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Title_Channel.setObjectName("Title_Channel")
        self.line_4 = QtWidgets.QFrame(self.Pages_Channel)
        self.line_4.setGeometry(QtCore.QRect(0, 100, 1071, 2))
        self.line_4.setAutoFillBackground(False)
        self.line_4.setStyleSheet("border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0.477318, y1:0, x2:0.5, y2:1, stop:0 rgba(114, 66, 228, 255), stop:0.613636 rgba(210, 62, 176, 255), stop:1 rgba(68, 244, 255, 255));")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.btn_import_file = QtWidgets.QPushButton(self.Pages_Channel)
        self.btn_import_file.setEnabled(True)
        self.btn_import_file.setGeometry(QtCore.QRect(20, 110, 71, 71))
        self.btn_import_file.setStyleSheet("QPushButton{\n"
"\n"
"border-radius:5px;\n"
"font:500 24pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 97, 242);\n"
"border-top:2px solid rgb(105, 97, 242);\n"
"border-left:2px solid rgb(76, 71, 177);\n"
"border-right:2px solid rgb(76, 71, 177);\n"
"border-bottom:5px solid rgb(76, 71, 177);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(82, 122, 255);\n"
"border-top:2px solid rgb(82, 122, 255);\n"
"border-left:2px solid rgb(76, 71, 177);\n"
"border-right:2px solid rgb(76, 71, 177);\n"
"border-bottom:5px solid rgb(76, 71, 177);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(76, 71, 177);\n"
"border:none;\n"
"}\n"
"QPushButton:disabled{\n"
"background-color:rgb(148, 148, 148);\n"
"border-top:2px solid rgb(148, 148, 148);\n"
"border-left:2px solid rgb(94, 94, 94);\n"
"border-right:2px solid rgb(94, 94, 94);\n"
"border-bottom:5px solid rgb(94, 94, 94);\n"
"}\n"
"")
        self.btn_import_file.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/assets/open_file_alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_import_file.setIcon(icon5)
        self.btn_import_file.setIconSize(QtCore.QSize(50, 50))
        self.btn_import_file.setFlat(False)
        self.btn_import_file.setObjectName("btn_import_file")
        self.Bg_Channel = QtWidgets.QLabel(self.Pages_Channel)
        self.Bg_Channel.setGeometry(QtCore.QRect(0, 0, 1071, 651))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Bg_Channel.setFont(font)
        self.Bg_Channel.setStyleSheet("background-color: rgb(35, 39, 51);\n"
"border-radius:25px\n"
"")
        self.Bg_Channel.setText("")
        self.Bg_Channel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Bg_Channel.setObjectName("Bg_Channel")
        self.scrollArea = QtWidgets.QScrollArea(self.Pages_Channel)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(20, 220, 1031, 401))
        self.scrollArea.setStyleSheet("\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    margin: 15px 0 15px 0;\n"
"    background-color: rgb(57, 65, 85);\n"
"    width: 14px;\n"
"    border-radius: 0px;\n"
"    \n"
" }\n"
"QScrollBar::handle::vertical {    \n"
"    background-color: rgb(116, 187, 220);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"border: none;\n"
"}\n"
"QScrollBar::handle:vertical::hover{    \n"
"    \n"
"    background-color: rgb(127, 223, 252);\n"
"\n"
"}\n"
"QScrollBar::handle:vertical::pressed {    \n"
"    background-color: rgb(7, 203, 148);\n"
"}\n"
"QScrollBar::sub-line::vertical {\n"
"    border: none;\n"
"    background-color: rgb(116, 187, 220);;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical::hover {    \n"
"    background-color: rgb(127, 223, 252);\n"
"}\n"
"QScrollBar::sub-line::vertical::pressed {    \n"
"    background-color: rgb(7, 203, 148);\n"
"}\n"
"QScrollBar::add-line::vertical {\n"
"    border: none;\n"
"    background-color:  rgb(116, 187, 220);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line::vertical::hover {    \n"
"    background-color: rgb(127, 223, 252);\n"
"border: none;\n"
"}\n"
"QScrollBar::add-line::vertical::pressed {    \n"
"    background-color: rgb(7, 203, 148);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow::vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page::vertical {\n"
"    background: none;\n"
"}\n"
"QScrollArea QWidget{\n"
"background-color: rgb(35, 39, 51);\n"
"border: 3px solid rgb(7, 203, 148);\n"
"}\n"
"")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1015, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btn_refresh = QtWidgets.QPushButton(self.Pages_Channel)
        self.btn_refresh.setGeometry(QtCore.QRect(110, 110, 71, 71))
        self.btn_refresh.setStyleSheet("QPushButton{\n"
"\n"
"border-radius:5px;\n"
"font:500 24pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(8, 189, 17);\n"
"border-top:2px solid rgb(5, 152, 10);\n"
"border-left:2px solidrgb(5, 152, 10);\n"
"border-right:2px solid rgb(5, 152, 10);\n"
"border-bottom:5px solid rgb(5, 152, 10);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(8, 221, 15);\n"
"border-top:2px solid rgb(5, 152, 10);\n"
"border-left:2px solidrgb(5, 152, 10);\n"
"border-right:2px solid rgb(5, 152, 10);\n"
"border-bottom:5px solid rgb(5, 152, 10);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(5, 152, 10);\n"
"border:none;\n"
"}\n"
"QPushButton:disabled{\n"
"background-color:rgb(148, 148, 148);\n"
"border-top:2px solid rgb(148, 148, 148);\n"
"border-left:2px solid rgb(94, 94, 94);\n"
"border-right:2px solid rgb(94, 94, 94);\n"
"border-bottom:5px solid rgb(94, 94, 94);\n"
"}\n"
"\n"
"")
        self.btn_refresh.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/assets/refresh_alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_refresh.setIcon(icon6)
        self.btn_refresh.setIconSize(QtCore.QSize(50, 50))
        self.btn_refresh.setFlat(True)
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_train = QtWidgets.QPushButton(self.Pages_Channel)
        self.btn_train.setGeometry(QtCore.QRect(840, 170, 201, 41))
        self.btn_train.setStyleSheet("QPushButton{\n"
"\n"
"border-radius:5px;\n"
"font:500 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 97, 242);\n"
"border-top:2px solid rgb(105, 97, 242);\n"
"border-left:2px solid rgb(76, 71, 177);\n"
"border-right:2px solid rgb(76, 71, 177);\n"
"border-bottom:5px solid rgb(76, 71, 177);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(82, 122, 255);\n"
"border-top:2px solid rgb(82, 122, 255);\n"
"border-left:2px solid rgb(76, 71, 177);\n"
"border-right:2px solid rgb(76, 71, 177);\n"
"border-bottom:5px solid rgb(76, 71, 177);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(76, 71, 177);\n"
"border:none;\n"
"}\n"
"QPushButton:disabled{\n"
"background-color:rgb(148, 148, 148);\n"
"border-top:2px solid rgb(148, 148, 148);\n"
"border-left:2px solid rgb(94, 94, 94);\n"
"border-right:2px solid rgb(94, 94, 94);\n"
"border-bottom:5px solid rgb(94, 94, 94);\n"
"}\n"
"")
        self.btn_train.setObjectName("btn_train")
        self.btn_clear = QtWidgets.QPushButton(self.Pages_Channel)
        self.btn_clear.setGeometry(QtCore.QRect(200, 110, 71, 71))
        self.btn_clear.setStyleSheet("QPushButton{\n"
"\n"
"border-radius:5px;\n"
"font:500 24pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(213, 20, 56);\n"
"border-top:2px solid rgb(163, 15, 45);\n"
"border-left:2px solid  rgb(163, 15, 45);\n"
"border-right:2px solid  rgb(163, 15, 45);\n"
"border-bottom:5px solid  rgb(163, 15, 45);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 24, 31);\n"
"border-top:2px solid rgb(163, 15, 45);\n"
"border-left:2px solid  rgb(163, 15, 45);\n"
"border-right:2px solid  rgb(163, 15, 45);\n"
"border-bottom:5px solid  rgb(163, 15, 45);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(163, 15, 45);\n"
"border:none;\n"
"}\n"
"QPushButton:disabled{\n"
"background-color:rgb(148, 148, 148);\n"
"border-top:2px solid rgb(148, 148, 148);\n"
"border-left:2px solid rgb(94, 94, 94);\n"
"border-right:2px solid rgb(94, 94, 94);\n"
"border-bottom:5px solid rgb(94, 94, 94);\n"
"}\n"
"")
        self.btn_clear.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/assets/clear_alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_clear.setIcon(icon7)
        self.btn_clear.setIconSize(QtCore.QSize(50, 50))
        self.btn_clear.setFlat(True)
        self.btn_clear.setObjectName("btn_clear")
        self.rbtn_pos = QtWidgets.QPushButton(self.Pages_Channel)
        self.rbtn_pos.setGeometry(QtCore.QRect(20, 190, 111, 31))
        self.rbtn_pos.setStyleSheet("QPushButton{\n"
"background-color: rgb(116, 187, 220);\n"
"color: white;\n"
"font: 500 12pt \"Segoe UI\";\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-left:2px solid white;\n"
"border-right:2px solid white;\n"
"border-top:2px solid white;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(7, 203, 148);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color:rgb(148, 148, 148);\n"
"}\n"
"")
        self.rbtn_pos.setCheckable(True)
        self.rbtn_pos.setChecked(True)
        self.rbtn_pos.setAutoExclusive(True)
        self.rbtn_pos.setObjectName("rbtn_pos")
        self.rbtn_neu = QtWidgets.QPushButton(self.Pages_Channel)
        self.rbtn_neu.setGeometry(QtCore.QRect(130, 190, 111, 31))
        self.rbtn_neu.setStyleSheet("QPushButton{\n"
"background-color: rgb(116, 187, 220);\n"
"color: white;\n"
"font: 500 12pt \"Segoe UI\";\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-left:2px solid white;\n"
"border-right:2px solid white;\n"
"border-top:2px solid white;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(7, 203, 148);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color:rgb(148, 148, 148);\n"
"}")
        self.rbtn_neu.setCheckable(True)
        self.rbtn_neu.setAutoExclusive(True)
        self.rbtn_neu.setObjectName("rbtn_neu")
        self.rbtn_neg = QtWidgets.QPushButton(self.Pages_Channel)
        self.rbtn_neg.setGeometry(QtCore.QRect(240, 190, 111, 31))
        self.rbtn_neg.setStyleSheet("QPushButton{\n"
"background-color: rgb(116, 187, 220);\n"
"color: white;\n"
"font: 500 12pt \"Segoe UI\";\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-left:2px solid white;\n"
"border-right:2px solid white;\n"
"border-top:2px solid white;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(7, 203, 148);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color:rgb(148, 148, 148);\n"
"}")
        self.rbtn_neg.setCheckable(True)
        self.rbtn_neg.setAutoExclusive(True)
        self.rbtn_neg.setObjectName("rbtn_neg")
        self.label_count = QtWidgets.QLabel(self.Pages_Channel)
        self.label_count.setGeometry(QtCore.QRect(20, 620, 211, 31))
        self.label_count.setStyleSheet("font: 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_count.setObjectName("label_count")
        self.label_training = QtWidgets.QLabel(self.Pages_Channel)
        self.label_training.setGeometry(QtCore.QRect(640, 170, 191, 41))
        self.label_training.setStyleSheet("font:500 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_training.setObjectName("label_training")
        self.gif_loading = QtWidgets.QLabel(self.Pages_Channel)
        self.gif_loading.setGeometry(QtCore.QRect(560, 140, 70, 70))
        self.gif_loading.setText("")
        self.gif_loading.setScaledContents(True)
        self.gif_loading.setObjectName("gif_loading")
        self.Bg_Channel.raise_()
        self.Page_icon_Channel.raise_()
        self.Title_Channel.raise_()
        self.line_4.raise_()
        self.scrollArea.raise_()
        self.btn_import_file.raise_()
        self.btn_refresh.raise_()
        self.btn_train.raise_()
        self.btn_clear.raise_()
        self.rbtn_pos.raise_()
        self.rbtn_neu.raise_()
        self.rbtn_neg.raise_()
        self.label_count.raise_()
        self.label_training.raise_()
        self.gif_loading.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.Pages_Option = QtWidgets.QFrame(self.page_2)
        self.Pages_Option.setGeometry(QtCore.QRect(0, 0, 1071, 651))
        self.Pages_Option.setStyleSheet("QLabel{\n"
"font: 500 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid;\n"
" border-radius:25px;\n"
" background-color: palette(base);\n"
"color:#FFF;\n"
"font: 16pt \"Segoe UI\";\n"
"padding-left:20px;\n"
"background-color: rgb(35, 39, 51);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85,170,255);\n"
"}")
        self.Pages_Option.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pages_Option.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Pages_Option.setObjectName("Pages_Option")
        self.Page_icon_Option = QtWidgets.QLabel(self.Pages_Option)
        self.Page_icon_Option.setGeometry(QtCore.QRect(20, 20, 60, 60))
        self.Page_icon_Option.setStyleSheet("background-image: url(:/Icons/12423272.png);\n"
"color: rgb(255, 255, 255);")
        self.Page_icon_Option.setText("")
        self.Page_icon_Option.setPixmap(QtGui.QPixmap(":/Icons/assets/Option_alt2.png"))
        self.Page_icon_Option.setScaledContents(True)
        self.Page_icon_Option.setAlignment(QtCore.Qt.AlignCenter)
        self.Page_icon_Option.setObjectName("Page_icon_Option")
        self.PageTitle_Option = QtWidgets.QLabel(self.Pages_Option)
        self.PageTitle_Option.setGeometry(QtCore.QRect(110, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PageTitle_Option.setFont(font)
        self.PageTitle_Option.setStyleSheet("font: 25pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.PageTitle_Option.setObjectName("PageTitle_Option")
        self.line_2 = QtWidgets.QFrame(self.Pages_Option)
        self.line_2.setGeometry(QtCore.QRect(0, 100, 1071, 2))
        self.line_2.setAutoFillBackground(False)
        self.line_2.setStyleSheet("border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0.477318, y1:0, x2:0.5, y2:1, stop:0 rgba(114, 66, 228, 255), stop:0.613636 rgba(210, 62, 176, 255), stop:1 rgba(68, 244, 255, 255));")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.btn_Confirm_Option = QtWidgets.QPushButton(self.Pages_Option)
        self.btn_Confirm_Option.setGeometry(QtCore.QRect(860, 570, 161, 41))
        self.btn_Confirm_Option.setStyleSheet("QPushButton{\n"
"\n"
"border-radius:5px;\n"
"font:500 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 97, 242);\n"
"border-top:2px solid rgb(105, 97, 242);\n"
"border-left:2px solid rgb(76, 71, 177);\n"
"border-right:2px solid rgb(76, 71, 177);\n"
"border-bottom:5px solid rgb(76, 71, 177);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(82, 122, 255);\n"
"border-top:2px solid rgb(82, 122, 255);\n"
"border-left:2px solid rgb(76, 71, 177);\n"
"border-right:2px solid rgb(76, 71, 177);\n"
"border-bottom:5px solid rgb(76, 71, 177);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(76, 71, 177);\n"
"border:none;\n"
"}\n"
"\n"
"")
        self.btn_Confirm_Option.setObjectName("btn_Confirm_Option")
        self.bg_Option = QtWidgets.QLabel(self.Pages_Option)
        self.bg_Option.setGeometry(QtCore.QRect(0, 0, 1071, 651))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        self.bg_Option.setFont(font)
        self.bg_Option.setStyleSheet("background-color: rgb(35, 39, 51);\n"
"border-radius:25px\n"
"")
        self.bg_Option.setText("")
        self.bg_Option.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bg_Option.setObjectName("bg_Option")
        self.label_data = QtWidgets.QLabel(self.Pages_Option)
        self.label_data.setGeometry(QtCore.QRect(60, 290, 151, 45))
        self.label_data.setObjectName("label_data")
        self.label_bpm = QtWidgets.QLabel(self.Pages_Option)
        self.label_bpm.setGeometry(QtCore.QRect(490, 290, 81, 45))
        self.label_bpm.setStyleSheet("")
        self.label_bpm.setObjectName("label_bpm")
        self.edit_datarange = QtWidgets.QLineEdit(self.Pages_Option)
        self.edit_datarange.setGeometry(QtCore.QRect(50, 350, 251, 51))
        self.edit_datarange.setMaxLength(3)
        self.edit_datarange.setObjectName("edit_datarange")
        self.edit_BPM = QtWidgets.QLineEdit(self.Pages_Option)
        self.edit_BPM.setGeometry(QtCore.QRect(480, 350, 231, 51))
        self.edit_BPM.setObjectName("edit_BPM")
        self.label_instrument = QtWidgets.QLabel(self.Pages_Option)
        self.label_instrument.setGeometry(QtCore.QRect(60, 440, 171, 45))
        self.label_instrument.setObjectName("label_instrument")
        self.btn_midi_piano = QtWidgets.QPushButton(self.Pages_Option)
        self.btn_midi_piano.setGeometry(QtCore.QRect(80, 500, 100, 100))
        self.btn_midi_piano.setStyleSheet("QPushButton:hover{\n"
"    border:2px solid white;\n"
"}\n"
"QPushButton:checked{\n"
"    border:2px solid rgb(250, 185, 255);\n"
"    \n"
"    background-color: rgb(251, 229, 255);\n"
"}")
        self.btn_midi_piano.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Icons/assets/Piano.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.btn_midi_piano.setIcon(icon8)
        self.btn_midi_piano.setIconSize(QtCore.QSize(80, 80))
        self.btn_midi_piano.setCheckable(True)
        self.btn_midi_piano.setAutoExclusive(True)
        self.btn_midi_piano.setFlat(True)
        self.btn_midi_piano.setObjectName("btn_midi_piano")
        self.btn_midi_saxphone = QtWidgets.QPushButton(self.Pages_Option)
        self.btn_midi_saxphone.setGeometry(QtCore.QRect(230, 500, 100, 100))
        self.btn_midi_saxphone.setStyleSheet("QPushButton:hover{\n"
"    border:2px solid white;\n"
"}\n"
"QPushButton:checked{\n"
"    border:2px solid rgb(250, 185, 255);\n"
"    \n"
"    background-color: rgb(251, 229, 255);\n"
"}")
        self.btn_midi_saxphone.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Icons/assets/Saxphone.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.btn_midi_saxphone.setIcon(icon9)
        self.btn_midi_saxphone.setIconSize(QtCore.QSize(80, 80))
        self.btn_midi_saxphone.setCheckable(True)
        self.btn_midi_saxphone.setAutoExclusive(True)
        self.btn_midi_saxphone.setFlat(True)
        self.btn_midi_saxphone.setObjectName("btn_midi_saxphone")
        self.btn_midi_trumpet = QtWidgets.QPushButton(self.Pages_Option)
        self.btn_midi_trumpet.setGeometry(QtCore.QRect(380, 500, 100, 100))
        self.btn_midi_trumpet.setStyleSheet("QPushButton:hover{\n"
"    border:2px solid white;\n"
"}\n"
"QPushButton:checked{\n"
"    border:2px solid rgb(250, 185, 255);\n"
"    \n"
"    background-color: rgb(251, 229, 255);\n"
"}")
        self.btn_midi_trumpet.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Icons/assets/Trumpet.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.btn_midi_trumpet.setIcon(icon10)
        self.btn_midi_trumpet.setIconSize(QtCore.QSize(80, 80))
        self.btn_midi_trumpet.setCheckable(True)
        self.btn_midi_trumpet.setAutoExclusive(True)
        self.btn_midi_trumpet.setFlat(True)
        self.btn_midi_trumpet.setObjectName("btn_midi_trumpet")
        self.btn_midi_guitar = QtWidgets.QPushButton(self.Pages_Option)
        self.btn_midi_guitar.setGeometry(QtCore.QRect(530, 500, 100, 100))
        self.btn_midi_guitar.setStyleSheet("QPushButton:hover{\n"
"    border:2px solid white;\n"
"}\n"
"QPushButton:checked{\n"
"    border:2px solid rgb(250, 185, 255);\n"
"    \n"
"    background-color: rgb(251, 229, 255);\n"
"}")
        self.btn_midi_guitar.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Icons/assets/Guitar.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.btn_midi_guitar.setIcon(icon11)
        self.btn_midi_guitar.setIconSize(QtCore.QSize(80, 80))
        self.btn_midi_guitar.setCheckable(True)
        self.btn_midi_guitar.setAutoExclusive(True)
        self.btn_midi_guitar.setFlat(True)
        self.btn_midi_guitar.setObjectName("btn_midi_guitar")
        self.edit_ChannelID = QtWidgets.QLineEdit(self.Pages_Option)
        self.edit_ChannelID.setGeometry(QtCore.QRect(220, 200, 411, 51))
        self.edit_ChannelID.setObjectName("edit_ChannelID")
        self.Twitch_icon_Option = QtWidgets.QLabel(self.Pages_Option)
        self.Twitch_icon_Option.setGeometry(QtCore.QRect(80, 175, 100, 100))
        self.Twitch_icon_Option.setStyleSheet("")
        self.Twitch_icon_Option.setText("")
        self.Twitch_icon_Option.setTextFormat(QtCore.Qt.AutoText)
        self.Twitch_icon_Option.setScaledContents(True)
        self.Twitch_icon_Option.setObjectName("Twitch_icon_Option")
        self.label_instrument_2 = QtWidgets.QLabel(self.Pages_Option)
        self.label_instrument_2.setGeometry(QtCore.QRect(60, 120, 121, 45))
        self.label_instrument_2.setObjectName("label_instrument_2")
        self.bpm_error = QtWidgets.QLabel(self.Pages_Option)
        self.bpm_error.setGeometry(QtCore.QRect(570, 290, 141, 45))
        self.bpm_error.setStyleSheet("color: rgb(255, 255, 0);")
        self.bpm_error.setText("")
        self.bpm_error.setObjectName("bpm_error")
        self.data_error = QtWidgets.QLabel(self.Pages_Option)
        self.data_error.setGeometry(QtCore.QRect(240, 290, 241, 45))
        self.data_error.setStyleSheet("color: rgb(255, 255, 0);")
        self.data_error.setText("")
        self.data_error.setObjectName("data_error")
        self.id_error = QtWidgets.QLabel(self.Pages_Option)
        self.id_error.setGeometry(QtCore.QRect(220, 120, 331, 45))
        self.id_error.setStyleSheet("color: rgb(255, 255, 0);")
        self.id_error.setText("")
        self.id_error.setObjectName("id_error")
        self.midi_error = QtWidgets.QLabel(self.Pages_Option)
        self.midi_error.setGeometry(QtCore.QRect(260, 440, 281, 45))
        self.midi_error.setStyleSheet("color: rgb(255, 255, 0);")
        self.midi_error.setText("")
        self.midi_error.setObjectName("midi_error")
        self.bg_Option.raise_()
        self.Page_icon_Option.raise_()
        self.PageTitle_Option.raise_()
        self.line_2.raise_()
        self.btn_Confirm_Option.raise_()
        self.label_data.raise_()
        self.label_bpm.raise_()
        self.edit_datarange.raise_()
        self.edit_BPM.raise_()
        self.label_instrument.raise_()
        self.btn_midi_piano.raise_()
        self.btn_midi_saxphone.raise_()
        self.btn_midi_trumpet.raise_()
        self.btn_midi_guitar.raise_()
        self.edit_ChannelID.raise_()
        self.Twitch_icon_Option.raise_()
        self.label_instrument_2.raise_()
        self.bpm_error.raise_()
        self.data_error.raise_()
        self.id_error.raise_()
        self.midi_error.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.Pages_Chat = QtWidgets.QFrame(self.page_3)
        self.Pages_Chat.setGeometry(QtCore.QRect(0, 0, 471, 501))
        self.Pages_Chat.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pages_Chat.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Pages_Chat.setObjectName("Pages_Chat")
        self.Page_icon_Chat = QtWidgets.QLabel(self.Pages_Chat)
        self.Page_icon_Chat.setGeometry(QtCore.QRect(20, 20, 60, 60))
        self.Page_icon_Chat.setStyleSheet("background-image: url(:/Icons/12423272.png);\n"
"color: rgb(255, 255, 255);")
        self.Page_icon_Chat.setText("")
        self.Page_icon_Chat.setPixmap(QtGui.QPixmap(":/Icons/assets/ChatnPlay_alt2.png"))
        self.Page_icon_Chat.setScaledContents(True)
        self.Page_icon_Chat.setAlignment(QtCore.Qt.AlignCenter)
        self.Page_icon_Chat.setObjectName("Page_icon_Chat")
        self.PageTitle_Chat = QtWidgets.QLabel(self.Pages_Chat)
        self.PageTitle_Chat.setGeometry(QtCore.QRect(110, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PageTitle_Chat.setFont(font)
        self.PageTitle_Chat.setStyleSheet("font: 25pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.PageTitle_Chat.setObjectName("PageTitle_Chat")
        self.line_6 = QtWidgets.QFrame(self.Pages_Chat)
        self.line_6.setGeometry(QtCore.QRect(0, 100, 471, 2))
        self.line_6.setAutoFillBackground(False)
        self.line_6.setStyleSheet("border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0.477318, y1:0, x2:0.5, y2:1, stop:0 rgba(114, 66, 228, 255), stop:0.613636 rgba(210, 62, 176, 255), stop:1 rgba(68, 244, 255, 255));")
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.bg_Chat = QtWidgets.QLabel(self.Pages_Chat)
        self.bg_Chat.setGeometry(QtCore.QRect(0, 0, 481, 501))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.bg_Chat.setFont(font)
        self.bg_Chat.setStyleSheet("background-color: rgb(35, 39, 51);\n"
"border-top-left-radius:25px\n"
"")
        self.bg_Chat.setText("")
        self.bg_Chat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bg_Chat.setObjectName("bg_Chat")
        self.tEdit_Chatlog = QtWidgets.QTextEdit(self.Pages_Chat)
        self.tEdit_Chatlog.setGeometry(QtCore.QRect(0, 100, 471, 401))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(18)
        self.tEdit_Chatlog.setFont(font)
        self.tEdit_Chatlog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.483, y1:0, x2:0.5, y2:1, stop:0 rgba(85, 18, 123, 250), stop:1 rgba(0, 0, 0, 212));\n"
"color:#FFF;\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"border-top: 2px solid rgb(215, 92, 255);\n"
"font: 150 16pt \"微軟正黑體\";\n"
"\n"
"\n"
"")
        self.tEdit_Chatlog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tEdit_Chatlog.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tEdit_Chatlog.setPlaceholderText("")
        self.tEdit_Chatlog.setObjectName("tEdit_Chatlog")
        self.btn_chat = QtWidgets.QPushButton(self.Pages_Chat)
        self.btn_chat.setGeometry(QtCore.QRect(120, 260, 221, 81))
        self.btn_chat.setStyleSheet("QPushButton{\n"
"\n"
"border-radius:5px;\n"
"font:500 24pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 97, 242);\n"
"border-top:2px solid rgb(105, 97, 242);\n"
"border-left:2px solid rgb(76, 71, 177);\n"
"border-right:2px solid rgb(76, 71, 177);\n"
"border-bottom:5px solid rgb(76, 71, 177);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(82, 122, 255);\n"
"border-top:2px solid rgb(82, 122, 255);\n"
"border-left:2px solid rgb(76, 71, 177);\n"
"border-right:2px solid rgb(76, 71, 177);\n"
"border-bottom:5px solid rgb(76, 71, 177);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(76, 71, 177);\n"
"border:none;\n"
"}\n"
"")
        self.btn_chat.setObjectName("btn_chat")
        self.bg_Chat.raise_()
        self.Page_icon_Chat.raise_()
        self.PageTitle_Chat.raise_()
        self.line_6.raise_()
        self.tEdit_Chatlog.raise_()
        self.btn_chat.raise_()
        self.Pages_Playlist = QtWidgets.QFrame(self.page_3)
        self.Pages_Playlist.setGeometry(QtCore.QRect(500, 0, 571, 501))
        self.Pages_Playlist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pages_Playlist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Pages_Playlist.setObjectName("Pages_Playlist")
        self.PageTitle_Playlist = QtWidgets.QLabel(self.Pages_Playlist)
        self.PageTitle_Playlist.setGeometry(QtCore.QRect(110, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PageTitle_Playlist.setFont(font)
        self.PageTitle_Playlist.setStyleSheet("font: 25pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.PageTitle_Playlist.setObjectName("PageTitle_Playlist")
        self.line_7 = QtWidgets.QFrame(self.Pages_Playlist)
        self.line_7.setGeometry(QtCore.QRect(0, 100, 561, 2))
        self.line_7.setAutoFillBackground(False)
        self.line_7.setStyleSheet("border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0.477318, y1:0, x2:0.5, y2:1, stop:0 rgba(114, 66, 228, 255), stop:0.613636 rgba(210, 62, 176, 255), stop:1 rgba(68, 244, 255, 255));")
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.bg_Playlist = QtWidgets.QLabel(self.Pages_Playlist)
        self.bg_Playlist.setGeometry(QtCore.QRect(0, 0, 571, 501))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bg_Playlist.setFont(font)
        self.bg_Playlist.setStyleSheet("background-color: rgb(35, 39, 51);\n"
"border-top-right-radius:25px;\n"
"\n"
"font: 24pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.bg_Playlist.setText("")
        self.bg_Playlist.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bg_Playlist.setObjectName("bg_Playlist")
        self.label = QtWidgets.QLabel(self.Pages_Playlist)
        self.label.setGeometry(QtCore.QRect(20, 20, 60, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Icons/assets/Play_alt2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.music_list = QtWidgets.QListWidget(self.Pages_Playlist)
        self.music_list.setGeometry(QtCore.QRect(0, 100, 571, 401))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.music_list.setFont(font)
        self.music_list.setStyleSheet("QListWidget::item {\n"
"    background-color: transparent;\n"
"    color: #000000;\n"
"    border: transparent;\n"
"    padding: 25px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #f5f5f5;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: rgb(98, 104, 120);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QListWidget{\n"
"    background-color: transparent;\n"
"    border-top: 2px solid rgb(215, 92, 255);\n"
"}")
        self.music_list.setWordWrap(True)
        self.music_list.setObjectName("music_list")
        self.bg_Playlist.raise_()
        self.PageTitle_Playlist.raise_()
        self.line_7.raise_()
        self.label.raise_()
        self.music_list.raise_()
        self.Pages_Player = QtWidgets.QFrame(self.page_3)
        self.Pages_Player.setGeometry(QtCore.QRect(0, 530, 1071, 121))
        self.Pages_Player.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pages_Player.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Pages_Player.setObjectName("Pages_Player")
        self.bg_Playlist_5 = QtWidgets.QLabel(self.Pages_Player)
        self.bg_Playlist_5.setGeometry(QtCore.QRect(0, -10, 1071, 131))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.bg_Playlist_5.setFont(font)
        self.bg_Playlist_5.setStyleSheet("background-color: rgb(35, 39, 51);\n"
"border-bottom-left-radius:25px;\n"
"border-bottom-right-radius:25px;")
        self.bg_Playlist_5.setText("")
        self.bg_Playlist_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bg_Playlist_5.setObjectName("bg_Playlist_5")
        self.Audio_Slider = QtWidgets.QSlider(self.Pages_Player)
        self.Audio_Slider.setGeometry(QtCore.QRect(300, 70, 501, 21))
        self.Audio_Slider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #999999;\n"
"height: 14px;\n"
"\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 14px;\n"
"\n"
"margin:-1px;\n"
"background-color: rgb(85, 90, 104);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"background: lightgrey;\n"
"border-top-right-radius: 7px;\n"
"border-bottom-right-radius: 7px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QSlider::sub-page:qlineargradient {\n"
"background: rgb(85, 90, 104);\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-left-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}")
        self.Audio_Slider.setTracking(True)
        self.Audio_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Audio_Slider.setInvertedAppearance(False)
        self.Audio_Slider.setInvertedControls(False)
        self.Audio_Slider.setObjectName("Audio_Slider")
        self.btn_Play = QtWidgets.QPushButton(self.Pages_Player)
        self.btn_Play.setGeometry(QtCore.QRect(530, 20, 40, 31))
        self.btn_Play.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Icons/assets/play_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap(":/Icons/assets/play_disable.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap(":/Icons/assets/play_disable.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.btn_Play.setIcon(icon12)
        self.btn_Play.setIconSize(QtCore.QSize(32, 32))
        self.btn_Play.setFlat(True)
        self.btn_Play.setObjectName("btn_Play")
        self.btn_Next = QtWidgets.QPushButton(self.Pages_Player)
        self.btn_Next.setGeometry(QtCore.QRect(630, 20, 40, 31))
        self.btn_Next.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Icons/assets/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon13.addPixmap(QtGui.QPixmap(":/Icons/assets/next_disable.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.btn_Next.setIcon(icon13)
        self.btn_Next.setIconSize(QtCore.QSize(32, 32))
        self.btn_Next.setFlat(True)
        self.btn_Next.setObjectName("btn_Next")
        self.btn_Pre = QtWidgets.QPushButton(self.Pages_Player)
        self.btn_Pre.setGeometry(QtCore.QRect(430, 20, 40, 31))
        self.btn_Pre.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Icons/assets/pre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon14.addPixmap(QtGui.QPixmap(":/Icons/assets/pre_disable.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.btn_Pre.setIcon(icon14)
        self.btn_Pre.setIconSize(QtCore.QSize(32, 32))
        self.btn_Pre.setFlat(True)
        self.btn_Pre.setObjectName("btn_Pre")
        self.btn_delete_track = QtWidgets.QPushButton(self.Pages_Player)
        self.btn_delete_track.setGeometry(QtCore.QRect(20, 10, 32, 32))
        self.btn_delete_track.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/Icons/assets/close_widget.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete_track.setIcon(icon15)
        self.btn_delete_track.setIconSize(QtCore.QSize(32, 32))
        self.btn_delete_track.setFlat(True)
        self.btn_delete_track.setObjectName("btn_delete_track")
        self.stackedWidget.addWidget(self.page_3)
        self.Background.raise_()
        self.User.raise_()
        self.Menu.raise_()
        self.Titlebar.raise_()
        self.stackedWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setEnabled(True)
        self.statusBar.setStyleSheet("background-color: rgb(35, 39, 51);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"font: 500 16pt \"Segoe UI\";")
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_File_Browser.setStatusTip(_translate("MainWindow", "File_Browser"))
        self.btn_Option.setStatusTip(_translate("MainWindow", "Option"))
        self.btn_ChatnPlayer.setStatusTip(_translate("MainWindow", "Chat&Player"))
        self.name_Titlebar.setText(_translate("MainWindow", "Sentiment analysis-based music generator"))
        self.btn_Exit.setStatusTip(_translate("MainWindow", "Exit (Shift+Esc)"))
        self.btn_Min.setStatusTip(_translate("MainWindow", "Minimize"))
        self.Title_Channel.setText(_translate("MainWindow", "File Browser"))
        self.btn_import_file.setStatusTip(_translate("MainWindow", "Open_File"))
        self.scrollArea.setStatusTip(_translate("MainWindow", "Browser"))
        self.btn_refresh.setStatusTip(_translate("MainWindow", "Refresh_File"))
        self.btn_train.setStatusTip(_translate("MainWindow", "Train_Model"))
        self.btn_train.setText(_translate("MainWindow", "Train Model"))
        self.btn_clear.setStatusTip(_translate("MainWindow", "Clear_File"))
        self.rbtn_pos.setStatusTip(_translate("MainWindow", "Emotion_Positive"))
        self.rbtn_pos.setText(_translate("MainWindow", "Positive"))
        self.rbtn_neu.setStatusTip(_translate("MainWindow", "Emotion_Neutral"))
        self.rbtn_neu.setText(_translate("MainWindow", "Neutral"))
        self.rbtn_neg.setStatusTip(_translate("MainWindow", "Emotion_Negative"))
        self.rbtn_neg.setText(_translate("MainWindow", "Negative"))
        self.label_count.setText(_translate("MainWindow", "Files amount"))
        self.label_training.setText(_translate("MainWindow", "Model Training..."))
        self.PageTitle_Option.setText(_translate("MainWindow", "Option"))
        self.btn_Confirm_Option.setStatusTip(_translate("MainWindow", "Option_Comfirm"))
        self.btn_Confirm_Option.setText(_translate("MainWindow", "Confirm"))
        self.label_data.setText(_translate("MainWindow", "Set data range"))
        self.label_bpm.setText(_translate("MainWindow", "BPM"))
        self.edit_datarange.setStatusTip(_translate("MainWindow", "Data_Range"))
        self.edit_datarange.setPlaceholderText(_translate("MainWindow", "Enter range (50~100)"))
        self.edit_BPM.setStatusTip(_translate("MainWindow", "BPM"))
        self.edit_BPM.setPlaceholderText(_translate("MainWindow", "Enter BPM (1~300)"))
        self.label_instrument.setText(_translate("MainWindow", "MIDI Instrument"))
        self.btn_midi_piano.setStatusTip(_translate("MainWindow", "MIDI_Piano"))
        self.btn_midi_saxphone.setStatusTip(_translate("MainWindow", "MIDI_Saxphone"))
        self.btn_midi_trumpet.setStatusTip(_translate("MainWindow", "MIDI_Trumpet"))
        self.btn_midi_guitar.setStatusTip(_translate("MainWindow", "MIDI_Guitar"))
        self.edit_ChannelID.setStatusTip(_translate("MainWindow", "Channel_ID"))
        self.edit_ChannelID.setPlaceholderText(_translate("MainWindow", "Enter Channel ID..."))
        self.Twitch_icon_Option.setStatusTip(_translate("MainWindow", "Streamer_Icon"))
        self.label_instrument_2.setText(_translate("MainWindow", "Channel ID"))
        self.PageTitle_Chat.setText(_translate("MainWindow", "Chat"))
        self.tEdit_Chatlog.setStatusTip(_translate("MainWindow", "Chat_Log"))
        self.tEdit_Chatlog.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:16pt; font-weight:144; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_chat.setStatusTip(_translate("MainWindow", "Capture_Chat"))
        self.btn_chat.setText(_translate("MainWindow", "Capture Chat"))
        self.PageTitle_Playlist.setText(_translate("MainWindow", "Player"))
        self.btn_Play.setStatusTip(_translate("MainWindow", "Play"))
        self.btn_Next.setStatusTip(_translate("MainWindow", "Next"))
        self.btn_Pre.setStatusTip(_translate("MainWindow", "Previous"))
        self.btn_delete_track.setStatusTip(_translate("MainWindow", "Delete_track"))

import asset_rc
