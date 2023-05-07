# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signIn.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 880)
        MainWindow.setMinimumSize(QtCore.QSize(920, 880))
        MainWindow.setStyleSheet("background: #16213E;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 50))
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setStyleSheet("background: #0F3460")
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(10, 0, 20, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ControlButtons = QtWidgets.QFrame(self.header)
        self.ControlButtons.setObjectName("ControlButtons")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.ControlButtons)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.close = QtWidgets.QPushButton(self.ControlButtons)
        self.close.setMinimumSize(QtCore.QSize(20, 26))
        self.close.setMaximumSize(QtCore.QSize(26, 26))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("QPushButton::hover{\n"
"    background-color: #E94560;\n"
"    border-radius: 12px;\n"
"}")
        self.close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Controles/Images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setIconSize(QtCore.QSize(12, 14))
        self.close.setFlat(True)
        self.close.setObjectName("close")
        self.horizontalLayout_6.addWidget(self.close)
        self.expand = QtWidgets.QPushButton(self.ControlButtons)
        self.expand.setMinimumSize(QtCore.QSize(26, 26))
        self.expand.setMaximumSize(QtCore.QSize(26, 26))
        self.expand.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.expand.setStyleSheet("QPushButton::hover{\n"
"    background-color: #E94560;\n"
"    border-radius: 12px;\n"
"}")
        self.expand.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Controles/Images/expand-arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expand.setIcon(icon1)
        self.expand.setIconSize(QtCore.QSize(20, 25))
        self.expand.setFlat(True)
        self.expand.setObjectName("expand")
        self.horizontalLayout_6.addWidget(self.expand)
        self.minimize = QtWidgets.QPushButton(self.ControlButtons)
        self.minimize.setMinimumSize(QtCore.QSize(26, 26))
        self.minimize.setMaximumSize(QtCore.QSize(26, 26))
        self.minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize.setStyleSheet("QPushButton::hover{\n"
"    background-color: #E94560;\n"
"    border-radius: 12px;\n"
"}")
        self.minimize.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Controles/Images/minimize-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize.setIcon(icon2)
        self.minimize.setIconSize(QtCore.QSize(13, 16))
        self.minimize.setFlat(True)
        self.minimize.setObjectName("minimize")
        self.horizontalLayout_6.addWidget(self.minimize)
        self.horizontalLayout.addWidget(self.ControlButtons, 0, QtCore.Qt.AlignLeft)
        self.Logo = QtWidgets.QFrame(self.header)
        self.Logo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Logo.setObjectName("Logo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Logo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Learn = QtWidgets.QLabel(self.Logo)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Learn.setFont(font)
        self.Learn.setStyleSheet("color: white")
        self.Learn.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Learn.setWordWrap(False)
        self.Learn.setObjectName("Learn")
        self.horizontalLayout_2.addWidget(self.Learn)
        self.Loop = QtWidgets.QLabel(self.Logo)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Loop.setFont(font)
        self.Loop.setStyleSheet("color: #E94560")
        self.Loop.setObjectName("Loop")
        self.horizontalLayout_2.addWidget(self.Loop)
        self.horizontalLayout.addWidget(self.Logo)
        self.ProfilePhotoAndSettings = QtWidgets.QFrame(self.header)
        self.ProfilePhotoAndSettings.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ProfilePhotoAndSettings.setObjectName("ProfilePhotoAndSettings")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ProfilePhotoAndSettings)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout.addWidget(self.ProfilePhotoAndSettings, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.header)
        self.mainPage = QtWidgets.QFrame(self.centralwidget)
        self.mainPage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPage.setStyleSheet("border: none;")
        self.mainPage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPage.setObjectName("mainPage")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mainPage)
        self.verticalLayout_9.setContentsMargins(0, 80, 0, 0)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.page = QtWidgets.QFrame(self.mainPage)
        self.page.setMinimumSize(QtCore.QSize(0, 0))
        self.page.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.page.setSizeIncrement(QtCore.QSize(2, 0))
        self.page.setStyleSheet("")
        self.page.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page.setObjectName("page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.SecondHeader = QtWidgets.QFrame(self.page)
        self.SecondHeader.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.SecondHeader.setSizeIncrement(QtCore.QSize(0, 0))
        self.SecondHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SecondHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SecondHeader.setObjectName("SecondHeader")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SecondHeader)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 150)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo_2 = QtWidgets.QFrame(self.SecondHeader)
        self.logo_2.setMinimumSize(QtCore.QSize(650, 53))
        self.logo_2.setMaximumSize(QtCore.QSize(16777215, 53))
        self.logo_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.logo_2.setBaseSize(QtCore.QSize(0, 0))
        self.logo_2.setStyleSheet("")
        self.logo_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_2.setObjectName("logo_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.logo_2)
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Learn_2 = QtWidgets.QLabel(self.logo_2)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Learn_2.setFont(font)
        self.Learn_2.setStyleSheet("color: white;\n"
"letter-spacing: 0.7px;")
        self.Learn_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Learn_2.setWordWrap(False)
        self.Learn_2.setObjectName("Learn_2")
        self.horizontalLayout_3.addWidget(self.Learn_2)
        self.Loop_2 = QtWidgets.QLabel(self.logo_2)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Loop_2.setFont(font)
        self.Loop_2.setStyleSheet("color: #E94560;\n"
"letter-spacing: 1px;")
        self.Loop_2.setObjectName("Loop_2")
        self.horizontalLayout_3.addWidget(self.Loop_2)
        self.verticalLayout_2.addWidget(self.logo_2)
        self.label = QtWidgets.QLabel(self.SecondHeader)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(9)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#BBBBBB;\n"
"letter-spacing:7.4px;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.SecondHeader)
        self.phone_ID_2 = QtWidgets.QFrame(self.page)
        self.phone_ID_2.setMinimumSize(QtCore.QSize(0, 150))
        self.phone_ID_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.phone_ID_2.setStyleSheet("")
        self.phone_ID_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.phone_ID_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.phone_ID_2.setLineWidth(1)
        self.phone_ID_2.setObjectName("phone_ID_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.phone_ID_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.phonenum_2 = QtWidgets.QFrame(self.phone_ID_2)
        self.phonenum_2.setMinimumSize(QtCore.QSize(400, 150))
        self.phonenum_2.setMaximumSize(QtCore.QSize(400, 150))
        self.phonenum_2.setStyleSheet("")
        self.phonenum_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.phonenum_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.phonenum_2.setObjectName("phonenum_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.phonenum_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.phonenum_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 22))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color: #FFFFFF")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.phonenum_2)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(243, 50))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"margin-top: 10px;\n"
