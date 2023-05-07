# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminMainPage.ui'
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
        MainWindow.resize(920, 880)
        MainWindow.setMinimumSize(QSize(920, 880))
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
        self.close = QPushButton(self.ControlButtons_2)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(20, 26))
        self.close.setMaximumSize(QSize(26, 26))
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: #E94560;\n"
"	border-radius: 12px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Controles/Images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon)
        self.close.setIconSize(QSize(12, 14))
        self.close.setFlat(True)

        self.horizontalLayout_6.addWidget(self.close)

        self.expand = QPushButton(self.ControlButtons_2)
        self.expand.setObjectName(u"expand")
        self.expand.setMinimumSize(QSize(26, 26))
        self.expand.setMaximumSize(QSize(26, 26))
        self.expand.setCursor(QCursor(Qt.PointingHandCursor))
        self.expand.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: #E94560;\n"
"	border-radius: 12px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Controles/Images/expand-arrows.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand.setIcon(icon1)
        self.expand.setIconSize(QSize(20, 25))
        self.expand.setFlat(True)

        self.horizontalLayout_6.addWidget(self.expand)

        self.minimize = QPushButton(self.ControlButtons_2)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(26, 26))
        self.minimize.setMaximumSize(QSize(26, 26))
        self.minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: #E94560;\n"
"	border-radius: 12px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Controles/Images/minimize-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon2)
        self.minimize.setIconSize(QSize(13, 16))
        self.minimize.setFlat(True)

        self.horizontalLayout_6.addWidget(self.minimize)


        self.horizontalLayout_4.addWidget(self.ControlButtons_2, 0, Qt.AlignLeft)

        self.Logo_2 = QFrame(self.header)
        self.Logo_2.setObjectName(u"Logo_2")
        self.Logo_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_7 = QHBoxLayout(self.Logo_2)
        self.horizontalLayout_7.setSpacing(8)
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
        self.settings_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_2.setStyleSheet(u"background-color: #E94560;\n"
"border-style: outset")
        icon3 = QIcon()
        icon3.addFile(u":/Controles/Images/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_2.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u":/Controles/Images/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profilePhoto_2.setIcon(icon4)
        self.profilePhoto_2.setIconSize(QSize(35, 35))
        self.profilePhoto_2.setAutoDefault(False)
        self.profilePhoto_2.setFlat(True)

        self.horizontalLayout_8.addWidget(self.profilePhoto_2)


        self.horizontalLayout_4.addWidget(self.ProfilePhotoAndSettings_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.mainPage = QFrame(self.centralwidget)
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setMaximumSize(QSize(16777215, 16777215))
        self.mainPage.setCursor(QCursor(Qt.ArrowCursor))
        self.mainPage.setStyleSheet(u"border: none;")
        self.mainPage.setFrameShape(QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 40, 0, 0)
        self.buttons = QFrame(self.mainPage)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(0, 130))
        self.buttons.setMaximumSize(QSize(16777215, 130))
        self.buttons.setStyleSheet(u"")
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.groups = QFrame(self.buttons)
        self.groups.setObjectName(u"groups")
        self.groups.setMinimumSize(QSize(180, 110))
        self.groups.setMaximumSize(QSize(180, 110))
        font1 = QFont()
        font1.setFamily(u"MS Serif")
        self.groups.setFont(font1)
        self.groups.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 0.5px;")
        self.groups.setFrameShape(QFrame.StyledPanel)
        self.groups.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.groups)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.numOfGroups = QLabel(self.groups)
        self.numOfGroups.setObjectName(u"numOfGroups")
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Condensed")
        font2.setPointSize(22)
        font2.setBold(False)
        font2.setWeight(50)
        self.numOfGroups.setFont(font2)

        self.verticalLayout_3.addWidget(self.numOfGroups, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.groups)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 40))
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.groups)

        self.groups_2 = QFrame(self.buttons)
        self.groups_2.setObjectName(u"groups_2")
        self.groups_2.setMinimumSize(QSize(180, 110))
        self.groups_2.setMaximumSize(QSize(180, 110))
        self.groups_2.setFont(font1)
        self.groups_2.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 0.5px;")
        self.groups_2.setFrameShape(QFrame.StyledPanel)
        self.groups_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.groups_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.numOfGroups_2 = QLabel(self.groups_2)
        self.numOfGroups_2.setObjectName(u"numOfGroups_2")
        self.numOfGroups_2.setFont(font2)

        self.verticalLayout_4.addWidget(self.numOfGroups_2, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.groups_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 40))
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)


        self.horizontalLayout.addWidget(self.groups_2)

        self.groups_3 = QFrame(self.buttons)
        self.groups_3.setObjectName(u"groups_3")
        self.groups_3.setMinimumSize(QSize(180, 110))
        self.groups_3.setMaximumSize(QSize(180, 110))
        self.groups_3.setFont(font1)
        self.groups_3.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 0.5px;")
        self.groups_3.setFrameShape(QFrame.StyledPanel)
        self.groups_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.groups_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)

        self.numOfGroups_3 = QLabel(self.groups_3)
        self.numOfGroups_3.setObjectName(u"numOfGroups_3")
        self.numOfGroups_3.setFont(font2)

        self.verticalLayout_7.addWidget(self.numOfGroups_3, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.groups_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 40))
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_12)


        self.horizontalLayout.addWidget(self.groups_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.buttons)

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
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Condensed")
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setWeight(50)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: white;\n"
"\n"
"letter-spacing: 1px;")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(75, 35))
        self.pushButton.setMaximumSize(QSize(75, 35))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift Condensed")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setWeight(50)
        self.pushButton.setFont(font4)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: #E94560;\n"
