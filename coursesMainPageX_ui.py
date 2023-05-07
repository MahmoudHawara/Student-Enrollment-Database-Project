# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coursesMainPageX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 880)
        MainWindow.setMinimumSize(QSize(880, 880))
        MainWindow.setStyleSheet(u"background: #16213E;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setStyleSheet(u"background: #0F3460")
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.ControlButtons_2 = QFrame(self.header)
        self.ControlButtons_2.setObjectName(u"ControlButtons_2")
        self.horizontalLayout_6 = QHBoxLayout(self.ControlButtons_2)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.close_2 = QPushButton(self.ControlButtons_2)
        self.close_2.setObjectName(u"close_2")
        self.close_2.setMinimumSize(QSize(20, 26))
        self.close_2.setMaximumSize(QSize(26, 26))
        self.close_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_2.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: #E94560;\n"
"	border-radius: 12px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Controles/Images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_2.setIcon(icon)
        self.close_2.setIconSize(QSize(12, 14))
        self.close_2.setFlat(True)

        self.horizontalLayout_6.addWidget(self.close_2)

        self.expand_2 = QPushButton(self.ControlButtons_2)
        self.expand_2.setObjectName(u"expand_2")
        self.expand_2.setMinimumSize(QSize(26, 26))
        self.expand_2.setMaximumSize(QSize(26, 26))
        self.expand_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.expand_2.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: #E94560;\n"
"	border-radius: 12px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Controles/Images/expand-arrows.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_2.setIcon(icon1)
        self.expand_2.setIconSize(QSize(20, 25))
        self.expand_2.setFlat(True)

        self.horizontalLayout_6.addWidget(self.expand_2)

        self.minimize_2 = QPushButton(self.ControlButtons_2)
        self.minimize_2.setObjectName(u"minimize_2")
        self.minimize_2.setMinimumSize(QSize(26, 26))
        self.minimize_2.setMaximumSize(QSize(26, 26))
        self.minimize_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_2.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: #E94560;\n"
"	border-radius: 12px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Controles/Images/minimize-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_2.setIcon(icon2)
        self.minimize_2.setIconSize(QSize(13, 16))
        self.minimize_2.setFlat(True)

        self.horizontalLayout_6.addWidget(self.minimize_2)

        self.expand_3 = QPushButton(self.ControlButtons_2)
        self.expand_3.setObjectName(u"expand_3")
        self.expand_3.setMinimumSize(QSize(26, 26))
        self.expand_3.setMaximumSize(QSize(26, 26))
        self.expand_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.expand_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.expand_3.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: #E94560;\n"
"	border-radius: 12px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Controles/Images/return.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_3.setIcon(icon3)
        self.expand_3.setIconSize(QSize(20, 25))
        self.expand_3.setFlat(True)

        self.horizontalLayout_6.addWidget(self.expand_3)


        self.horizontalLayout_4.addWidget(self.ControlButtons_2, 0, Qt.AlignLeft)

        self.Logo_2 = QFrame(self.header)
        self.Logo_2.setObjectName(u"Logo_2")
        self.Logo_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_7 = QHBoxLayout(self.Logo_2)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Learn_2 = QLabel(self.Logo_2)
        self.Learn_2.setObjectName(u"Learn_2")
        font = QFont()
        font.setFamily(u"Tw Cen MT Condensed Extra Bold")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Learn_2.setFont(font)
        self.Learn_2.setStyleSheet(u"color: white")
        self.Learn_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Learn_2.setWordWrap(False)

        self.horizontalLayout_7.addWidget(self.Learn_2)

        self.Loop_2 = QLabel(self.Logo_2)
        self.Loop_2.setObjectName(u"Loop_2")
        self.Loop_2.setFont(font)
        self.Loop_2.setStyleSheet(u"color: #E94560")

        self.horizontalLayout_7.addWidget(self.Loop_2)


        self.horizontalLayout_4.addWidget(self.Logo_2)

        self.ProfilePhotoAndSettings_2 = QFrame(self.header)
        self.ProfilePhotoAndSettings_2.setObjectName(u"ProfilePhotoAndSettings_2")
        self.ProfilePhotoAndSettings_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.ProfilePhotoAndSettings_2)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.settings_2 = QPushButton(self.ProfilePhotoAndSettings_2)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setMinimumSize(QSize(45, 50))
        self.settings_2.setMaximumSize(QSize(45, 50))
        self.settings_2.setBaseSize(QSize(0, 0))
        self.settings_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_2.setStyleSheet(u"background-color: #E94560;\n"
"border-style: outset")
        icon4 = QIcon()
        icon4.addFile(u":/Controles/Images/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_2.setIcon(icon4)
        self.settings_2.setIconSize(QSize(30, 30))
        self.settings_2.setCheckable(False)
        self.settings_2.setAutoRepeat(False)
        self.settings_2.setAutoExclusive(False)
        self.settings_2.setAutoDefault(False)
        self.settings_2.setFlat(True)

        self.horizontalLayout_8.addWidget(self.settings_2)

        self.profilePhoto_2 = QPushButton(self.ProfilePhotoAndSettings_2)
        self.profilePhoto_2.setObjectName(u"profilePhoto_2")
        self.profilePhoto_2.setMinimumSize(QSize(35, 35))
        self.profilePhoto_2.setMaximumSize(QSize(35, 35))
        self.profilePhoto_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.profilePhoto_2.setAutoFillBackground(False)
        self.profilePhoto_2.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/Controles/Images/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profilePhoto_2.setIcon(icon5)
        self.profilePhoto_2.setIconSize(QSize(35, 35))
        self.profilePhoto_2.setAutoDefault(False)
        self.profilePhoto_2.setFlat(True)

        self.horizontalLayout_8.addWidget(self.profilePhoto_2)


        self.horizontalLayout_4.addWidget(self.ProfilePhotoAndSettings_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.mainPage = QFrame(self.centralwidget)
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setMaximumSize(QSize(16777215, 16777215))
        self.mainPage.setStyleSheet(u"border: none;")
        self.mainPage.setFrameShape(QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 40, 0, 0)
        self.frame_11 = QFrame(self.mainPage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 150))
        self.frame_11.setMaximumSize(QSize(16777215, 150))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(65, 125))
        self.frame_12.setMaximumSize(QSize(65, 100))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.line_7 = QFrame(self.frame_12)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(0, 60, 3, 60))
        self.line_7.setMinimumSize(QSize(0, 60))
        self.line_7.setMaximumSize(QSize(16777215, 60))
        self.line_7.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.frame_12)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(0, 120, 60, 3))
        self.line_8.setMinimumSize(QSize(60, 0))
        self.line_8.setMaximumSize(QSize(60, 16777215))
        self.line_8.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.frame_12)

        self.department = QFrame(self.frame_11)
        self.department.setObjectName(u"department")
        self.department.setMinimumSize(QSize(0, 100))
        self.department.setMaximumSize(QSize(750, 100))
        self.department.setStyleSheet(u"color: white;")
        self.department.setFrameShape(QFrame.StyledPanel)
        self.department.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.department)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.department)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Condensed")
        font1.setPointSize(25)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_11.setFont(font1)
        self.label_11.setLineWidth(5)

        self.horizontalLayout_19.addWidget(self.label_11, 0, Qt.AlignRight|Qt.AlignBottom)

        self.label_12 = QLabel(self.frame_17)
        self.label_12.setObjectName(u"label_12")
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Condensed")
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_12.setFont(font2)
        self.label_12.setFrameShadow(QFrame.Plain)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setIndent(-1)

        self.horizontalLayout_19.addWidget(self.label_12, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_9.addWidget(self.frame_17)

        self.label_14 = QLabel(self.department)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Condensed")
        font3.setPointSize(22)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_14.setFont(font3)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.department, 0, Qt.AlignHCenter)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(65, 125))
        self.frame_14.setMaximumSize(QSize(65, 125))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.line_3 = QFrame(self.frame_14)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(60, 0, 3, 60))
        self.line_3.setMinimumSize(QSize(0, 60))
        self.line_3.setMaximumSize(QSize(16777215, 60))
        self.line_3.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.frame_14)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 0, 60, 3))
        self.line_4.setMinimumSize(QSize(60, 0))
        self.line_4.setMaximumSize(QSize(60, 16777215))
        self.line_4.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.frame_14)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.searchAndAdd = QFrame(self.mainPage)
        self.searchAndAdd.setObjectName(u"searchAndAdd")
        self.searchAndAdd.setMinimumSize(QSize(620, 0))
        self.searchAndAdd.setMaximumSize(QSize(620, 16777215))
        self.searchAndAdd.setStyleSheet(u"")
        self.searchAndAdd.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.searchAndAdd.setFrameShape(QFrame.StyledPanel)
        self.searchAndAdd.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.searchAndAdd)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.searchAndAdd)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(620, 50))
        self.frame.setMaximumSize(QSize(300, 50))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Bahnschrift Condensed")
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setWeight(50)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: white;\n"
"\n"
"letter-spacing: 1px;")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(75, 35))
        self.pushButton.setMaximumSize(QSize(75, 35))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift Condensed")
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setWeight(50)
        self.pushButton.setFont(font5)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: #E94560;\n"
