# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentAddition.ui'
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
        MainWindow.resize(920, 1003)
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
        self.Logo.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.Logo)
        self.horizontalLayout_2.setSpacing(9)
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
        self.verticalLayout_9.setSpacing(0)
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
        self.logo_2.setMinimumSize(QSize(760, 53))
        self.logo_2.setMaximumSize(QSize(16777215, 53))
        self.logo_2.setSizeIncrement(QSize(0, 0))
        self.logo_2.setBaseSize(QSize(0, 0))
        self.logo_2.setStyleSheet(u"  border-top-right-radius: 5px;\n"
"  border-bottom-right-radius: 5px;background: #E94560")
        self.logo_2.setFrameShape(QFrame.StyledPanel)
        self.logo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.logo_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 194, 0)
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
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 20, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(100)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.phone_ID_2 = QFrame(self.frame)
        self.phone_ID_2.setObjectName(u"phone_ID_2")
        self.phone_ID_2.setMinimumSize(QSize(245, 150))
        self.phone_ID_2.setMaximumSize(QSize(245, 150))
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
        self.phonenum_2.setMinimumSize(QSize(245, 150))
        self.phonenum_2.setMaximumSize(QSize(245, 150))
        self.phonenum_2.setStyleSheet(u"")
        self.phonenum_2.setFrameShape(QFrame.StyledPanel)
        self.phonenum_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.phonenum_2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
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

        self.verticalLayout_15.addWidget(self.label_4)

        self.lineEdit_12 = QLineEdit(self.phonenum_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(243, 50))
        self.lineEdit_12.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light SemiCondensed")
        font3.setPointSize(14)
        self.lineEdit_12.setFont(font3)
        self.lineEdit_12.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"margin-top: 10px;\n"
"\n"
"")
        self.lineEdit_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lineEdit_12)

        self.label_17 = QLabel(self.phonenum_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(240, 30))
        self.label_17.setMaximumSize(QSize(240, 50))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiLight")
        font4.setPointSize(11)
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"color: #E94560;")
        self.label_17.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_17)


        self.verticalLayout_6.addWidget(self.phonenum_2)


        self.horizontalLayout_3.addWidget(self.phone_ID_2)

        self.phone_ID_3 = QFrame(self.frame)
        self.phone_ID_3.setObjectName(u"phone_ID_3")
        self.phone_ID_3.setMinimumSize(QSize(245, 150))
        self.phone_ID_3.setMaximumSize(QSize(245, 150))
        self.phone_ID_3.setStyleSheet(u"")
        self.phone_ID_3.setFrameShape(QFrame.StyledPanel)
        self.phone_ID_3.setFrameShadow(QFrame.Raised)
        self.phone_ID_3.setLineWidth(1)
        self.verticalLayout_27 = QVBoxLayout(self.phone_ID_3)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.phonenum_8 = QFrame(self.phone_ID_3)
        self.phonenum_8.setObjectName(u"phonenum_8")
        self.phonenum_8.setMinimumSize(QSize(245, 150))
        self.phonenum_8.setMaximumSize(QSize(245, 150))
        self.phonenum_8.setStyleSheet(u"")
        self.phonenum_8.setFrameShape(QFrame.StyledPanel)
        self.phonenum_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.phonenum_8)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.phonenum_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 22))
        self.label_26.setMaximumSize(QSize(16777215, 22))
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"\n"
"color: #FFFFFF")

        self.verticalLayout_28.addWidget(self.label_26)

        self.lineEdit_18 = QLineEdit(self.phonenum_8)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(243, 50))
        self.lineEdit_18.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_18.setFont(font3)
        self.lineEdit_18.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"margin-top: 10px;\n"
"")
        self.lineEdit_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.lineEdit_18)

        self.label_27 = QLabel(self.phonenum_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(240, 50))
        self.label_27.setMaximumSize(QSize(240, 50))
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"\n"
"\n"
"color: #E94560;")
        self.label_27.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.label_27)


        self.verticalLayout_27.addWidget(self.phonenum_8)


        self.horizontalLayout_3.addWidget(self.phone_ID_3)


        self.verticalLayout_10.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(100)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.phonenum_9 = QFrame(self.frame_2)
        self.phonenum_9.setObjectName(u"phonenum_9")
        self.phonenum_9.setMinimumSize(QSize(245, 150))
        self.phonenum_9.setMaximumSize(QSize(245, 150))
        self.phonenum_9.setStyleSheet(u"")
        self.phonenum_9.setFrameShape(QFrame.StyledPanel)
        self.phonenum_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.phonenum_9)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.phonenum_9)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 22))
        self.label_16.setMaximumSize(QSize(16777215, 22))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"\n"
"color: #FFFFFF")

        self.verticalLayout_29.addWidget(self.label_16)

        self.lineEdit_19 = QLineEdit(self.phonenum_9)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(243, 50))
        self.lineEdit_19.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_19.setFont(font3)
        self.lineEdit_19.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"margin-top: 10px;\n"
"")
        self.lineEdit_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.lineEdit_19)

        self.label_31 = QLabel(self.phonenum_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(240, 20))
        self.label_31.setMaximumSize(QSize(240, 20))
        self.label_31.setFont(font4)
        self.label_31.setStyleSheet(u"\n"
"color: #E94560;")
        self.label_31.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_31)


        self.horizontalLayout_5.addWidget(self.phonenum_9)

        self.phonenum_10 = QFrame(self.frame_2)
        self.phonenum_10.setObjectName(u"phonenum_10")
        self.phonenum_10.setMinimumSize(QSize(245, 150))
        self.phonenum_10.setMaximumSize(QSize(245, 150))
        self.phonenum_10.setStyleSheet(u"")
        self.phonenum_10.setFrameShape(QFrame.StyledPanel)
        self.phonenum_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.phonenum_10)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.phonenum_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 22))
        self.label_29.setMaximumSize(QSize(16777215, 22))
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"\n"
"color: #FFFFFF")

        self.verticalLayout_30.addWidget(self.label_29)

        self.lineEdit_20 = QLineEdit(self.phonenum_10)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(243, 50))
        self.lineEdit_20.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_20.setFont(font3)
        self.lineEdit_20.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"margin-top: 10px;\n"
