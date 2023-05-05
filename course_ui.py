# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'course.ui'
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
        MainWindow.resize(937, 818)
        MainWindow.setMinimumSize(QSize(880, 770))
        MainWindow.setStyleSheet(u"background:  #16213E")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_2 = QFrame(self.centralwidget)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setMinimumSize(QSize(0, 50))
        self.header_2.setMaximumSize(QSize(16777215, 50))
        self.header_2.setStyleSheet(u"background: #0F3460")
        self.horizontalLayout_4 = QHBoxLayout(self.header_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ControlButtons_2 = QFrame(self.header_2)
        self.ControlButtons_2.setObjectName(u"ControlButtons_2")
        self.horizontalLayout_6 = QHBoxLayout(self.ControlButtons_2)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.close_2 = QPushButton(self.ControlButtons_2)
        self.close_2.setObjectName(u"close_2")
        self.close_2.setMinimumSize(QSize(20, 0))
        self.close_2.setMaximumSize(QSize(20, 16777215))
        icon = QIcon()
        icon.addFile(u"C:/Downloads/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_2.setIcon(icon)
        self.close_2.setIconSize(QSize(13, 16))
        self.close_2.setFlat(True)

        self.horizontalLayout_6.addWidget(self.close_2)

        self.expand_2 = QPushButton(self.ControlButtons_2)
        self.expand_2.setObjectName(u"expand_2")
        self.expand_2.setMinimumSize(QSize(20, 25))
        self.expand_2.setMaximumSize(QSize(20, 25))
        icon1 = QIcon()
        icon1.addFile(u"C:/Downloads/expand-arrows.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand_2.setIcon(icon1)
        self.expand_2.setIconSize(QSize(20, 25))
        self.expand_2.setFlat(True)

        self.horizontalLayout_6.addWidget(self.expand_2)

        self.minimize_2 = QPushButton(self.ControlButtons_2)
        self.minimize_2.setObjectName(u"minimize_2")
        self.minimize_2.setMinimumSize(QSize(20, 20))
        self.minimize_2.setMaximumSize(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u"C:/Downloads/minimize-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_2.setIcon(icon2)
        self.minimize_2.setIconSize(QSize(13, 16))
        self.minimize_2.setFlat(True)

        self.horizontalLayout_6.addWidget(self.minimize_2)


        self.horizontalLayout_4.addWidget(self.ControlButtons_2, 0, Qt.AlignLeft)

        self.Logo_2 = QFrame(self.header_2)
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

        self.horizontalLayout_7.addWidget(self.Learn_2)

        self.Loop_2 = QLabel(self.Logo_2)
        self.Loop_2.setObjectName(u"Loop_2")
        self.Loop_2.setFont(font)
        self.Loop_2.setStyleSheet(u"color: #E94560")

        self.horizontalLayout_7.addWidget(self.Loop_2)


        self.horizontalLayout_4.addWidget(self.Logo_2)

        self.ProfilePhotoAndSettings_2 = QFrame(self.header_2)
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
        icon3.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon4.addFile(u"C:/Desktop/59022631_810914472627047_3797622654492475392_n.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.profilePhoto_2.setIcon(icon4)
        self.profilePhoto_2.setIconSize(QSize(50, 45))
        self.profilePhoto_2.setAutoDefault(False)
        self.profilePhoto_2.setFlat(True)

        self.horizontalLayout_8.addWidget(self.profilePhoto_2)


        self.horizontalLayout_4.addWidget(self.ProfilePhotoAndSettings_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_2)

        self.mainPage = QFrame(self.centralwidget)
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setMinimumSize(QSize(0, 79))
        self.mainPage.setMaximumSize(QSize(16777215, 16777215))
        self.mainPage.setStyleSheet(u"background-color: #16213E;")
        self.mainPage.setFrameShape(QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.mainPage)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(0, 0))
        self.logo.setMaximumSize(QSize(16777215, 300))
        self.logo.setStyleSheet(u"background-color: 16213e\n"
"")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.logo)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.logo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setStyleSheet(u"position: absolute;\n"
"width: 232px;\n"
"height: 36px;\n"
"\n"
"font-family: 'Righteous';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 22px;\n"
"line-height: 27px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #FFFFFF")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.logo)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setStyleSheet(u"background-color: 16213e")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 35, -1)
        self.horizontalSpacer_3 = QSpacerItem(35, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(130, 0))
        self.label.setMaximumSize(QSize(130, 16777215))
        self.label.setStyleSheet(u"\n"
"position: absolute;\n"
"width: 194px;\n"
"height: 29px;\n"
"\n"
"font-family: 'Righteous';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 25px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #FFFFFF;")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(70, 0))
        self.pushButton.setMaximumSize(QSize(70, 16777215))
        self.pushButton.setStyleSheet(u"background-color: rgb(233, 69, 96);\n"
"position: absolute;\n"
"width: 194px;\n"
"height: 29px;\n"
"\n"
"font-family: 'Righteous';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 25px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #FFFFFF;")
        icon5 = QIcon()
        icon5.addFile(u"Data-Edit-256.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.logo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"background-color: #16213e")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(40, 0, 40, 0)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    border-style: solid;\n"
"    border-right-width: 0px;\n"
"    border-bottom-width:2px;\n"
"   border-top-width:0px;\n"
"   border-left-width:0px;\n"
"	background-color: rgb(22, 33, 62);\n"
"    \n"
"  \n"
"    border-bottom-color: rgba(255, 255, 255, 0.5);\n"
"   \n"
"\n"
"}\n"
"QTextEdit[placeholderText=\"Search....\"] {\n"
"    color:rgba(255, 255, 255, 0.5);  /* Set the color of the placeholder text */\n"
"     /* Set the font style of the placeholder text */\n"
"    font-size: 17px;\n"
"}")
        self.textEdit.setPlaceholderText(u"Search....")

        self.horizontalLayout_9.addWidget(self.textEdit)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.logo)

        self.frame_4 = QFrame(self.mainPage)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet(u"background-color:#0f3460;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.mainPage)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.settings_2.setDefault(False)
        self.profilePhoto_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.close_2.setText("")
        self.expand_2.setText("")
        self.minimize_2.setText("")
        self.Learn_2.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
        self.Loop_2.setText(QCoreApplication.translate("MainWindow", u"Loop", None))
#if QT_CONFIG(statustip)
        self.settings_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.settings_2.setText("")
        self.profilePhoto_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"1st \n"
" Computer And \n"
" Communication", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ECE 115", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
#if QT_CONFIG(whatsthis)
        self.textEdit.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>hfgfg</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