"border-style: outset;\n"
"border-radius: 3px;\n"
"color: white;\n"
"letter-spacing: 1px;")
        icon6 = QIcon()
        icon6.addFile(u":/Controles/Images/plus2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(19, 19))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_2 = QFrame(self.searchAndAdd)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(243, 50))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift Light SemiCondensed")
        font6.setPointSize(16)
        self.lineEdit_6.setFont(font6)
        self.lineEdit_6.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:#A9A9A9;\n"
"border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"padding-left: 5px;\n"
"letter-spacing: 1.5px;\n"
"margin-top: 10px;\n"
"")
        self.lineEdit_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_6)


        self.verticalLayout_8.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.searchAndAdd, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.mainPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(820, 180))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #0F3460;\n"
"    width: 7px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #E94560, stop:1 #0F3460);\n"
"    border-radius: 10px;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background-color: #333333;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: #333333;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 813, 390))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.frame_31 = QFrame(self.scrollAreaWidgetContents)
#         self.frame_31.setObjectName(u"frame_31")
#         self.frame_31.setMinimumSize(QSize(240, 180))
#         self.frame_31.setMaximumSize(QSize(240, 180))
#         self.frame_31.setStyleSheet(u"background: #0F3460;\n"
# "color: white;\n"
# "border-radius: 5px;\n"
# "letter-spacing: 2px;")
#         self.frame_31.setFrameShape(QFrame.StyledPanel)
#         self.frame_31.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_14 = QVBoxLayout(self.frame_31)
#         self.verticalLayout_14.setSpacing(5)
#         self.verticalLayout_14.setObjectName(u"verticalLayout_14")
#         self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
#         self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