"\n"
"")
        self.lineEdit_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_30.addWidget(self.lineEdit_20)

        self.label_30 = QLabel(self.phonenum_10)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(240, 20))
        self.label_30.setMaximumSize(QSize(240, 20))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift SemiLight")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"\n"
"color: #E94560;")
        self.label_30.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.label_30)


        self.horizontalLayout_5.addWidget(self.phonenum_10)


        self.verticalLayout_10.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 100))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(100)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 100))
        self.frame_9.setMaximumSize(QSize(245, 100))
        self.frame_9.setStyleSheet(u"border: none;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(245, 0))
        self.frame_11.setMaximumSize(QSize(245, 16777215))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_11)
        self.verticalLayout_31.setSpacing(20)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_11)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 22))
        self.label_28.setMaximumSize(QSize(16777215, 22))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift SemiBold")
        font6.setPointSize(15)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_28.setFont(font6)
        self.label_28.setStyleSheet(u"\n"
"color: #FFFFFF;")

        self.verticalLayout_31.addWidget(self.label_28)

        self.comboBox_2 = QComboBox(self.frame_11)
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

        self.verticalLayout_31.addWidget(self.comboBox_2)


        self.horizontalLayout_10.addWidget(self.frame_11)


        self.horizontalLayout_8.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 100))
        self.frame_8.setMaximumSize(QSize(245, 100))
        self.frame_8.setStyleSheet(u"border: none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(245, 0))
        self.frame_14.setMaximumSize(QSize(245, 16777215))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_14)
        self.verticalLayout_33.setSpacing(20)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_14)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 22))
        self.label_34.setMaximumSize(QSize(16777215, 22))
        self.label_34.setFont(font6)
        self.label_34.setStyleSheet(u"\n"
"color: #FFFFFF;")

        self.verticalLayout_33.addWidget(self.label_34)

        self.dateEdit = QDateEdit(self.frame_14)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 40))
        self.dateEdit.setFont(font3)
        self.dateEdit.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"font-size: 14pt;")
        self.dateEdit.setDateTime(QDateTime(QDate(2001, 5, 11), QTime(0, 0, 0)))

        self.verticalLayout_33.addWidget(self.dateEdit)


        self.horizontalLayout_7.addWidget(self.frame_14)


        self.horizontalLayout_8.addWidget(self.frame_8)


        self.verticalLayout_10.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 100))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, -1)
        self.phone_ID_4 = QFrame(self.frame_4)
        self.phone_ID_4.setObjectName(u"phone_ID_4")
        self.phone_ID_4.setMinimumSize(QSize(590, 125))
        self.phone_ID_4.setMaximumSize(QSize(590, 125))
        self.phone_ID_4.setStyleSheet(u"")
        self.phone_ID_4.setFrameShape(QFrame.StyledPanel)
        self.phone_ID_4.setFrameShadow(QFrame.Raised)
        self.phone_ID_4.setLineWidth(1)
        self.verticalLayout_34 = QVBoxLayout(self.phone_ID_4)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.phonenum_11 = QFrame(self.phone_ID_4)
        self.phonenum_11.setObjectName(u"phonenum_11")
        self.phonenum_11.setMinimumSize(QSize(590, 125))
        self.phonenum_11.setMaximumSize(QSize(590, 125))
        self.phonenum_11.setStyleSheet(u"")
        self.phonenum_11.setFrameShape(QFrame.StyledPanel)
        self.phonenum_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.phonenum_11)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 20, 0, 0)
        self.label_35 = QLabel(self.phonenum_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 22))
        self.label_35.setMaximumSize(QSize(16777215, 22))
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"\n"
"color: #FFFFFF")

        self.verticalLayout_35.addWidget(self.label_35)

        self.lineEdit_10 = QLineEdit(self.phonenum_11)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 50))
        self.lineEdit_10.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_10.setFont(font3)
        self.lineEdit_10.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"margin-top: 10px;\n"
"")
        self.lineEdit_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_10.setReadOnly(True)

        self.verticalLayout_35.addWidget(self.lineEdit_10)


        self.verticalLayout_34.addWidget(self.phonenum_11)


        self.horizontalLayout_14.addWidget(self.phone_ID_4)


        self.verticalLayout_10.addWidget(self.frame_4, 0, Qt.AlignHCenter)

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
        font7 = QFont()
        font7.setFamily(u"Bahnschrift Condensed")
        font7.setPointSize(20)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.pushButton_4.setFont(font7)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"letter-spacing: 0.5px;\n"
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
        self.pushButton_5.setFont(font7)
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
        self.label_6.setMinimumSize(QSize(0, 25))
        self.label_6.setMaximumSize(QSize(16777215, 25))
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
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Student Addition", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mahmoud", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"First Name must contain English letters only ", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hawara", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Last Name must contain English letters only ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"ID is Invalid", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"01151239658", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Phone Number is Invalid", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Birth Date", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Course Name", None))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mahmoud115@learnloop.edu.eg", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"There is another Student with The Same ID", None))
    # retranslateUi

