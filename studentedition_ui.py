# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentedition.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 770)
        MainWindow.setMinimumSize(QSize(880, 770))
        MainWindow.setStyleSheet(u"background:  #16213E")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(20)
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
        self.close.setMinimumSize(QSize(20, 0))
        self.close.setMaximumSize(QSize(20, 16777215))
        icon = QIcon()
        icon.addFile(u"Images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon)
        self.close.setIconSize(QSize(13, 16))
        self.close.setFlat(True)

        self.horizontalLayout_6.addWidget(self.close)

        self.expand = QPushButton(self.ControlButtons_2)
        self.expand.setObjectName(u"expand")
        self.expand.setMinimumSize(QSize(20, 25))
        self.expand.setMaximumSize(QSize(20, 25))
        icon1 = QIcon()
        icon1.addFile(u"Images/expand-arrows.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand.setIcon(icon1)
        self.expand.setIconSize(QSize(20, 25))
        self.expand.setFlat(True)

        self.horizontalLayout_6.addWidget(self.expand)

        self.minimize = QPushButton(self.ControlButtons_2)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(20, 20))
        self.minimize.setMaximumSize(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u"Images/minimize-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon2)
        self.minimize.setIconSize(QSize(13, 16))
        self.minimize.setFlat(True)

        self.horizontalLayout_6.addWidget(self.minimize)


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
        font.setFamily(u"Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Learn_2.setFont(font)
        self.Learn_2.setStyleSheet(u"color: white")
        self.Learn_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Learn_2.setWordWrap(False)
        self.Learn_2.setMargin(3)

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
        self.settings_2.setStyleSheet(u"background-color: #E94560;\n"
"border-style: outset")
        icon3 = QIcon()
        icon3.addFile(u"Images/setting.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.profilePhoto_2.setMinimumSize(QSize(50, 50))
        self.profilePhoto_2.setMaximumSize(QSize(50, 50))
        self.profilePhoto_2.setAutoFillBackground(False)
        self.profilePhoto_2.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"../../../../Desktop/59022631_810914472627047_3797622654492475392_n.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.profilePhoto_2.setIcon(icon4)
        self.profilePhoto_2.setIconSize(QSize(50, 45))
        self.profilePhoto_2.setAutoDefault(False)
        self.profilePhoto_2.setFlat(True)

        self.horizontalLayout_8.addWidget(self.profilePhoto_2)


        self.horizontalLayout_4.addWidget(self.ProfilePhotoAndSettings_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.mainPage = QFrame(self.centralwidget)
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setMaximumSize(QSize(16777215, 16777215))
        self.mainPage.setStyleSheet(u"background-color: #16213E;")
        self.mainPage.setFrameShape(QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.logo = QFrame(self.mainPage)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 53))
        self.logo.setMaximumSize(QSize(608, 16777215))
        self.logo.setStyleSheet(u"\n"
"position: absolute;\n"
"width: 608px;\n"
"height: 53px;\n"
"\n"
"background: #E94560")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.logo)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.logo)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(433, 34))
        self.label_12.setMaximumSize(QSize(433, 37))
        self.label_12.setStyleSheet(u"position: absolute;\n"
"width: 433px;\n"
"height: 34px;\n"
"\n"
"font-family: 'Righteous';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 25px;\n"
"line-height: 31px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #FFFFFF;")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_12, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.logo)

        self.verticalSpacer_7 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.First_secondname = QFrame(self.mainPage)
        self.First_secondname.setObjectName(u"First_secondname")
        self.First_secondname.setMinimumSize(QSize(0, 118))
        self.First_secondname.setMaximumSize(QSize(16777215, 16777215))
        self.First_secondname.setStyleSheet(u"")
        self.First_secondname.setFrameShape(QFrame.StyledPanel)
        self.First_secondname.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.First_secondname)
        self.horizontalLayout.setSpacing(56)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(164, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frame = QFrame(self.First_secondname)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 118))
        self.frame.setMaximumSize(QSize(243, 118))
        self.frame.setStyleSheet(u"background-color:#16213E;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(144, 22))
        self.label_2.setMaximumSize(QSize(144, 22))
        self.label_2.setStyleSheet(u"position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 17px;\n"
"line-height: 21px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #FFFFFF")

        self.verticalLayout_5.addWidget(self.label_2)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(243, 0))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_3.setStyleSheet(u" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.lineEdit_3)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(240, 30))
        self.label_5.setMaximumSize(QSize(240, 34))
        self.label_5.setStyleSheet(u"position: absolute;\n"
"width: 240px;\n"
"height: 25px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 18px;\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #E94560;")
        self.label_5.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_5)


        self.horizontalLayout.addWidget(self.frame)

        self.firstname = QFrame(self.First_secondname)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setMinimumSize(QSize(0, 118))
        self.firstname.setMaximumSize(QSize(243, 118))
        self.firstname.setStyleSheet(u"\n"
"\n"
"background: #16213E;;")
        self.firstname.setFrameShape(QFrame.StyledPanel)
        self.firstname.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.firstname)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.firstname)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(144, 22))
        self.label_4.setMaximumSize(QSize(144, 22))
        self.label_4.setStyleSheet(u"position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 17px;\n"
"line-height: 21px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #FFFFFF")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.firstname)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(243, 0))
        self.lineEdit_4.setStyleSheet(u" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")

        self.verticalLayout_6.addWidget(self.lineEdit_4)

        self.label_6 = QLabel(self.firstname)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(240, 30))
        self.label_6.setMaximumSize(QSize(240, 34))
        self.label_6.setStyleSheet(u"position: absolute;\n"
"width: 240px;\n"
"height: 25px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 18px;\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #E94560;")
        self.label_6.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_6)


        self.horizontalLayout.addWidget(self.firstname)

        self.horizontalSpacer_3 = QSpacerItem(172, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.First_secondname)

        self.phone_ID = QFrame(self.mainPage)
        self.phone_ID.setObjectName(u"phone_ID")
        self.phone_ID.setMinimumSize(QSize(0, 116))
        self.phone_ID.setMaximumSize(QSize(16777215, 116))
        self.phone_ID.setStyleSheet(u"background: #16213E;")
        self.phone_ID.setFrameShape(QFrame.StyledPanel)
        self.phone_ID.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.phone_ID)
        self.horizontalLayout_2.setSpacing(56)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(164, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.phonenum = QFrame(self.phone_ID)
        self.phonenum.setObjectName(u"phonenum")
        self.phonenum.setMaximumSize(QSize(243, 118))
        self.phonenum.setStyleSheet(u"background: #16213E;")
        self.phonenum.setFrameShape(QFrame.StyledPanel)
        self.phonenum.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.phonenum)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.phonenum)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(144, 22))
        self.label_3.setMaximumSize(QSize(144, 22))
        self.label_3.setStyleSheet(u"position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 17px;\n"
"line-height: 21px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #FFFFFF")

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_5 = QLineEdit(self.phonenum)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(243, 0))
        self.lineEdit_5.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_5.setStyleSheet(u" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_5)

        self.label_7 = QLabel(self.phonenum)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(240, 20))
        self.label_7.setMaximumSize(QSize(240, 20))
        self.label_7.setStyleSheet(u"position: absolute;\n"
"width: 240px;\n"
"height: 25px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 18px;\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #E94560;")
        self.label_7.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_7)


        self.horizontalLayout_2.addWidget(self.phonenum)

        self.frame_2 = QFrame(self.phone_ID)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(243, 118))
        self.frame_2.setStyleSheet(u"background: #16213E;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(144, 22))
        self.label_8.setMaximumSize(QSize(144, 22))
        self.label_8.setStyleSheet(u"position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 17px;\n"
"line-height: 21px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #FFFFFF")

        self.verticalLayout_7.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(243, 0))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_6.setStyleSheet(u" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.lineEdit_6)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(240, 20))
        self.label_9.setMaximumSize(QSize(240, 20))
        self.label_9.setStyleSheet(u"position: absolute;\n"
"width: 240px;\n"
"height: 25px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 18px;\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #E94560;")
        self.label_9.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_9)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.horizontalSpacer_4 = QSpacerItem(172, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.phone_ID)

        self.signin = QFrame(self.mainPage)
        self.signin.setObjectName(u"signin")
        self.signin.setMinimumSize(QSize(0, 0))
        self.signin.setFrameShape(QFrame.StyledPanel)
        self.signin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.signin)
        self.verticalLayout_4.setSpacing(56)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.signin)

        self.frame_3 = QFrame(self.mainPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setStyleSheet(u"background: #16213E;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(56)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(164, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.DOB = QFrame(self.frame_3)
        self.DOB.setObjectName(u"DOB")
        self.DOB.setMaximumSize(QSize(243, 116))
        self.DOB.setStyleSheet(u"background: #16213E;")
        self.DOB.setFrameShape(QFrame.StyledPanel)
        self.DOB.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.DOB)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.DOB)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(144, 22))
        self.label_10.setMaximumSize(QSize(144, 22))
        self.label_10.setStyleSheet(u"position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 17px;\n"
"line-height: 21px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #FFFFFF;")

        self.verticalLayout_8.addWidget(self.label_10)

        self.lineEdit_7 = QLineEdit(self.DOB)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(243, 0))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_7.setStyleSheet(u" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lineEdit_7)


        self.horizontalLayout_3.addWidget(self.DOB)

        self.Gender = QFrame(self.frame_3)
        self.Gender.setObjectName(u"Gender")
        self.Gender.setMaximumSize(QSize(243, 116))
        self.Gender.setStyleSheet(u"background: #16213E;")
        self.Gender.setFrameShape(QFrame.StyledPanel)
        self.Gender.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Gender)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.Gender)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(144, 22))
        self.label_11.setMaximumSize(QSize(144, 22))
        self.label_11.setStyleSheet(u"position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 17px;\n"
"line-height: 21px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #FFFFFF;")

        self.verticalLayout_10.addWidget(self.label_11)

        self.lineEdit_9 = QLineEdit(self.Gender)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(243, 0))
        self.lineEdit_9.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_9.setStyleSheet(u" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.lineEdit_9)


        self.horizontalLayout_3.addWidget(self.Gender)

        self.horizontalSpacer_6 = QSpacerItem(172, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.mainPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 80))
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setStyleSheet(u"background: #16213E;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(545, 0))
        self.frame_5.setMaximumSize(QSize(545, 16777215))
        self.frame_5.setStyleSheet(u"background: #16213E;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(144, 22))
        self.label_13.setMaximumSize(QSize(144, 22))
        self.label_13.setStyleSheet(u"position: absolute;\n"
"width: 322.96px;\n"
"height: 22px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 17px;\n"
"line-height: 21px;\n"
"/* identical to box height */\n"
"\n"
"display: flex;\n"
"align-items: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #FFFFFF;")

        self.verticalLayout_11.addWidget(self.label_13)

        self.lineEdit_10 = QLineEdit(self.frame_5)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(545, 0))
        self.lineEdit_10.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_10.setStyleSheet(u" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.lineEdit_10)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.mainPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 55))
        self.frame_6.setMaximumSize(QSize(16777215, 55))
        self.frame_6.setStyleSheet(u"background: #16213E;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(45)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(164, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(175, 38))
        self.pushButton_2.setMaximumSize(QSize(175, 38))
        self.pushButton_2.setStyleSheet(u"\n"
"position: absolute;\n"
"width: 175px;\n"
"height: 38.5px;\n"
"\n"
"background: #E94560;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"position: absolute;\n"
"width: 175px;\n"
"height: 38.5px;\n"
"\n"
"font-family: 'Righteous';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 24px;\n"
"line-height: 30px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #FFFFFF;\n"
"")

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(175, 38))
        self.pushButton_3.setMaximumSize(QSize(175, 38))
        self.pushButton_3.setStyleSheet(u"\n"
"position: absolute;\n"
"width: 175px;\n"
"height: 38.5px;\n"
"\n"
"background: #E94560;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"position: absolute;\n"
"width: 175px;\n"
"height: 38.5px;\n"
"\n"
"font-family: 'Righteous';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 24px;\n"
"line-height: 30px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #FFFFFF;\n"
"")

        self.horizontalLayout_9.addWidget(self.pushButton_3)

        self.horizontalSpacer_8 = QSpacerItem(172, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.mainPage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 100))
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setStyleSheet(u"background: #16213E;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(396, 38))
        self.pushButton_4.setMaximumSize(QSize(396, 38))
        self.pushButton_4.setStyleSheet(u"\n"
"position: absolute;\n"
"width: 175px;\n"
"height: 38.5px;\n"
"\n"
"background: #E94560;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"position: absolute;\n"
"width: 175px;\n"
"height: 38.5px;\n"
"\n"
"font-family: 'Righteous';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 24px;\n"
"line-height: 30px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #FFFFFF;\n"
"")

        self.verticalLayout_12.addWidget(self.pushButton_4, 0, Qt.AlignHCenter)

        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(395, 15))
        self.label.setMaximumSize(QSize(395, 15))
        self.label.setStyleSheet(u"position: absolute;\n"
"width: 395.01px;\n"
"height: 15.22px;\n"
"\n"
"font-family: 'Outfit';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 18px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"letter-spacing: 0.11em;\n"
"\n"
"color: #E94560;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.verticalSpacer_4 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.verticalLayout.addWidget(self.mainPage)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.settings_2.setDefault(False)
        self.profilePhoto_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.close.setText("")
        self.expand.setText("")
        self.minimize.setText("")
        self.Learn_2.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
        self.Loop_2.setText(QCoreApplication.translate("MainWindow", u"Loop", None))
#if QT_CONFIG(statustip)
        self.settings_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.settings_2.setText("")
        self.profilePhoto_2.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Student Edition ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"First Name must contain English letters only ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Last Name must contain English letters only ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"01151239658", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Phone Number is Invalid", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"33333333333333333", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ID is Invalid", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Birth Date", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"11 / 5 / 2001", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"Name@@learnloop.edu.eg", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"There is another Student with the same ID ", None))
    # retranslateUi

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())