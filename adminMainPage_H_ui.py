# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminMainPage_H.ui'
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
        MainWindow.resize(880, 880)
        MainWindow.setMinimumSize(QSize(880, 880))
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
        self.close = QPushButton(self.ControlButtons_2)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(20, 26))
        self.close.setMaximumSize(QSize(26, 26))
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: #E94560;\n"
"	border-radius: 12px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"Images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon)
        self.close.setIconSize(QSize(12, 14))
        self.close.setFlat(True)

        self.horizontalLayout_6.addWidget(self.close)

        self.expand = QPushButton(self.ControlButtons_2)
        self.expand.setObjectName(u"expand")
        self.expand.setMinimumSize(QSize(26, 26))
        self.expand.setMaximumSize(QSize(26, 26))
        self.expand.setCursor(QCursor(Qt.PointingHandCursor))
        self.expand.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: #E94560;\n"
"	border-radius: 12px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Images/expand-arrows.png", QSize(), QIcon.Normal, QIcon.Off)
        self.expand.setIcon(icon1)
        self.expand.setIconSize(QSize(20, 25))
        self.expand.setFlat(True)

        self.horizontalLayout_6.addWidget(self.expand)

        self.minimize = QPushButton(self.ControlButtons_2)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(26, 26))
        self.minimize.setMaximumSize(QSize(26, 26))
        self.minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: #E94560;\n"
"	border-radius: 12px;\n"
"}")
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
        self.settings_2.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.profilePhoto_2.setMinimumSize(QSize(35, 35))
        self.profilePhoto_2.setMaximumSize(QSize(35, 35))
        self.profilePhoto_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.profilePhoto_2.setAutoFillBackground(False)
        self.profilePhoto_2.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"Images/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profilePhoto_2.setIcon(icon4)
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
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 40, 0, 0)
        self.buttons = QFrame(self.mainPage)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(0, 130))
        self.buttons.setMaximumSize(QSize(16777215, 130))
        self.buttons.setStyleSheet(u"")
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.groups = QFrame(self.buttons)
        self.groups.setObjectName(u"groups")
        self.groups.setMinimumSize(QSize(180, 100))
        self.groups.setMaximumSize(QSize(180, 100))
        self.groups.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 2px;")
        self.groups.setFrameShape(QFrame.StyledPanel)
        self.groups.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.groups)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.numOfGroups = QLabel(self.groups)
        self.numOfGroups.setObjectName(u"numOfGroups")
        font1 = QFont()
        font1.setFamily(u"Ubuntu Condensed")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.numOfGroups.setFont(font1)

        self.verticalLayout_3.addWidget(self.numOfGroups, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.groups)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.groups)

        self.courses = QFrame(self.buttons)
        self.courses.setObjectName(u"courses")
        self.courses.setMinimumSize(QSize(180, 100))
        self.courses.setMaximumSize(QSize(180, 100))
        self.courses.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 2px;")
        self.courses.setFrameShape(QFrame.StyledPanel)
        self.courses.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.courses)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.numOfCourses = QLabel(self.courses)
        self.numOfCourses.setObjectName(u"numOfCourses")
        self.numOfCourses.setFont(font1)

        self.verticalLayout_4.addWidget(self.numOfCourses, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.courses)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)


        self.horizontalLayout.addWidget(self.courses)

        self.students = QFrame(self.buttons)
        self.students.setObjectName(u"students")
        self.students.setMinimumSize(QSize(180, 100))
        self.students.setMaximumSize(QSize(180, 100))
        self.students.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 2px;")
        self.students.setFrameShape(QFrame.StyledPanel)
        self.students.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.students)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_13)

        self.numOfStudents = QLabel(self.students)
        self.numOfStudents.setObjectName(u"numOfStudents")
        self.numOfStudents.setFont(font1)

        self.verticalLayout_7.addWidget(self.numOfStudents, 0, Qt.AlignHCenter)

        self.label_14 = QLabel(self.students)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_14)


        self.horizontalLayout.addWidget(self.students)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.buttons)

        self.searchAndAdd = QFrame(self.mainPage)
        self.searchAndAdd.setObjectName(u"searchAndAdd")
        self.searchAndAdd.setMinimumSize(QSize(620, 0))
        self.searchAndAdd.setMaximumSize(QSize(680, 16777215))
        self.searchAndAdd.setStyleSheet(u"")
        self.searchAndAdd.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.searchAndAdd.setFrameShape(QFrame.StyledPanel)
        self.searchAndAdd.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.searchAndAdd)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.searchAndAdd)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(620, 35))
        self.frame.setMaximumSize(QSize(300, 35))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Ubuntu Condensed")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: white;\n"
"\n"
"letter-spacing: 1.5px;")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(75, 35))
        self.pushButton.setMaximumSize(QSize(75, 35))
        font3 = QFont()
        font3.setFamily(u"Ubuntu Condensed")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton.setFont(font3)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: #E94560;\n"