"")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_7.addWidget(self.lineEdit_6)
        self.label_8 = QtWidgets.QLabel(self.phonenum_2)
        self.label_8.setMinimumSize(QtCore.QSize(395, 28))
        self.label_8.setMaximumSize(QtCore.QSize(395, 35))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("\n"
"color: #E94560;")
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.verticalLayout_6.addWidget(self.phonenum_2)
        self.verticalLayout_10.addWidget(self.phone_ID_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_11 = QtWidgets.QFrame(self.page)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_11.setStyleSheet("")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.DOB_2 = QtWidgets.QFrame(self.frame_11)
        self.DOB_2.setMinimumSize(QtCore.QSize(0, 150))
        self.DOB_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.DOB_2.setStyleSheet("")
        self.DOB_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DOB_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DOB_2.setObjectName("DOB_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.DOB_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.DOB_2)
        self.label_11.setMinimumSize(QtCore.QSize(386, 22))
        self.label_11.setMaximumSize(QtCore.QSize(200, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("\n"
"color: #FFFFFF;")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.DOB_2)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(400, 50))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet(" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"letter-spacing: 5px;\n"
"margin-top: 10px;")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_8.addWidget(self.lineEdit_8)
        self.label_5 = QtWidgets.QLabel(self.DOB_2)
        self.label_5.setMinimumSize(QtCore.QSize(395, 17))
        self.label_5.setMaximumSize(QtCore.QSize(395, 17))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: #E94560;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.horizontalLayout_8.addWidget(self.DOB_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.frame_11, 0, QtCore.Qt.AlignHCenter)
        self.frame_10 = QtWidgets.QFrame(self.page)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(45)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_4.setMinimumSize(QtCore.QSize(400, 38))
        self.pushButton_4.setMaximumSize(QtCore.QSize(400, 38))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("\n"
"\n"
"background: #E94560;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_12.addWidget(self.pushButton_4)
        self.verticalLayout_10.addWidget(self.frame_10, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.verticalLayout_9.addWidget(self.page)
        self.verticalLayout.addWidget(self.mainPage)
        self.size_grip = QtWidgets.QFrame(self.centralwidget)
        self.size_grip.setMinimumSize(QtCore.QSize(0, 15))
        self.size_grip.setMaximumSize(QtCore.QSize(16777215, 15))
        self.size_grip.setStyleSheet("border: none;")
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.verticalLayout.addWidget(self.size_grip)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.close.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.expand.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.minimize.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.Learn.setText(_translate("MainWindow", "Learn"))
        self.Loop.setText(_translate("MainWindow", "Loop"))
        self.Learn_2.setText(_translate("MainWindow", "Learn"))
        self.Loop_2.setText(_translate("MainWindow", "Loop"))
        self.label.setText(_translate("MainWindow", "College Project"))
        self.label_4.setText(_translate("MainWindow", "E-Mail"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "someone123@learnloop.edu.eg"))
        self.label_8.setText(_translate("MainWindow", "E-Mail is Invalid"))
        self.label_11.setText(_translate("MainWindow", "Password"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "**********"))
        self.label_5.setText(_translate("MainWindow", "Password is Incorrect"))
        self.pushButton_4.setText(_translate("MainWindow", "Sign In"))
import Images_rc