"border-style: outset;\n"
"border-radius: 3px;\n"
"color: white;\n"
"letter-spacing: 1px;")
        icon5 = QIcon()
        icon5.addFile(u":/Controles/Images/plus2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
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
        font5 = QFont()
        font5.setFamily(u"Bahnschrift Light SemiCondensed")
        font5.setPointSize(16)
        self.lineEdit_6.setFont(font5)
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
        self.scrollArea.setMinimumSize(QSize(820, 150))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 813, 330))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
#         self.frame_23 = QFrame(self.scrollAreaWidgetContents)
#         self.frame_23.setObjectName(u"frame_23")
#         self.frame_23.setMinimumSize(QSize(240, 150))
#         self.frame_23.setMaximumSize(QSize(240, 150))
#         self.frame_23.setStyleSheet(u"background: #0F3460;\n"
# "color: white;\n"
# "border-radius: 5px;\n"
# "letter-spacing: 2px;")
#         self.frame_23.setFrameShape(QFrame.StyledPanel)
#         self.frame_23.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_12 = QVBoxLayout(self.frame_23)
#         self.verticalLayout_12.setSpacing(5)
#         self.verticalLayout_12.setObjectName(u"verticalLayout_12")
#         self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
#         self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

#         self.verticalLayout_12.addItem(self.verticalSpacer_19)

#         self.frame_24 = QFrame(self.frame_23)
#         self.frame_24.setObjectName(u"frame_24")
#         self.frame_24.setMinimumSize(QSize(0, 30))
#         self.frame_24.setMaximumSize(QSize(16777215, 30))
#         self.frame_24.setFrameShape(QFrame.StyledPanel)
#         self.frame_24.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_23 = QHBoxLayout(self.frame_24)
#         self.horizontalLayout_23.setSpacing(2)
#         self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
#         self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
#         self.label_22 = QLabel(self.frame_24)
#         self.label_22.setObjectName(u"label_22")
#         self.label_22.setMinimumSize(QSize(0, 30))
#         self.label_22.setMaximumSize(QSize(16777215, 30))
#         self.label_22.setFont(font2)
#         self.label_22.setLineWidth(5)

#         self.horizontalLayout_23.addWidget(self.label_22, 0, Qt.AlignRight|Qt.AlignBottom)

#         self.label_23 = QLabel(self.frame_24)
#         self.label_23.setObjectName(u"label_23")
#         self.label_23.setMinimumSize(QSize(0, 20))
#         self.label_23.setMaximumSize(QSize(16777215, 20))
#         self.label_23.setFont(font4)
#         self.label_23.setFrameShadow(QFrame.Plain)
#         self.label_23.setAlignment(Qt.AlignCenter)
#         self.label_23.setIndent(-1)

#         self.horizontalLayout_23.addWidget(self.label_23, 0, Qt.AlignLeft|Qt.AlignBottom)


#         self.verticalLayout_12.addWidget(self.frame_24, 0, Qt.AlignHCenter)

#         self.frame_25 = QFrame(self.frame_23)
#         self.frame_25.setObjectName(u"frame_25")
#         self.frame_25.setFrameShape(QFrame.StyledPanel)
#         self.frame_25.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_18 = QHBoxLayout(self.frame_25)
#         self.horizontalLayout_18.setSpacing(2)
#         self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
#         self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)

#         self.verticalLayout_12.addWidget(self.frame_25, 0, Qt.AlignHCenter|Qt.AlignBottom)

#         self.label_24 = QLabel(self.frame_23)
#         self.label_24.setObjectName(u"label_24")
#         self.label_24.setMaximumSize(QSize(16777215, 35))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift Condensed")
        font6.setPointSize(18)
        font6.setBold(False)
        font6.setWeight(50)
