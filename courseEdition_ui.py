# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'courseEdition.ui'
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
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 20, 0)
        self.ControlButtons = QFrame(self.header)
        self.ControlButtons.setObjectName(u"ControlButtons")
        self.horizontalLayout_6 = QHBoxLayout(self.ControlButtons)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.close = QPushButton(self.ControlButtons)
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

        self.expand = QPushButton(self.ControlButtons)
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

        self.minimize = QPushButton(self.ControlButtons)
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


        self.horizontalLayout.addWidget(self.ControlButtons, 0, Qt.AlignLeft)

        self.Logo = QFrame(self.header)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.Logo)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Learn = QLabel(self.Logo)
        self.Learn.setObjectName(u"Learn")
        font = QFont()
        font.setFamily(u"Tw Cen MT Condensed Extra Bold")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Learn.setFont(font)
        self.Learn.setStyleSheet(u"color: white")
        self.Learn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Learn.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.Learn)

        self.Loop = QLabel(self.Logo)
        self.Loop.setObjectName(u"Loop")
        self.Loop.setFont(font)
        self.Loop.setStyleSheet(u"color: #E94560")

        self.horizontalLayout_2.addWidget(self.Loop)


        self.horizontalLayout.addWidget(self.Logo)

        self.ProfilePhotoAndSettings = QFrame(self.header)
        self.ProfilePhotoAndSettings.setObjectName(u"ProfilePhotoAndSettings")
        self.ProfilePhotoAndSettings.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.ProfilePhotoAndSettings)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.ProfilePhotoAndSettings, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.mainPage = QFrame(self.centralwidget)
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setMaximumSize(QSize(16777215, 16777215))
        self.mainPage.setStyleSheet(u"border: none;")
        self.mainPage.setFrameShape(QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.mainPage)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 70, 0, 0)
        self.SecondHeader = QFrame(self.mainPage)
        self.SecondHeader.setObjectName(u"SecondHeader")
        self.SecondHeader.setMaximumSize(QSize(16777215, 53))
        self.SecondHeader.setFrameShape(QFrame.StyledPanel)
        self.SecondHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.SecondHeader)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.logo_2 = QFrame(self.SecondHeader)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setMinimumSize(QSize(675, 53))
        self.logo_2.setMaximumSize(QSize(16777215, 53))
        self.logo_2.setSizeIncrement(QSize(0, 0))
        self.logo_2.setBaseSize(QSize(0, 0))
        self.logo_2.setStyleSheet(u"  border-top-right-radius: 5px;\n"
"  border-bottom-right-radius: 5px;background: #E94560\n"
"\n"
"")
        self.logo_2.setFrameShape(QFrame.StyledPanel)
        self.logo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.logo_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 135, 0)
        self.label_14 = QLabel(self.logo_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(433, 34))
        self.label_14.setMaximumSize(QSize(433, 37))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Condensed")
        font1.setPointSize(22)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"letter-spacing: 0.5px;\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.label_14, 0, Qt.AlignRight)


        self.horizontalLayout_13.addWidget(self.logo_2)


        self.verticalLayout_9.addWidget(self.SecondHeader, 0, Qt.AlignLeft)

        self.page = QFrame(self.mainPage)
        self.page.setObjectName(u"page")
        self.page.setMinimumSize(QSize(0, 0))
        self.page.setMaximumSize(QSize(16777215, 16777215))
        self.page.setSizeIncrement(QSize(2, 0))
        self.page.setStyleSheet(u"")
        self.page.setFrameShape(QFrame.StyledPanel)
        self.page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.page)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.phone_ID_2 = QFrame(self.page)
        self.phone_ID_2.setObjectName(u"phone_ID_2")
        self.phone_ID_2.setMinimumSize(QSize(0, 150))
        self.phone_ID_2.setMaximumSize(QSize(16777215, 150))
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
        self.phonenum_2.setMinimumSize(QSize(400, 150))
        self.phonenum_2.setMaximumSize(QSize(400, 150))
        self.phonenum_2.setStyleSheet(u"")
        self.phonenum_2.setFrameShape(QFrame.StyledPanel)
        self.phonenum_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.phonenum_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.phonenum_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(144, 22))
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

        self.verticalLayout_7.addWidget(self.lineEdit_6)

        self.label_8 = QLabel(self.phonenum_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(395, 50))
        self.label_8.setMaximumSize(QSize(395, 50))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiLight")
        font4.setPointSize(11)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"\n"
