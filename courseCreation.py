# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coursecreation.ui'
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
        self.Learn.setStyleSheet("color: white;\n"
"")
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
        self.Loop.setStyleSheet("color: #E94560;\n"
"")
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
        self.SecondHeader = QtWidgets.QFrame(self.mainPage)
        self.SecondHeader.setMaximumSize(QtCore.QSize(16777215, 53))
        self.SecondHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SecondHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SecondHeader.setObjectName("SecondHeader")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.SecondHeader)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.logo_2 = QtWidgets.QFrame(self.SecondHeader)
        self.logo_2.setMinimumSize(QtCore.QSize(675, 53))
        self.logo_2.setMaximumSize(QtCore.QSize(16777215, 53))
        self.logo_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.logo_2.setBaseSize(QtCore.QSize(0, 0))
        self.logo_2.setStyleSheet("  border-top-right-radius: 5px;\n"
"  border-bottom-right-radius: 5px;background: #E94560")
        self.logo_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_2.setObjectName("logo_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.logo_2)
        self.verticalLayout_16.setContentsMargins(0, 0, 110, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_14 = QtWidgets.QLabel(self.logo_2)
        self.label_14.setMinimumSize(QtCore.QSize(433, 34))
        self.label_14.setMaximumSize(QtCore.QSize(433, 37))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: #FFFFFF;\n"
"letter-spacing: 0.5px;\n"
"")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_16.addWidget(self.label_14, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_13.addWidget(self.logo_2)
        self.verticalLayout_9.addWidget(self.SecondHeader, 0, QtCore.Qt.AlignLeft)
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
        self.label_4.setMinimumSize(QtCore.QSize(144, 25))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 25))
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
        self.label_8.setMinimumSize(QtCore.QSize(395, 50))
        self.label_8.setMaximumSize(QtCore.QSize(395, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
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
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet(" border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"margin-top: 10px;\n"
"\n"
"")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_8.addWidget(self.lineEdit_8)
        self.label_5 = QtWidgets.QLabel(self.DOB_2)
        self.label_5.setMinimumSize(QtCore.QSize(395, 25))
        self.label_5.setMaximumSize(QtCore.QSize(395, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: #E94560;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.horizontalLayout_8.addWidget(self.DOB_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.frame_11, 0, QtCore.Qt.AlignHCenter)
        self.frame_8 = QtWidgets.QFrame(self.page)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_8.setStyleSheet("border: none;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_9.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_9.setStyleSheet("")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_15 = QtWidgets.QLabel(self.frame_9)
        self.label_15.setMinimumSize(QtCore.QSize(144, 22))
        self.label_15.setMaximumSize(QtCore.QSize(144, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("\n"
"color: #FFFFFF;")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_13.addWidget(self.label_15)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_9)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.setStyleSheet(" QComboBox {\n"
"        border-width: 2px; border-style: solid; border-color:white;border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"\n"
"    }\n"
"    QComboBox::hover {\n"
"    }\n"
"QComboBox QAbstractItemView { background-color: #0F3460; }\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_13.addWidget(self.comboBox_2)
        self.horizontalLayout_7.addWidget(self.frame_9)
        self.verticalLayout_10.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.page)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setContentsMargins(0, 20, 0, 0)
        self.horizontalLayout_12.setSpacing(50)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_4.setMinimumSize(QtCore.QSize(175, 38))
        self.pushButton_4.setMaximumSize(QtCore.QSize(175, 38))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("\n"
"letter-spacing: 0.5px;\n"
"\n"
"background: #E94560;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_12.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_5.setMinimumSize(QtCore.QSize(175, 38))
        self.pushButton_5.setMaximumSize(QtCore.QSize(175, 38))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("background: #E94560;\n"
"border-radius: 5px;\n"
"letter-spacing: 0.5px;\n"
"color: #FFFFFF;\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_12.addWidget(self.pushButton_5)
        self.verticalLayout_10.addWidget(self.frame_10, 0, QtCore.Qt.AlignHCenter)
        self.frame_12 = QtWidgets.QFrame(self.page)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_12.setStyleSheet("")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        self.label_6.setMinimumSize(QtCore.QSize(395, 25))
        self.label_6.setMaximumSize(QtCore.QSize(395, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"color: #E94560;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.frame_12, 0, QtCore.Qt.AlignHCenter)
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
        self.label_14.setText(_translate("MainWindow", "Course Creation"))
        self.label_4.setText(_translate("MainWindow", "Course Name"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "ECE 115"))
        self.label_8.setText(_translate("MainWindow", "Course Name must contain Capital English letters and digits only "))
        self.label_11.setText(_translate("MainWindow", "Number Of Hours"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "115"))
        self.label_5.setText(_translate("MainWindow", "Number of Hours must contain Digits only "))
        self.label_15.setText(_translate("MainWindow", "Term"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "First"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Second"))
        self.pushButton_4.setText(_translate("MainWindow", "Create"))
        self.pushButton_5.setText(_translate("MainWindow", "Cancel"))
        self.label_6.setText(_translate("MainWindow", "There is another Course with The Same Name"))

import Images_rc