#         self.label_24.setFont(font6)
#         self.label_24.setStyleSheet(u"")

#         self.verticalLayout_12.addWidget(self.label_24, 0, Qt.AlignHCenter)

#         self.frame_26 = QFrame(self.frame_23)
#         self.frame_26.setObjectName(u"frame_26")
#         self.frame_26.setMinimumSize(QSize(0, 33))
#         self.frame_26.setMaximumSize(QSize(16777215, 33))
#         self.frame_26.setStyleSheet(u"")
#         self.frame_26.setFrameShape(QFrame.StyledPanel)
#         self.frame_26.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_24 = QHBoxLayout(self.frame_26)
#         self.horizontalLayout_24.setSpacing(20)
#         self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
#         self.horizontalLayout_24.setContentsMargins(0, 5, 0, 0)
#         self.pushButton_12 = QPushButton(self.frame_26)
#         self.pushButton_12.setObjectName(u"pushButton_12")
#         self.pushButton_12.setMinimumSize(QSize(75, 28))
#         self.pushButton_12.setMaximumSize(QSize(75, 28))
#         self.pushButton_12.setSizeIncrement(QSize(0, 0))
        font7 = QFont()
        font7.setFamily(u"Bahnschrift Condensed")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setWeight(50)
#         self.pushButton_12.setFont(font7)
#         self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
#         self.pushButton_12.setStyleSheet(u"background: #E94560;\n"
# "border-radius: 3px;\n"
# "")

#         self.horizontalLayout_24.addWidget(self.pushButton_12)

#         self.pushButton_13 = QPushButton(self.frame_26)
#         self.pushButton_13.setObjectName(u"pushButton_13")
#         self.pushButton_13.setMinimumSize(QSize(75, 28))
#         self.pushButton_13.setMaximumSize(QSize(75, 28))
#         self.pushButton_13.setSizeIncrement(QSize(0, 0))
#         self.pushButton_13.setFont(font7)
#         self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
#         self.pushButton_13.setStyleSheet(u"background: #E94560;\n"
# "border-radius: 3px;\n"
# "")

#         self.horizontalLayout_24.addWidget(self.pushButton_13)


#         self.verticalLayout_12.addWidget(self.frame_26, 0, Qt.AlignHCenter|Qt.AlignVCenter)

#         self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

#         self.verticalLayout_12.addItem(self.verticalSpacer_20)


        # self.verticalLayout_5.addWidget(self.frame_23)

#         self.frame_27 = QFrame(self.scrollAreaWidgetContents)
#         self.frame_27.setObjectName(u"frame_27")
#         self.frame_27.setMinimumSize(QSize(240, 150))
#         self.frame_27.setMaximumSize(QSize(240, 150))
#         self.frame_27.setStyleSheet(u"background: #0F3460;\n"
# "color: white;\n"
# "border-radius: 5px;\n"
# "letter-spacing: 2px;")
#         self.frame_27.setFrameShape(QFrame.StyledPanel)
#         self.frame_27.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_13 = QVBoxLayout(self.frame_27)
#         self.verticalLayout_13.setSpacing(5)
#         self.verticalLayout_13.setObjectName(u"verticalLayout_13")
#         self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
#         self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

#         self.verticalLayout_13.addItem(self.verticalSpacer_21)

#         self.frame_28 = QFrame(self.frame_27)
#         self.frame_28.setObjectName(u"frame_28")
#         self.frame_28.setMinimumSize(QSize(0, 30))
#         self.frame_28.setMaximumSize(QSize(16777215, 30))
#         self.frame_28.setFrameShape(QFrame.StyledPanel)
#         self.frame_28.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_25 = QHBoxLayout(self.frame_28)
#         self.horizontalLayout_25.setSpacing(2)
#         self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
#         self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
#         self.label_25 = QLabel(self.frame_28)
#         self.label_25.setObjectName(u"label_25")
#         self.label_25.setMinimumSize(QSize(0, 30))
#         self.label_25.setMaximumSize(QSize(16777215, 30))
#         self.label_25.setFont(font2)
#         self.label_25.setLineWidth(5)

#         self.horizontalLayout_25.addWidget(self.label_25, 0, Qt.AlignRight|Qt.AlignBottom)

#         self.label_26 = QLabel(self.frame_28)
#         self.label_26.setObjectName(u"label_26")
#         self.label_26.setMinimumSize(QSize(0, 20))
#         self.label_26.setMaximumSize(QSize(16777215, 20))
#         self.label_26.setFont(font4)
#         self.label_26.setFrameShadow(QFrame.Plain)
#         self.label_26.setAlignment(Qt.AlignCenter)
#         self.label_26.setIndent(-1)