"color: #E94560;")
        self.label_8.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_8)


        self.verticalLayout_6.addWidget(self.phonenum_2)


        self.verticalLayout_10.addWidget(self.phone_ID_2, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 150))
        self.frame_11.setMaximumSize(QSize(16777215, 150))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.DOB_2 = QFrame(self.frame_11)
        self.DOB_2.setObjectName(u"DOB_2")
        self.DOB_2.setMinimumSize(QSize(0, 150))
        self.DOB_2.setMaximumSize(QSize(16777215, 150))
        self.DOB_2.setStyleSheet(u"")
        self.DOB_2.setFrameShape(QFrame.StyledPanel)
        self.DOB_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.DOB_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.DOB_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(386, 22))
        self.label_11.setMaximumSize(QSize(200, 22))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"\n"
"color: #FFFFFF;")

        self.verticalLayout_8.addWidget(self.label_11)

        self.lineEdit_8 = QLineEdit(self.DOB_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(400, 50))
        self.lineEdit_8.setMaximumSize(QSize(400, 50))
        self.lineEdit_8.setFont(font3)
        self.lineEdit_8.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"margin-top: 10px;\n"
"")
        self.lineEdit_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lineEdit_8)

        self.label_5 = QLabel(self.DOB_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(395, 25))
        self.label_5.setMaximumSize(QSize(395, 25))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"\n"
"color: #E94560;")

        self.verticalLayout_8.addWidget(self.label_5)


        self.horizontalLayout_8.addWidget(self.DOB_2, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_11, 0, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 100))
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setStyleSheet(u"border: none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(400, 0))
        self.frame_9.setMaximumSize(QSize(400, 16777215))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(144, 22))
        self.label_15.setMaximumSize(QSize(144, 22))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift SemiBold")
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"\n"
"color: #FFFFFF;")

        self.verticalLayout_13.addWidget(self.label_15)

        self.comboBox_2 = QComboBox(self.frame_9)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 40))
        self.comboBox_2.setFont(font3)
        self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_2.setStyleSheet(u" QComboBox {\n"
"        border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"\n"
"    }\n"
"    QComboBox::hover {\n"
"    }\n"
"QComboBox QAbstractItemView { background-color: #0F3460; }\n"
"")

        self.verticalLayout_13.addWidget(self.comboBox_2)


        self.horizontalLayout_7.addWidget(self.frame_9)


        self.verticalLayout_10.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 60))
        self.frame_10.setMaximumSize(QSize(16777215, 60))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setSpacing(50)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 20, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_10)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(175, 38))
        self.pushButton_4.setMaximumSize(QSize(175, 38))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift Condensed")
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.pushButton_4.setFont(font6)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"letter-spacing: 0.5px;\n"
"\n"
"\n"
"background: #E94560;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")

        self.horizontalLayout_12.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_10)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(175, 38))
        self.pushButton_5.setMaximumSize(QSize(175, 38))
        self.pushButton_5.setFont(font6)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"letter-spacing: 0.5px;\n"
"\n"
"background: #E94560;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")

        self.horizontalLayout_12.addWidget(self.pushButton_5)


        self.verticalLayout_10.addWidget(self.frame_10, 0, Qt.AlignHCenter)

        self.pushButton_6 = QPushButton(self.page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(400, 38))
        self.pushButton_6.setMaximumSize(QSize(400, 38))
        font7 = QFont()
        font7.setFamily(u"Bahnschrift Condensed")
        font7.setPointSize(20)
        font7.setBold(False)
        font7.setWeight(50)
        self.pushButton_6.setFont(font7)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"letter-spacing: 0.5px;\n"
"\n"
"\n"
"background: #E94560;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")

        self.verticalLayout_10.addWidget(self.pushButton_6, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 30))
        self.frame_12.setMaximumSize(QSize(16777215, 30))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 5, 0, 0)
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(395, 25))
        self.label_6.setMaximumSize(QSize(395, 25))
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"\n"
"color: #E94560;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setMargin(0)

        self.horizontalLayout_11.addWidget(self.label_6)


        self.verticalLayout_10.addWidget(self.frame_12, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.verticalLayout_9.addWidget(self.page)


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
        self.Learn.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
        self.Loop.setText(QCoreApplication.translate("MainWindow", u"Loop", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Course Edition", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Course Name", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ECE 115", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Course Name must contain Capital English letters and digits only ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Number Of Hours", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Number of Hours must contain Digits only ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Term", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"First", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Second", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"There is another Course with The Same Name", None))
    # retranslateUi