#         self.verticalLayout_14.addItem(self.verticalSpacer_23)

#         self.frame_32 = QFrame(self.frame_31)
#         self.frame_32.setObjectName(u"frame_32")
#         self.frame_32.setMinimumSize(QSize(0, 30))
#         self.frame_32.setMaximumSize(QSize(16777215, 30))
#         self.frame_32.setFrameShape(QFrame.StyledPanel)
#         self.frame_32.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_27 = QHBoxLayout(self.frame_32)
#         self.horizontalLayout_27.setSpacing(2)
#         self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
#         self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
#         self.label_26 = QLabel(self.frame_32)
#         self.label_26.setObjectName(u"label_26")
#         self.label_26.setMinimumSize(QSize(0, 30))
#         self.label_26.setMaximumSize(QSize(16777215, 30))
#         self.label_26.setFont(font2)
#         self.label_26.setLineWidth(5)

#         self.horizontalLayout_27.addWidget(self.label_26, 0, Qt.AlignRight|Qt.AlignBottom)


#         self.verticalLayout_14.addWidget(self.frame_32, 0, Qt.AlignHCenter)

#         self.frame_33 = QFrame(self.frame_31)
#         self.frame_33.setObjectName(u"frame_33")
#         self.frame_33.setFrameShape(QFrame.StyledPanel)
#         self.frame_33.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_21 = QHBoxLayout(self.frame_33)
#         self.horizontalLayout_21.setSpacing(2)
#         self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
#         self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)

#         self.verticalLayout_14.addWidget(self.frame_33, 0, Qt.AlignHCenter|Qt.AlignBottom)

#         self.label_27 = QLabel(self.frame_31)
#         self.label_27.setObjectName(u"label_27")
#         self.label_27.setMaximumSize(QSize(16777215, 35))
#         self.label_27.setFont(font2)
#         self.label_27.setStyleSheet(u"")

