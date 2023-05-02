# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentaddition.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 770)
        MainWindow.setMinimumSize(QtCore.QSize(880, 770))
        MainWindow.setStyleSheet("background:  #16213E")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_2 = QtWidgets.QFrame(self.centralwidget)
        self.header_2.setMinimumSize(QtCore.QSize(0, 50))
        self.header_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header_2.setStyleSheet("background: #0F3460")
        self.header_2.setObjectName("header_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_2)
        self.horizontalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ControlButtons_2 = QtWidgets.QFrame(self.header_2)
        self.ControlButtons_2.setObjectName("ControlButtons_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.ControlButtons_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.close_2 = QtWidgets.QPushButton(self.ControlButtons_2)
        self.close_2.setMinimumSize(QtCore.QSize(20, 0))
        self.close_2.setMaximumSize(QtCore.QSize(20, 16777215))
        self.close_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_2.setIcon(icon)
        self.close_2.setIconSize(QtCore.QSize(13, 16))
        self.close_2.setFlat(True)
        self.close_2.setObjectName("close_2")
        self.horizontalLayout_6.addWidget(self.close_2)
        self.expand_2 = QtWidgets.QPushButton(self.ControlButtons_2)
        self.expand_2.setMinimumSize(QtCore.QSize(20, 25))
        self.expand_2.setMaximumSize(QtCore.QSize(20, 25))
        self.expand_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Downloads/expand-arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expand_2.setIcon(icon1)
        self.expand_2.setIconSize(QtCore.QSize(20, 25))
        self.expand_2.setFlat(True)
        self.expand_2.setObjectName("expand_2")
        self.horizontalLayout_6.addWidget(self.expand_2)
        self.minimize_2 = QtWidgets.QPushButton(self.ControlButtons_2)
        self.minimize_2.setMinimumSize(QtCore.QSize(20, 20))
        self.minimize_2.setMaximumSize(QtCore.QSize(20, 20))
        self.minimize_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../Downloads/minimize-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_2.setIcon(icon2)
        self.minimize_2.setIconSize(QtCore.QSize(13, 16))
        self.minimize_2.setFlat(True)
        self.minimize_2.setObjectName("minimize_2")
        self.horizontalLayout_6.addWidget(self.minimize_2)
        self.horizontalLayout_4.addWidget(self.ControlButtons_2, 0, QtCore.Qt.AlignLeft)
        self.Logo_2 = QtWidgets.QFrame(self.header_2)
        self.Logo_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Logo_2.setObjectName("Logo_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Logo_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Learn_2 = QtWidgets.QLabel(self.Logo_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Learn_2.setFont(font)
        self.Learn_2.setStyleSheet("color: white")
        self.Learn_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Learn_2.setWordWrap(False)
        self.Learn_2.setObjectName("Learn_2")
        self.horizontalLayout_7.addWidget(self.Learn_2)
        self.Loop_2 = QtWidgets.QLabel(self.Logo_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Loop_2.setFont(font)
        self.Loop_2.setStyleSheet("color: #E94560")
        self.Loop_2.setObjectName("Loop_2")
        self.horizontalLayout_7.addWidget(self.Loop_2)
        self.horizontalLayout_4.addWidget(self.Logo_2)
        self.ProfilePhotoAndSettings_2 = QtWidgets.QFrame(self.header_2)
        self.ProfilePhotoAndSettings_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ProfilePhotoAndSettings_2.setObjectName("ProfilePhotoAndSettings_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.ProfilePhotoAndSettings_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.settings_2 = QtWidgets.QPushButton(self.ProfilePhotoAndSettings_2)
        self.settings_2.setMinimumSize(QtCore.QSize(45, 50))
        self.settings_2.setMaximumSize(QtCore.QSize(45, 50))
        self.settings_2.setStatusTip("")
        self.settings_2.setStyleSheet("background-color: #E94560;\n"
"border-style: outset")
        self.settings_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../Downloads/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_2.setIcon(icon3)
        self.settings_2.setIconSize(QtCore.QSize(30, 30))
        self.settings_2.setCheckable(False)
        self.settings_2.setAutoRepeat(False)
        self.settings_2.setAutoExclusive(False)
        self.settings_2.setAutoDefault(False)
        self.settings_2.setDefault(False)
        self.settings_2.setFlat(True)
        self.settings_2.setObjectName("settings_2")
        self.horizontalLayout_8.addWidget(self.settings_2)
        self.profilePhoto_2 = QtWidgets.QPushButton(self.ProfilePhotoAndSettings_2)
        self.profilePhoto_2.setMinimumSize(QtCore.QSize(50, 50))
        self.profilePhoto_2.setMaximumSize(QtCore.QSize(50, 50))
        self.profilePhoto_2.setAutoFillBackground(False)
        self.profilePhoto_2.setStyleSheet("")
        self.profilePhoto_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../Desktop/59022631_810914472627047_3797622654492475392_n.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profilePhoto_2.setIcon(icon4)
        self.profilePhoto_2.setIconSize(QtCore.QSize(50, 45))
        self.profilePhoto_2.setAutoDefault(False)
        self.profilePhoto_2.setDefault(False)
        self.profilePhoto_2.setFlat(True)
        self.profilePhoto_2.setObjectName("profilePhoto_2")
        self.horizontalLayout_8.addWidget(self.profilePhoto_2)
        self.horizontalLayout_4.addWidget(self.ProfilePhotoAndSettings_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.header_2)
        self.mainPage = QtWidgets.QFrame(self.centralwidget)
        self.mainPage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPage.setStyleSheet("background-color: #16213E;")
        self.mainPage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPage.setObjectName("mainPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.logo = QtWidgets.QFrame(self.mainPage)
        self.logo.setMinimumSize(QtCore.QSize(0, 53))
        self.logo.setMaximumSize(QtCore.QSize(608, 16777215))
        self.logo.setStyleSheet("\n"
"position: absolute;\n"
"width: 608px;\n"
"height: 53px;\n"
"\n"
"background: #E94560")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.logo)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.logo)
        self.label_12.setMinimumSize(QtCore.QSize(433, 34))
        self.label_12.setMaximumSize(QtCore.QSize(433, 37))
        self.label_12.setStyleSheet("position: absolute;\n"
"width: 433px;\n"
"height: 34px;\n"
"\n"
"font-family: \'Righteous\';\n"
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
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.First_secondname = QtWidgets.QFrame(self.mainPage)
        self.First_secondname.setMinimumSize(QtCore.QSize(0, 118))
        self.First_secondname.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.First_secondname.setStyleSheet("")
        self.First_secondname.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.First_secondname.setFrameShadow(QtWidgets.QFrame.Raised)
        self.First_secondname.setObjectName("First_secondname")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.First_secondname)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(56)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(164, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.frame = QtWidgets.QFrame(self.First_secondname)
        self.frame.setMinimumSize(QtCore.QSize(0, 118))
        self.frame.setMaximumSize(QtCore.QSize(243, 118))
        self.frame.setStyleSheet("background-color:#16213E;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(144, 22))
        self.label_2.setMaximumSize(QtCore.QSize(144, 22))
        self.label_2.setStyleSheet("position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(243, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_3.setStyleSheet(" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(240, 30))
        self.label_5.setMaximumSize(QtCore.QSize(240, 34))
        self.label_5.setStyleSheet("position: absolute;\n"
"width: 240px;\n"
"height: 25px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout.addWidget(self.frame)
        self.firstname = QtWidgets.QFrame(self.First_secondname)
        self.firstname.setMinimumSize(QtCore.QSize(0, 118))
        self.firstname.setMaximumSize(QtCore.QSize(243, 118))
        self.firstname.setStyleSheet("\n"
"\n"
"background: #16213E;;")
        self.firstname.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.firstname.setFrameShadow(QtWidgets.QFrame.Raised)
        self.firstname.setObjectName("firstname")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.firstname)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.firstname)
        self.label_4.setMinimumSize(QtCore.QSize(144, 22))
        self.label_4.setMaximumSize(QtCore.QSize(144, 22))
        self.label_4.setStyleSheet("position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.firstname)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(243, 0))
        self.lineEdit_4.setStyleSheet(" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.firstname)
        self.label_6.setMinimumSize(QtCore.QSize(240, 30))
        self.label_6.setMaximumSize(QtCore.QSize(240, 34))
        self.label_6.setStyleSheet("position: absolute;\n"
"width: 240px;\n"
"height: 25px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.horizontalLayout.addWidget(self.firstname)
        spacerItem3 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.First_secondname)
        self.phone_ID = QtWidgets.QFrame(self.mainPage)
        self.phone_ID.setMinimumSize(QtCore.QSize(0, 116))
        self.phone_ID.setMaximumSize(QtCore.QSize(16777215, 116))
        self.phone_ID.setStyleSheet("background: #16213E;")
        self.phone_ID.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.phone_ID.setFrameShadow(QtWidgets.QFrame.Raised)
        self.phone_ID.setObjectName("phone_ID")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.phone_ID)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(56)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(164, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.phonenum = QtWidgets.QFrame(self.phone_ID)
        self.phonenum.setMaximumSize(QtCore.QSize(243, 118))
        self.phonenum.setStyleSheet("background: #16213E;")
        self.phonenum.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.phonenum.setFrameShadow(QtWidgets.QFrame.Raised)
        self.phonenum.setObjectName("phonenum")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.phonenum)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.phonenum)
        self.label_3.setMinimumSize(QtCore.QSize(144, 22))
        self.label_3.setMaximumSize(QtCore.QSize(144, 22))
        self.label_3.setStyleSheet("position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.phonenum)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(243, 0))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_5.setStyleSheet(" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_3.addWidget(self.lineEdit_5)
        self.label_7 = QtWidgets.QLabel(self.phonenum)
        self.label_7.setMinimumSize(QtCore.QSize(240, 20))
        self.label_7.setMaximumSize(QtCore.QSize(240, 20))
        self.label_7.setStyleSheet("position: absolute;\n"
"width: 240px;\n"
"height: 25px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_2.addWidget(self.phonenum)
        self.frame_2 = QtWidgets.QFrame(self.phone_ID)
        self.frame_2.setMaximumSize(QtCore.QSize(243, 118))
        self.frame_2.setStyleSheet("background: #16213E;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setMinimumSize(QtCore.QSize(144, 22))
        self.label_8.setMaximumSize(QtCore.QSize(144, 22))
        self.label_8.setStyleSheet("position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(243, 0))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_6.setStyleSheet(" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_7.addWidget(self.lineEdit_6)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setMinimumSize(QtCore.QSize(240, 20))
        self.label_9.setMaximumSize(QtCore.QSize(240, 20))
        self.label_9.setStyleSheet("position: absolute;\n"
"width: 240px;\n"
"height: 25px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.horizontalLayout_2.addWidget(self.frame_2)
        spacerItem5 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.phone_ID)
        self.signin = QtWidgets.QFrame(self.mainPage)
        self.signin.setMinimumSize(QtCore.QSize(0, 0))
        self.signin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.signin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signin.setObjectName("signin")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.signin)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(56)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2.addWidget(self.signin)
        self.frame_3 = QtWidgets.QFrame(self.mainPage)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_3.setStyleSheet("background: #16213E;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(56)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(164, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.DOB = QtWidgets.QFrame(self.frame_3)
        self.DOB.setMaximumSize(QtCore.QSize(243, 116))
        self.DOB.setStyleSheet("background: #16213E;")
        self.DOB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DOB.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DOB.setObjectName("DOB")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.DOB)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.DOB)
        self.label_10.setMinimumSize(QtCore.QSize(144, 22))
        self.label_10.setMaximumSize(QtCore.QSize(144, 22))
        self.label_10.setStyleSheet("position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.DOB)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(243, 0))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_7.setStyleSheet(" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_8.addWidget(self.lineEdit_7)
        self.horizontalLayout_3.addWidget(self.DOB)
        self.Gender = QtWidgets.QFrame(self.frame_3)
        self.Gender.setMaximumSize(QtCore.QSize(243, 116))
        self.Gender.setStyleSheet("background: #16213E;")
        self.Gender.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Gender.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Gender.setObjectName("Gender")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Gender)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.Gender)
        self.label_11.setMinimumSize(QtCore.QSize(144, 22))
        self.label_11.setMaximumSize(QtCore.QSize(144, 22))
        self.label_11.setStyleSheet("position: absolute;\n"
"width: 144px;\n"
"height: 22px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.Gender)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(243, 0))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_9.setStyleSheet(" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_10.addWidget(self.lineEdit_9)
        self.horizontalLayout_3.addWidget(self.Gender)
        spacerItem7 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.mainPage)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_4.setStyleSheet("background: #16213E;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(545, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(545, 16777215))
        self.frame_5.setStyleSheet("background: #16213E;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setMinimumSize(QtCore.QSize(144, 22))
        self.label_13.setMaximumSize(QtCore.QSize(144, 22))
        self.label_13.setStyleSheet("position: absolute;\n"
"width: 322.96px;\n"
"height: 22px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label_13.setObjectName("label_13")
        self.verticalLayout_11.addWidget(self.label_13)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(545, 0))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_10.setStyleSheet(" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_11.addWidget(self.lineEdit_10)
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.mainPage)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_6.setStyleSheet("background: #16213E;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(45)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem8 = QtWidgets.QSpacerItem(164, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setMinimumSize(QtCore.QSize(175, 38))
        self.pushButton_2.setMaximumSize(QtCore.QSize(175, 38))
        self.pushButton_2.setStyleSheet("\n"
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
"font-family: \'Righteous\';\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setMinimumSize(QtCore.QSize(175, 38))
        self.pushButton_3.setMaximumSize(QtCore.QSize(175, 38))
        self.pushButton_3.setStyleSheet("\n"
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
"font-family: \'Righteous\';\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3)
        spacerItem9 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.mainPage)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_7.setStyleSheet("background: #16213E;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setMinimumSize(QtCore.QSize(395, 15))
        self.label.setMaximumSize(QtCore.QSize(395, 15))
        self.label.setStyleSheet("position: absolute;\n"
"width: 395.01px;\n"
"height: 15.22px;\n"
"\n"
"font-family: \'Outfit\';\n"
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
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_7)
        spacerItem10 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.verticalLayout.addWidget(self.mainPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Learn_2.setText(_translate("MainWindow", "Learn"))
        self.Loop_2.setText(_translate("MainWindow", "Loop"))
        self.label_12.setText(_translate("MainWindow", "Student Addition"))
        self.label_2.setText(_translate("MainWindow", "First Name"))
        self.lineEdit_3.setText(_translate("MainWindow", "Name"))
        self.label_5.setText(_translate("MainWindow", "First Name must contain English letters only "))
        self.label_4.setText(_translate("MainWindow", "Last Name"))
        self.lineEdit_4.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Last Name must contain English letters only "))
        self.label_3.setText(_translate("MainWindow", "Phone Number"))
        self.lineEdit_5.setText(_translate("MainWindow", "01151239658"))
        self.label_7.setText(_translate("MainWindow", "Phone Number is Invalid"))
        self.label_8.setText(_translate("MainWindow", "ID"))
        self.lineEdit_6.setText(_translate("MainWindow", "33333333333333333"))
        self.label_9.setText(_translate("MainWindow", "ID is Invalid"))
        self.label_10.setText(_translate("MainWindow", "Birth Date"))
        self.lineEdit_7.setText(_translate("MainWindow", "11 / 5 / 2001"))
        self.label_11.setText(_translate("MainWindow", "Gender"))
        self.lineEdit_9.setText(_translate("MainWindow", "Male"))
        self.label_13.setText(_translate("MainWindow", "E-Mail"))
        self.lineEdit_10.setText(_translate("MainWindow", "Name@@learnloop.edu.eg"))
        self.pushButton_2.setText(_translate("MainWindow", "Update"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))
        self.label.setText(_translate("MainWindow", "There is another Student with the same ID "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

