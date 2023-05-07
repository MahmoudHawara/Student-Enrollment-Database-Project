# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentProfileFromStudent.ui'
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
        self.profilePhoto_2 = QPushButton(self.ProfilePhotoAndSettings_2)
        self.profilePhoto_2.setObjectName(u"profilePhoto_2")
        self.profilePhoto_2.setMinimumSize(QSize(35, 35))
        self.profilePhoto_2.setMaximumSize(QSize(35, 35))
        self.profilePhoto_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.profilePhoto_2.setAutoFillBackground(False)
        self.profilePhoto_2.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/Controles/Images/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profilePhoto_2.setIcon(icon3)
        self.profilePhoto_2.setIconSize(QSize(35, 35))
        self.profilePhoto_2.setAutoDefault(False)
        self.profilePhoto_2.setFlat(True)

        self.horizontalLayout_8.addWidget(self.profilePhoto_2)


        self.horizontalLayout_4.addWidget(self.ProfilePhotoAndSettings_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.mainPage = QFrame(self.centralwidget)
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setMaximumSize(QSize(16777215, 16777215))
        self.mainPage.setStyleSheet(u"border: none;")
        self.mainPage.setFrameShape(QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.mainPage)
        self.verticalLayout_9.setSpacing(85)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.frame = QFrame(self.mainPage)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(65, 125))
        self.frame_5.setMaximumSize(QSize(65, 100))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.line_7 = QFrame(self.frame_5)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(0, 60, 3, 60))
        self.line_7.setMinimumSize(QSize(0, 60))
        self.line_7.setMaximumSize(QSize(16777215, 60))
        self.line_7.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.frame_5)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(0, 120, 60, 3))
        self.line_8.setMinimumSize(QSize(60, 0))
        self.line_8.setMaximumSize(QSize(60, 16777215))
        self.line_8.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.frame_5)

        self.department = QFrame(self.frame)
        self.department.setObjectName(u"department")
        self.department.setMinimumSize(QSize(0, 100))
        self.department.setMaximumSize(QSize(750, 100))
        self.department.setStyleSheet(u"color: white;")
        self.department.setFrameShape(QFrame.StyledPanel)
        self.department.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.department)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.department)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Condensed")
        font1.setPointSize(25)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_14.setFont(font1)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.department)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_19.setSpacing(20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 45))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiBold")
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: #E94560")
        self.label_9.setLineWidth(5)

        self.horizontalLayout_19.addWidget(self.label_9, 0, Qt.AlignRight|Qt.AlignBottom)

        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setFrameShadow(QFrame.Plain)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setIndent(-1)

        self.horizontalLayout_19.addWidget(self.label_10, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_17, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.department, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(65, 125))
        self.frame_4.setMaximumSize(QSize(65, 125))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(60, 0, 3, 60))
        self.line_3.setMinimumSize(QSize(0, 60))
        self.line_3.setMaximumSize(QSize(16777215, 60))
        self.line_3.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.frame_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 0, 60, 3))
        self.line_4.setMinimumSize(QSize(60, 0))
        self.line_4.setMaximumSize(QSize(60, 16777215))
        self.line_4.setStyleSheet(u"border: 1.5px solid #E94560;")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.frame_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addWidget(self.frame)

        self.photo = QFrame(self.mainPage)
        self.photo.setObjectName(u"photo")
        self.photo.setMinimumSize(QSize(200, 200))
        self.photo.setMaximumSize(QSize(200, 200))
        self.photo.setStyleSheet(u"")
        self.photo.setFrameShape(QFrame.StyledPanel)
        self.photo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.photo)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.photo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 200))
        self.label_4.setMaximumSize(QSize(200, 200))
        self.label_4.setPixmap(QPixmap(u":/Controles/Images/user.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_4)


        self.verticalLayout_9.addWidget(self.photo, 0, Qt.AlignHCenter)

        self.buttons = QFrame(self.mainPage)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(0, 150))
        self.buttons.setMaximumSize(QSize(16777215, 150))
        self.buttons.setStyleSheet(u"")
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttons)
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.buttons)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 145))
        self.frame_6.setMaximumSize(QSize(200, 150))
        self.frame_6.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 0.5px;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Condensed")
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_11.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(75, 28))
        self.pushButton_3.setMaximumSize(QSize(75, 28))
        self.pushButton_3.setSizeIncrement(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift Condensed")
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setWeight(50)
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background: #E94560;\n"
"border-radius: 3px;\n"
"\n"
"\n"
"")

        self.verticalLayout_6.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.buttons)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 145))
        self.frame_3.setMaximumSize(QSize(200, 150))
        self.frame_3.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 0.5px;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(75, 28))
        self.pushButton_2.setMaximumSize(QSize(75, 28))
        self.pushButton_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background: #E94560;\n"
"border-radius: 3px;\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_9.addWidget(self.buttons, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


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
        self.Learn_2.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
        self.Loop_2.setText(QCoreApplication.translate("MainWindow", u"Loop", None))
        self.profilePhoto_2.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Mahmoud Hawara", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.label_4.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Personal", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MY", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Courses", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow =QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())