#         self.verticalLayout_14.addWidget(self.label_27, 0, Qt.AlignHCenter)

#         self.label_40 = QLabel(self.frame_31)
#         self.label_40.setObjectName(u"label_40")
#         self.label_40.setMaximumSize(QSize(16777215, 35))
#         self.label_40.setFont(font2)
#         self.label_40.setStyleSheet(u"")

#         self.verticalLayout_14.addWidget(self.label_40, 0, Qt.AlignHCenter)

#         self.frame_34 = QFrame(self.frame_31)
#         self.frame_34.setObjectName(u"frame_34")
#         self.frame_34.setMinimumSize(QSize(0, 33))
#         self.frame_34.setMaximumSize(QSize(16777215, 33))
#         self.frame_34.setStyleSheet(u"")
#         self.frame_34.setFrameShape(QFrame.StyledPanel)
#         self.frame_34.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_28 = QHBoxLayout(self.frame_34)
#         self.horizontalLayout_28.setSpacing(20)
#         self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
#         self.horizontalLayout_28.setContentsMargins(0, 5, 0, 0)
#         self.pushButton_14 = QPushButton(self.frame_34)
#         self.pushButton_14.setObjectName(u"pushButton_14")
#         self.pushButton_14.setMinimumSize(QSize(75, 28))
#         self.pushButton_14.setMaximumSize(QSize(75, 28))
#         self.pushButton_14.setSizeIncrement(QSize(0, 0))
        font7 = QFont()
        font7.setFamily(u"Bahnschrift Condensed")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setWeight(50)
#         self.pushButton_14.setFont(font7)
#         self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
#         self.pushButton_14.setStyleSheet(u"background: #E94560;\n"
# "border-radius: 3px;\n"
# "")

#         self.horizontalLayout_28.addWidget(self.pushButton_14)


#         self.verticalLayout_14.addWidget(self.frame_34, 0, Qt.AlignHCenter|Qt.AlignVCenter)

#         self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

#         self.verticalLayout_14.addItem(self.verticalSpacer_24)


        # self.verticalLayout_3.addWidget(self.frame_31)

#         self.frame_59 = QFrame(self.scrollAreaWidgetContents)
#         self.frame_59.setObjectName(u"frame_59")
#         self.frame_59.setMinimumSize(QSize(240, 180))
#         self.frame_59.setMaximumSize(QSize(240, 180))
#         self.frame_59.setStyleSheet(u"background: #0F3460;\n"
# "color: white;\n"
# "border-radius: 5px;\n"
# "letter-spacing: 2px;")
#         self.frame_59.setFrameShape(QFrame.StyledPanel)
#         self.frame_59.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_21 = QVBoxLayout(self.frame_59)
#         self.verticalLayout_21.setSpacing(5)
#         self.verticalLayout_21.setObjectName(u"verticalLayout_21")
#         self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
#         self.verticalSpacer_37 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

#         self.verticalLayout_21.addItem(self.verticalSpacer_37)

#         self.frame_60 = QFrame(self.frame_59)
#         self.frame_60.setObjectName(u"frame_60")
#         self.frame_60.setMinimumSize(QSize(0, 30))
#         self.frame_60.setMaximumSize(QSize(16777215, 30))
#         self.frame_60.setFrameShape(QFrame.StyledPanel)
#         self.frame_60.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_46 = QHBoxLayout(self.frame_60)
#         self.horizontalLayout_46.setSpacing(2)
#         self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
#         self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
#         self.label_41 = QLabel(self.frame_60)
#         self.label_41.setObjectName(u"label_41")
#         self.label_41.setMinimumSize(QSize(0, 30))
#         self.label_41.setMaximumSize(QSize(16777215, 30))
#         self.label_41.setFont(font2)
#         self.label_41.setLineWidth(5)

#         self.horizontalLayout_46.addWidget(self.label_41, 0, Qt.AlignRight|Qt.AlignBottom)


#         self.verticalLayout_21.addWidget(self.frame_60, 0, Qt.AlignHCenter)

