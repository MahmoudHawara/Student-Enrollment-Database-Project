# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'course.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
# from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QColor
from PySide2.QtSql import QSqlDatabase, QSqlQuery
import Images_rc


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                if not MainWindow.objectName():
                        MainWindow.setObjectName(u"MainWindow")
                MainWindow.resize(937, 818)
                MainWindow.setMinimumSize(QtCore.QSize(880, 770))
                MainWindow.setStyleSheet("background:  #16213E")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setSpacing(20)
                self.verticalLayout.setObjectName("verticalLayout")
                self.header = QtWidgets.QFrame(self.centralwidget)
                self.header.setMinimumSize(QtCore.QSize(0, 50))
                self.header.setMaximumSize(QtCore.QSize(16777215, 50))
                self.header.setStyleSheet("background: #0F3460")
                self.header.setObjectName("header")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header)
                self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_4.setSpacing(0)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.ControlButtons_2 = QtWidgets.QFrame(self.header)
                self.ControlButtons_2.setObjectName("ControlButtons_2")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.ControlButtons_2)
                self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_6.setSpacing(15)
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.close = QtWidgets.QPushButton(self.ControlButtons_2)
                self.close.setMinimumSize(QtCore.QSize(20, 0))
                self.close.setMaximumSize(QtCore.QSize(20, 16777215))
                self.close.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("Images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.close.setIcon(icon)
                self.close.setIconSize(QtCore.QSize(13, 16))
                self.close.setFlat(True)
                self.close.setObjectName("close")
                self.horizontalLayout_6.addWidget(self.close)
                self.expand = QtWidgets.QPushButton(self.ControlButtons_2)
                self.expand.setMinimumSize(QtCore.QSize(20, 25))
                self.expand.setMaximumSize(QtCore.QSize(20, 25))
                self.expand.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("Images/expand-arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.expand.setIcon(icon1)
                self.expand.setIconSize(QtCore.QSize(20, 25))
                self.expand.setFlat(True)
                self.expand.setObjectName("expand")
                self.horizontalLayout_6.addWidget(self.expand)
                self.minimize = QtWidgets.QPushButton(self.ControlButtons_2)
                self.minimize.setMinimumSize(QtCore.QSize(20, 20))
                self.minimize.setMaximumSize(QtCore.QSize(20, 20))
                self.minimize.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("minimize-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.minimize.setIcon(icon2)
                self.minimize.setIconSize(QtCore.QSize(13, 16))
                self.minimize.setFlat(True)
                self.minimize.setObjectName("minimize")
                self.horizontalLayout_6.addWidget(self.minimize)
                self.horizontalLayout_4.addWidget(self.ControlButtons_2, 0, QtCore.Qt.AlignLeft)
                self.Logo_2 = QtWidgets.QFrame(self.header)
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
                self.ProfilePhotoAndSettings_2 = QtWidgets.QFrame(self.header)
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
                icon3.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
                icon4.addPixmap(QtGui.QPixmap("C:/Desktop/59022631_810914472627047_3797622654492475392_n.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.profilePhoto_2.setIcon(icon4)
                self.profilePhoto_2.setIconSize(QtCore.QSize(50, 45))
                self.profilePhoto_2.setAutoDefault(False)
                self.profilePhoto_2.setDefault(False)
                self.profilePhoto_2.setFlat(True)
                self.profilePhoto_2.setObjectName("profilePhoto_2")
                self.horizontalLayout_8.addWidget(self.profilePhoto_2)
                self.horizontalLayout_4.addWidget(self.ProfilePhotoAndSettings_2, 0, QtCore.Qt.AlignRight)
                self.verticalLayout.addWidget(self.header)
                self.mainPage = QtWidgets.QFrame(self.centralwidget)
                self.mainPage.setMinimumSize(QtCore.QSize(0, 79))
                self.mainPage.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.mainPage.setStyleSheet("background-color: #16213E;")
                self.mainPage.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.mainPage.setFrameShadow(QtWidgets.QFrame.Raised)
                self.mainPage.setObjectName("mainPage")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainPage)
                self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.logo = QtWidgets.QFrame(self.mainPage)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
                self.logo.setSizePolicy(sizePolicy)
                self.logo.setMinimumSize(QtCore.QSize(0, 0))
                self.logo.setMaximumSize(QtCore.QSize(16777215, 300))
                self.logo.setStyleSheet("background-color: 16213e\n"
        "")
                self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
                self.logo.setObjectName("logo")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.logo)
                self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_3.setSpacing(0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.frame_3 = QtWidgets.QFrame(self.logo)
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.label_2 = QtWidgets.QLabel(self.frame_3)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
                self.label_2.setSizePolicy(sizePolicy)
                self.label_2.setMinimumSize(QtCore.QSize(0, 0))
                self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.label_2.setStyleSheet("position: absolute;\n"
        "width: 232px;\n"
        "height: 36px;\n"
        "\n"
        "font-family: \'Righteous\';\n"
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
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setObjectName("label_2")
                self.verticalLayout_4.addWidget(self.label_2)
                spacerItem = QtWidgets.QSpacerItem(20, 101, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_4.addItem(spacerItem)
                self.verticalLayout_3.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
                self.frame = QtWidgets.QFrame(self.logo)
                self.frame.setMinimumSize(QtCore.QSize(0, 0))
                self.frame.setMaximumSize(QtCore.QSize(16777215, 80))
                self.frame.setStyleSheet("background-color: 16213e")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
                self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_5.setSpacing(0)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_3.setContentsMargins(10, -1, 35, -1)
                self.horizontalLayout_3.setSpacing(7)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_3.addItem(spacerItem1)
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setMinimumSize(QtCore.QSize(130, 0))
                self.label.setMaximumSize(QtCore.QSize(130, 16777215))
                self.label.setStyleSheet("\n"
        "position: absolute;\n"
        "width: 194px;\n"
        "height: 29px;\n"
        "\n"
        "font-family: \'Righteous\';\n"
        "font-style: normal;\n"
        "font-weight: 400;\n"
        "font-size: 20px;\n"
        "line-height: 25px;\n"
        "display: flex;\n"
        "align-items: center;\n"
        "\n"
        "color: #FFFFFF;")
                self.label.setObjectName("label")
                self.horizontalLayout_3.addWidget(self.label)
                spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_3.addItem(spacerItem2)
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
                self.pushButton = QtWidgets.QPushButton(self.frame)
                self.pushButton.setMinimumSize(QtCore.QSize(70, 0))
                self.pushButton.setMaximumSize(QtCore.QSize(70, 16777215))
                self.pushButton.setStyleSheet("background-color: rgb(233, 69, 96);\n"
        "position: absolute;\n"
        "width: 194px;\n"
        "height: 29px;\n"
        "\n"
        "font-family: \'Righteous\';\n"
        "font-style: normal;\n"
        "font-weight: 400;\n"
        "font-size: 20px;\n"
        "line-height: 25px;\n"
        "display: flex;\n"
        "align-items: center;\n"
        "\n"
        "color: #FFFFFF;")
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap("Data-Edit-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushButton.setIcon(icon5)
                self.pushButton.setObjectName("pushButton")
                self.horizontalLayout_3.addWidget(self.pushButton)
                spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_3.addItem(spacerItem3)
                self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
                self.verticalLayout_3.addWidget(self.frame)
                self.frame_2 = QtWidgets.QFrame(self.logo)
                self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
                self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
                self.frame_2.setStyleSheet("background-color: #16213e")
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
                self.horizontalLayout_9.setContentsMargins(40, 0, 40, 0)
                self.horizontalLayout_9.setSpacing(0)
                self.horizontalLayout_9.setObjectName("horizontalLayout_9")
                self.textEdit = QtWidgets.QTextEdit(self.frame_2)
                self.textEdit.setStyleSheet("QTextEdit {\n"
        "    border-style: solid;\n"
        "    border-right-width: 0px;\n"
        "    border-bottom-width:2px;\n"
        "   border-top-width:0px;\n"
        "   border-left-width:0px;\n"
        "    background-color: rgb(22, 33, 62);\n"
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
                self.textEdit.setPlaceholderText("Search....")
                self.textEdit.setObjectName("textEdit")
                self.horizontalLayout_9.addWidget(self.textEdit)
                self.verticalLayout_3.addWidget(self.frame_2)
                self.verticalLayout_2.addWidget(self.logo)
                self.frame_4 = QtWidgets.QFrame(self.mainPage)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
                self.frame_4.setSizePolicy(sizePolicy)
                self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
                self.frame_4.setAutoFillBackground(False)
                self.frame_4.setStyleSheet("background-color:#16213e;")
                self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_4.setObjectName("frame_4")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.table = QtWidgets.QTableWidget()
                self.verticalLayout_5.addWidget(self.table);
                self.verticalLayout_5.setAlignment(QtCore.Qt.AlignCenter);
                self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                self.table.autoFillBackground();
                # self.table.;
                # self.table.setMinimumWidth(self.table.width())
                # self.table.setMinimumHeight(self.table.height())
                print(self.frame_3.width());
                print(self.frame_3.height());
                self.table.setMaximumWidth(1200)
                self.table.setMaximumHeight(500)
                self.verticalLayout_2.addWidget(self.frame_4)
                self.verticalLayout.addWidget(self.mainPage)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.Learn_2.setText(_translate("MainWindow", "Learn"))
                self.Loop_2.setText(_translate("MainWindow", "Loop"))
                self.label_2.setText(_translate("MainWindow", "1st \n"
        " Computer And \n"
        " Communication"))
                self.label.setText(_translate("MainWindow", "students"))
                self.pushButton.setText(_translate("MainWindow", "New"))
                self.textEdit.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>hfgfg</p></body></html>"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())