"border-style: outset;\n"
"border-radius: 3px;\n"
"color: white;")
        icon5 = QIcon()
        icon5.addFile(u"Images/plus2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_2 = QFrame(self.searchAndAdd)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(243, 50))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(14)
        self.lineEdit_6.setFont(font4)
        self.lineEdit_6.setStyleSheet(u" border-width: 2px; border-style: solid; border-color:#A9A9A9;\n"
"border-top-style:none;\n"
"border-left-style:none; border-right-style:none;\n"
"color: #A9A9A9;\n"
"padding-left: 5px;\n"
"letter-spacing: 1.5px;\n"
"")
        self.lineEdit_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_6)


        self.verticalLayout_8.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.searchAndAdd, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.mainPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_18.setSpacing(40)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(240, 150))
        self.frame_4.setMaximumSize(QSize(240, 150))
        self.frame_4.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 2px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setFamily(u"Ubuntu Condensed")
        font5.setPointSize(22)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_2.setFont(font5)
        self.label_2.setLineWidth(5)

        self.horizontalLayout_9.addWidget(self.label_2, 0, Qt.AlignRight|Qt.AlignBottom)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        font6 = QFont()
        font6.setFamily(u"Ubuntu Condensed")
        font6.setPointSize(15)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_3.setFont(font6)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setIndent(-1)

        self.horizontalLayout_9.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        font7 = QFont()
        font7.setFamily(u"Ubuntu Condensed")
        font7.setPointSize(18)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_9.setFont(font7)
        self.label_9.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 27))
        self.frame_5.setMaximumSize(QSize(16777215, 27))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(75, 27))
        self.pushButton_2.setMaximumSize(QSize(75, 27))
        self.pushButton_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background: #E94560;\n"
"border-radius: 2px;\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(75, 27))
        self.pushButton_3.setMaximumSize(QSize(75, 27))
        self.pushButton_3.setSizeIncrement(QSize(0, 0))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background: #E94560;\n"
"border-radius: 2px;\n"
"")

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.verticalLayout_5.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)


        self.horizontalLayout_18.addWidget(self.frame_4)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(240, 150))
        self.frame_10.setMaximumSize(QSize(240, 150))
        self.frame_10.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 2px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_17)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_13)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font5)
        self.label_17.setLineWidth(5)

        self.horizontalLayout_16.addWidget(self.label_17, 0, Qt.AlignRight|Qt.AlignBottom)

        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font6)
        self.label_18.setFrameShadow(QFrame.Plain)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setIndent(-1)

        self.horizontalLayout_16.addWidget(self.label_18, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_11.addWidget(self.frame_13)

        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font7)
        self.label_19.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 27))
        self.frame_16.setMaximumSize(QSize(16777215, 27))
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setSpacing(20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_16)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(75, 27))
        self.pushButton_10.setMaximumSize(QSize(75, 27))
        self.pushButton_10.setSizeIncrement(QSize(0, 0))
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"background: #E94560;\n"
"border-radius: 2px;\n"
"")

        self.horizontalLayout_17.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_16)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(75, 27))
        self.pushButton_11.setMaximumSize(QSize(75, 27))
        self.pushButton_11.setSizeIncrement(QSize(0, 0))
        self.pushButton_11.setFont(font2)
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"background: #E94560;\n"
"border-radius: 2px;\n"
"")

        self.horizontalLayout_17.addWidget(self.pushButton_11)


        self.verticalLayout_11.addWidget(self.frame_16, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_18)


        self.horizontalLayout_18.addWidget(self.frame_10)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(240, 150))
        self.frame_7.setMaximumSize(QSize(240, 150))
        self.frame_7.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 2px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_9)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setLineWidth(5)

        self.horizontalLayout_10.addWidget(self.label_4, 0, Qt.AlignRight|Qt.AlignBottom)

        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)
        self.label_5.setFrameShadow(QFrame.Plain)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setIndent(-1)

        self.horizontalLayout_10.addWidget(self.label_5, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)
        self.label_10.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 27))
        self.frame_9.setMaximumSize(QSize(16777215, 27))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_9)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(75, 27))
        self.pushButton_4.setMaximumSize(QSize(75, 27))
        self.pushButton_4.setSizeIncrement(QSize(0, 0))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"background: #E94560;\n"
"border-radius: 2px;\n"
"")

        self.horizontalLayout_11.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(75, 27))
        self.pushButton_5.setMaximumSize(QSize(75, 27))
        self.pushButton_5.setSizeIncrement(QSize(0, 0))
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"background: #E94560;\n"
"border-radius: 2px;\n"
"")

        self.horizontalLayout_11.addWidget(self.pushButton_5)


        self.verticalLayout_6.addWidget(self.frame_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)


        self.horizontalLayout_18.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


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

        self.settings_2.setDefault(False)
        self.profilePhoto_2.setDefault(False)


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
        self.Learn_2.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
        self.Loop_2.setText(QCoreApplication.translate("MainWindow", u"Loop", None))
#if QT_CONFIG(statustip)
        self.settings_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.settings_2.setText("")
        self.profilePhoto_2.setText("")
        self.numOfGroups.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.numOfCourses.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Courses", None))
        self.numOfStudents.setText(QCoreApplication.translate("MainWindow", u"115", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Study Group", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" NEW", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search.....", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"st", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Electrical Power", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"st", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Electrical Power", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"st", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Electrical Power", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())