#         self.horizontalLayout_25.addWidget(self.label_26, 0, Qt.AlignLeft|Qt.AlignBottom)


#         self.verticalLayout_13.addWidget(self.frame_28, 0, Qt.AlignHCenter)

#         self.frame_29 = QFrame(self.frame_27)
#         self.frame_29.setObjectName(u"frame_29")
#         self.frame_29.setFrameShape(QFrame.StyledPanel)
#         self.frame_29.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_26 = QHBoxLayout(self.frame_29)
#         self.horizontalLayout_26.setSpacing(2)
#         self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
#         self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)

#         self.verticalLayout_13.addWidget(self.frame_29, 0, Qt.AlignHCenter|Qt.AlignBottom)

#         self.label_27 = QLabel(self.frame_27)
#         self.label_27.setObjectName(u"label_27")
#         self.label_27.setMaximumSize(QSize(16777215, 35))
#         self.label_27.setFont(font6)
#         self.label_27.setStyleSheet(u"")

#         self.verticalLayout_13.addWidget(self.label_27, 0, Qt.AlignHCenter)

#         self.frame_30 = QFrame(self.frame_27)
#         self.frame_30.setObjectName(u"frame_30")
#         self.frame_30.setMinimumSize(QSize(0, 33))
#         self.frame_30.setMaximumSize(QSize(16777215, 33))
#         self.frame_30.setStyleSheet(u"")
#         self.frame_30.setFrameShape(QFrame.StyledPanel)
#         self.frame_30.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_27 = QHBoxLayout(self.frame_30)
#         self.horizontalLayout_27.setSpacing(20)
#         self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
#         self.horizontalLayout_27.setContentsMargins(0, 5, 0, 0)
#         self.pushButton_14 = QPushButton(self.frame_30)
#         self.pushButton_14.setObjectName(u"pushButton_14")
#         self.pushButton_14.setMinimumSize(QSize(75, 28))
#         self.pushButton_14.setMaximumSize(QSize(75, 28))
#         self.pushButton_14.setSizeIncrement(QSize(0, 0))
#         self.pushButton_14.setFont(font7)
#         self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
#         self.pushButton_14.setStyleSheet(u"background: #E94560;\n"
# "border-radius: 3px;\n"
# "")

#         self.horizontalLayout_27.addWidget(self.pushButton_14)

#         self.pushButton_15 = QPushButton(self.frame_30)
#         self.pushButton_15.setObjectName(u"pushButton_15")
#         self.pushButton_15.setMinimumSize(QSize(75, 28))
#         self.pushButton_15.setMaximumSize(QSize(75, 28))
#         self.pushButton_15.setSizeIncrement(QSize(0, 0))
#         self.pushButton_15.setFont(font7)
#         self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
#         self.pushButton_15.setStyleSheet(u"background: #E94560;\n"
# "border-radius: 3px;\n"
# "")

#         self.horizontalLayout_27.addWidget(self.pushButton_15)


#         self.verticalLayout_13.addWidget(self.frame_30, 0, Qt.AlignHCenter|Qt.AlignVCenter)

#         self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

#         self.verticalLayout_13.addItem(self.verticalSpacer_22)


#         self.verticalLayout_5.addWidget(self.frame_27)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


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
        self.close.setText("")
#if QT_CONFIG(shortcut)
        self.close.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F4", None))
#endif // QT_CONFIG(shortcut)
        self.expand.setText("")
#if QT_CONFIG(shortcut)
        self.expand.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.minimize.setText("")
#if QT_CONFIG(shortcut)
        self.minimize.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.Learn_2.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
        self.Loop_2.setText(QCoreApplication.translate("MainWindow", u"Loop", None))
#if QT_CONFIG(statustip)
        self.settings_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.settings_2.setText("")
        self.profilePhoto_2.setText("")
        self.numOfGroups.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.numOfGroups_2.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Courses", None))
        self.numOfGroups_3.setText(QCoreApplication.translate("MainWindow", u"115", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Study Groups", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" NEW", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search.....", None))
        # self.label_22.setText(QCoreApplication.translate("MainWindow", u"1", None))
        # self.label_23.setText(QCoreApplication.translate("MainWindow", u"st", None))
        # self.label_24.setText(QCoreApplication.translate("MainWindow", u"Electrical Power", None))
        # self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        # self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        # self.label_25.setText(QCoreApplication.translate("MainWindow", u"1", None))
        # self.label_26.setText(QCoreApplication.translate("MainWindow", u"st", None))
        # self.label_27.setText(QCoreApplication.translate("MainWindow", u"Electrical Power", None))
        # self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        # self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow =QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())