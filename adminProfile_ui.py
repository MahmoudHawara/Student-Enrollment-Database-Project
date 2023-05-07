# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminProfile.ui'
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

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 50, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.mainPage = QFrame(self.frame)
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setMinimumSize(QSize(400, 0))
        self.mainPage.setMaximumSize(QSize(400, 16777215))
        self.mainPage.setStyleSheet(u"border: none;")
        self.mainPage.setFrameShape(QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.frame_7 = QFrame(self.mainPage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 150))
        self.frame_7.setMaximumSize(QSize(16777215, 150))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(65, 125))
        self.frame_8.setMaximumSize(QSize(65, 100))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.line_9 = QFrame(self.frame_8)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(0, 60, 3, 60))
        self.line_9.setMinimumSize(QSize(0, 60))
        self.line_9.setMaximumSize(QSize(16777215, 60))
        self.line_9.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.line_10 = QFrame(self.frame_8)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(0, 120, 60, 3))
        self.line_10.setMinimumSize(QSize(60, 0))
        self.line_10.setMaximumSize(QSize(60, 16777215))
        self.line_10.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.frame_8)

        self.department_2 = QFrame(self.frame_7)
        self.department_2.setObjectName(u"department_2")
        self.department_2.setMinimumSize(QSize(0, 100))
        self.department_2.setMaximumSize(QSize(750, 100))
        self.department_2.setStyleSheet(u"color: white;")
        self.department_2.setFrameShape(QFrame.StyledPanel)
        self.department_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.department_2)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.department_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Condensed")
        font1.setPointSize(25)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_15.setFont(font1)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_15, 0, Qt.AlignHCenter)

        self.frame_18 = QFrame(self.department_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_20.setSpacing(20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_18)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setFrameShadow(QFrame.Plain)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setIndent(-1)

        self.horizontalLayout_20.addWidget(self.label_12)


        self.verticalLayout_11.addWidget(self.frame_18, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.department_2, 0, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(65, 125))
        self.frame_9.setMaximumSize(QSize(65, 125))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.line_5 = QFrame(self.frame_9)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(60, 0, 3, 60))
        self.line_5.setMinimumSize(QSize(0, 60))
        self.line_5.setMaximumSize(QSize(16777215, 60))
        self.line_5.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.frame_9)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(0, 0, 60, 3))
        self.line_6.setMinimumSize(QSize(60, 0))
        self.line_6.setMaximumSize(QSize(60, 16777215))
        self.line_6.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.frame_9)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.pushButton = QPushButton(self.mainPage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 200))
        self.pushButton.setMaximumSize(QSize(200, 200))
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(200, 200))

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.phone_ID_2 = QFrame(self.mainPage)
        self.phone_ID_2.setObjectName(u"phone_ID_2")
        self.phone_ID_2.setMinimumSize(QSize(0, 120))
        self.phone_ID_2.setMaximumSize(QSize(16777215, 120))
        self.phone_ID_2.setStyleSheet(u"")
        self.phone_ID_2.setFrameShape(QFrame.StyledPanel)
        self.phone_ID_2.setFrameShadow(QFrame.Raised)
        self.phone_ID_2.setLineWidth(1)
        self.verticalLayout_6 = QVBoxLayout(self.phone_ID_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.phonenum_2 = QFrame(self.phone_ID_2)
        self.phonenum_2.setObjectName(u"phonenum_2")
        self.phonenum_2.setMinimumSize(QSize(400, 120))
        self.phonenum_2.setMaximumSize(QSize(400, 120))
        self.phonenum_2.setStyleSheet(u"")
        self.phonenum_2.setFrameShape(QFrame.StyledPanel)
        self.phonenum_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.phonenum_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.phonenum_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 22))
        self.label_4.setMaximumSize(QSize(16777215, 22))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiBold")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"\n"
"color: #FFFFFF")

        self.verticalLayout_7.addWidget(self.label_4)

        self.lineEdit_6 = QLineEdit(self.phonenum_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(243, 50))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light SemiCondensed")
        font3.setPointSize(14)
        self.lineEdit_6.setFont(font3)
        self.lineEdit_6.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"margin-top: 10px;\n"
"")
        self.lineEdit_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_6.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.lineEdit_6)


        self.verticalLayout_6.addWidget(self.phonenum_2)


        self.verticalLayout_2.addWidget(self.phone_ID_2, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.mainPage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(400, 120))
        self.frame_11.setMaximumSize(QSize(400, 120))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.DOB_2 = QFrame(self.frame_11)
        self.DOB_2.setObjectName(u"DOB_2")
        self.DOB_2.setMinimumSize(QSize(400, 120))
        self.DOB_2.setMaximumSize(QSize(400, 120))
        self.DOB_2.setStyleSheet(u"")
        self.DOB_2.setFrameShape(QFrame.StyledPanel)
        self.DOB_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.DOB_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.DOB_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(386, 35))
        self.label_11.setMaximumSize(QSize(200, 35))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"\n"
"color: #FFFFFF;")

        self.verticalLayout_8.addWidget(self.label_11)

        self.lineEdit_8 = QLineEdit(self.DOB_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(400, 50))
        self.lineEdit_8.setMaximumSize(QSize(400, 50))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiBold Condensed")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.lineEdit_8.setFont(font4)
        self.lineEdit_8.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"letter-spacing: 5px;\n"
"margin-top: 10px;")
        self.lineEdit_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lineEdit_8)


        self.horizontalLayout_9.addWidget(self.DOB_2, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_11, 0, Qt.AlignHCenter)

        self.pushButton_4 = QPushButton(self.mainPage)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(400, 38))
        self.pushButton_4.setMaximumSize(QSize(400, 38))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift Condensed")
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.pushButton_4.setFont(font5)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"\n"
"\n"
"background: #E94560;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_4, 0, Qt.AlignHCenter)

        self.pushButton_5 = QPushButton(self.mainPage)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(400, 38))
        self.pushButton_5.setMaximumSize(QSize(400, 38))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift Condensed")
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.pushButton_5.setFont(font6)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"letter-spacing: 0.5px;\n"
"\n"
"background: #E94560;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_5, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.mainPage, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame)

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
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Mahmoud", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Hawara", None))
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"someone123@learnloop.edu.eg", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"**********", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow =QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())