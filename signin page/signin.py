# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign.ui'
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
        self.verticalLayout.setSpacing(50)
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
        spacerItem = QtWidgets.QSpacerItem(20, 112, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.logo = QtWidgets.QFrame(self.mainPage)
        self.logo.setMinimumSize(QtCore.QSize(0, 0))
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.logo)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Learn_3 = QtWidgets.QLabel(self.logo)
        font = QtGui.QFont()
        font.setFamily("Fugaz One")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Learn_3.setFont(font)
        self.Learn_3.setStyleSheet("position: absolute;\n"
"width: 259px;\n"
"height: 35.2px;\n"
"\n"
"font-family: \'Fugaz One\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 40px;\n"
"line-height: 59px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.Learn_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Learn_3.setWordWrap(False)
        self.Learn_3.setObjectName("Learn_3")
        self.horizontalLayout_10.addWidget(self.Learn_3)
        self.Loop_3 = QtWidgets.QLabel(self.logo)
        font = QtGui.QFont()
        font.setFamily("Fugaz One")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Loop_3.setFont(font)
        self.Loop_3.setStyleSheet("position: absolute;\n"
"width: 259px;\n"
"height: 35.2px;\n"
"\n"
"font-family: \'Fugaz One\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 40px;\n"
"line-height: 59px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #E94560;")
        self.Loop_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Loop_3.setObjectName("Loop_3")
        self.horizontalLayout_10.addWidget(self.Loop_3)
        self.verticalLayout_2.addWidget(self.logo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.collagelabel = QtWidgets.QFrame(self.mainPage)
        self.collagelabel.setMinimumSize(QtCore.QSize(0, 30))
        self.collagelabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.collagelabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.collagelabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.collagelabel.setObjectName("collagelabel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.collagelabel)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.collagelabel)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setStyleSheet("\n"
"position: absolute;\n"
"width: 205px;\n"
"height: 17.6px;\n"
"\n"
"font-family: \'Fugaz One\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"line-height: 21px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"letter-spacing: 0.51em;\n"
"\n"
"color: #BBBBBB;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.collagelabel)
        spacerItem3 = QtWidgets.QSpacerItem(20, 160, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.input = QtWidgets.QFrame(self.mainPage)
        self.input.setMinimumSize(QtCore.QSize(0, 200))
        self.input.setMaximumSize(QtCore.QSize(16777215, 200))
        self.input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input.setObjectName("input")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.input)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.lineEdit = QtWidgets.QLineEdit(self.input)
        self.lineEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit.setStyleSheet(" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.input)
        self.label.setMinimumSize(QtCore.QSize(400, 0))
        self.label.setMaximumSize(QtCore.QSize(400, 25))
        self.label.setStyleSheet("position: absolute;\n"
"width: 305px;\n"
"height: 15.4px;\n"
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
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.input)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_2.setStyleSheet(" border-width: 3px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"QLineEdit::placeholderr {\n"
"    color:white;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.input)
        self.label_3.setMinimumSize(QtCore.QSize(400, 0))
        self.label_3.setMaximumSize(QtCore.QSize(400, 25))
        self.label_3.setStyleSheet("position: absolute;\n"
"width: 305px;\n"
"height: 15.4px;\n"
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
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.verticalLayout_2.addWidget(self.input)
        self.signin = QtWidgets.QFrame(self.mainPage)
        self.signin.setMinimumSize(QtCore.QSize(0, 0))
        self.signin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.signin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signin.setObjectName("signin")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.signin)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(24)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.signin)
        self.pushButton.setMinimumSize(QtCore.QSize(400, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pushButton.setStyleSheet("position: absolute;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"width: 305px;\n"
"height: 38.5px;\n"
"\n"
"background: #E94560;\n"
"border-radius: 8px;\n"
"\n"
"\n"
"position: absolute;\n"
"width: 305px;\n"
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
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.signin)
        spacerItem7 = QtWidgets.QSpacerItem(20, 128, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addWidget(self.mainPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Learn_2.setText(_translate("MainWindow", "Learn"))
        self.Loop_2.setText(_translate("MainWindow", "Loop"))
        self.Learn_3.setText(_translate("MainWindow", "Learn"))
        self.Loop_3.setText(_translate("MainWindow", "Loop"))
        self.label_2.setText(_translate("MainWindow", "Collage Project"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "E-mail"))
        self.label.setText(_translate("MainWindow", "E-mail is Invalid"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Password is incorrect"))
        self.pushButton.setText(_translate("MainWindow", "Sign in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