#         self.frame_61 = QFrame(self.frame_59)
#         self.frame_61.setObjectName(u"frame_61")
#         self.frame_61.setFrameShape(QFrame.StyledPanel)
#         self.frame_61.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_23 = QHBoxLayout(self.frame_61)
#         self.horizontalLayout_23.setSpacing(2)
#         self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
#         self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)

#         self.verticalLayout_21.addWidget(self.frame_61, 0, Qt.AlignHCenter|Qt.AlignBottom)

#         self.label_42 = QLabel(self.frame_59)
#         self.label_42.setObjectName(u"label_42")
#         self.label_42.setMaximumSize(QSize(16777215, 35))
#         self.label_42.setFont(font2)
#         self.label_42.setStyleSheet(u"")

#         self.verticalLayout_21.addWidget(self.label_42, 0, Qt.AlignHCenter)

#         self.label_43 = QLabel(self.frame_59)
#         self.label_43.setObjectName(u"label_43")
#         self.label_43.setMaximumSize(QSize(16777215, 35))
#         self.label_43.setFont(font2)
#         self.label_43.setStyleSheet(u"")

#         self.verticalLayout_21.addWidget(self.label_43, 0, Qt.AlignHCenter)

#         self.frame_62 = QFrame(self.frame_59)
#         self.frame_62.setObjectName(u"frame_62")
#         self.frame_62.setMinimumSize(QSize(0, 33))
#         self.frame_62.setMaximumSize(QSize(16777215, 33))
#         self.frame_62.setStyleSheet(u"")
#         self.frame_62.setFrameShape(QFrame.StyledPanel)
#         self.frame_62.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_47 = QHBoxLayout(self.frame_62)
#         self.horizontalLayout_47.setSpacing(20)
#         self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
#         self.horizontalLayout_47.setContentsMargins(0, 5, 0, 0)
#         self.pushButton_21 = QPushButton(self.frame_62)
#         self.pushButton_21.setObjectName(u"pushButton_21")
#         self.pushButton_21.setMinimumSize(QSize(75, 28))
#         self.pushButton_21.setMaximumSize(QSize(75, 28))
#         self.pushButton_21.setSizeIncrement(QSize(0, 0))
#         self.pushButton_21.setFont(font7)
#         self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
#         self.pushButton_21.setStyleSheet(u"background: #E94560;\n"
# "border-radius: 3px;\n"
# "")

#         self.horizontalLayout_47.addWidget(self.pushButton_21)


#         self.verticalLayout_21.addWidget(self.frame_62, 0, Qt.AlignHCenter|Qt.AlignVCenter)

#         self.verticalSpacer_38 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

#         self.verticalLayout_21.addItem(self.verticalSpacer_38)


#         self.verticalLayout_3.addWidget(self.frame_59)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.mainPage)

        self.size_grip = QFrame(self.centralwidget)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(0, 15))
        self.size_grip.setMaximumSize(QSize(16777215, 15))
        self.size_grip.setStyleSheet(u"border: none;")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.size_grip)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.settings_2.setDefault(False)
        self.profilePhoto_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.close_2.setText("")
#if QT_CONFIG(shortcut)
        self.close_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F4", None))
#endif // QT_CONFIG(shortcut)
        self.expand_2.setText("")
#if QT_CONFIG(shortcut)
        self.expand_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.minimize_2.setText("")
#if QT_CONFIG(shortcut)
        self.minimize_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.expand_3.setText("")
#if QT_CONFIG(shortcut)
        self.expand_3.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.Learn_2.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
        self.Loop_2.setText(QCoreApplication.translate("MainWindow", u"Loop", None))
#if QT_CONFIG(statustip)
        self.settings_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.settings_2.setText("")
        self.profilePhoto_2.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"st", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Computer and Communication", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Courses", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" NEW", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search.....", None))
        # self.label_26.setText(QCoreApplication.translate("MainWindow", u"ECE 115", None))
        # self.label_27.setText(QCoreApplication.translate("MainWindow", u"20 Hours", None))
        # self.label_40.setText(QCoreApplication.translate("MainWindow", u"First Term", None))
        # self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        # self.label_41.setText(QCoreApplication.translate("MainWindow", u"ECE 115", None))
        # self.label_42.setText(QCoreApplication.translate("MainWindow", u"20 Hours", None))
        # self.label_43.setText(QCoreApplication.translate("MainWindow", u"First Term", None))
        # self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
    # retranslateUi

