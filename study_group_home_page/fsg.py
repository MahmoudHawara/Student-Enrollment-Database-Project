# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fsg_H.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

mydb = mysql.connector.connect(
  host="db4free.net",
  user="reemmahmoud",
  password="dbfinalproject",
  database="dbfinalproject"
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # -----needs to be global---------------------------------------------------------------
        self.currentStudyGroupID = 2
        #---------------------------------------------------------------------------------
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT COUNT(*) FROM SG{}_COURSES".format(str(self.currentStudyGroupID)))
        self.coursesNumber = mycursor.fetchall()[0][0]

        mycursor.execute("SELECT COUNT(*) FROM SG{}_STUDENTS".format(str(self.currentStudyGroupID)))
        self.localStudentNumber = mycursor.fetchall()[0][0]
       
        mycursor.execute("SELECT SGname FROM study_groups WHERE PersonID = {}".format(str(self.currentStudyGroupID)))
        self.currentStudyGroupName = mycursor.fetchall()[0][0]
        mydb.close()
        
        self.separated_SGname = self.currentStudyGroupName.split(',')

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 880)
        MainWindow.setMinimumSize(QtCore.QSize(880, 880))
        MainWindow.setStyleSheet("background: #16213E;\n" "")
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ControlButtons_2 = QtWidgets.QFrame(self.header)
        self.ControlButtons_2.setObjectName("ControlButtons_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.ControlButtons_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.close_2 = QtWidgets.QPushButton(self.ControlButtons_2)
        self.close_2.setMinimumSize(QtCore.QSize(20, 26))
        self.close_2.setMaximumSize(QtCore.QSize(26, 26))
        self.close_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_2.setStyleSheet("QPushButton::hover{\n"
"    background-color: #E94560;\n"
"    border-radius: 12px;\n"
"}")
        self.close_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Controles/Images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_2.setIcon(icon)
        self.close_2.setIconSize(QtCore.QSize(12, 14))
        self.close_2.setFlat(True)
        self.close_2.setObjectName("close_2")
        self.horizontalLayout_6.addWidget(self.close_2)
        self.expand_2 = QtWidgets.QPushButton(self.ControlButtons_2)
        self.expand_2.setMinimumSize(QtCore.QSize(26, 26))
        self.expand_2.setMaximumSize(QtCore.QSize(26, 26))
        self.expand_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.expand_2.setStyleSheet("QPushButton::hover{\n"
"    background-color: #E94560;\n"
"    border-radius: 12px;\n"
"}")
        self.expand_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Controles/Images/expand-arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expand_2.setIcon(icon1)
        self.expand_2.setIconSize(QtCore.QSize(20, 25))
        self.expand_2.setFlat(True)
        self.expand_2.setObjectName("expand_2")
        self.horizontalLayout_6.addWidget(self.expand_2)
        self.minimize_2 = QtWidgets.QPushButton(self.ControlButtons_2)
        self.minimize_2.setMinimumSize(QtCore.QSize(26, 26))
        self.minimize_2.setMaximumSize(QtCore.QSize(26, 26))
        self.minimize_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize_2.setStyleSheet("QPushButton::hover{\n"
"    background-color: #E94560;\n"
"    border-radius: 12px;\n"
"}")
        self.minimize_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Controles/Images/minimize-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_2.setIcon(icon2)
        self.minimize_2.setIconSize(QtCore.QSize(13, 16))
        self.minimize_2.setFlat(True)
        self.minimize_2.setObjectName("minimize_2")
        self.horizontalLayout_6.addWidget(self.minimize_2)
        self.expand_3 = QtWidgets.QPushButton(self.ControlButtons_2)
        self.expand_3.setMinimumSize(QtCore.QSize(26, 26))
        self.expand_3.setMaximumSize(QtCore.QSize(26, 26))
        self.expand_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.expand_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.expand_3.setStyleSheet("QPushButton::hover{\n"
"    background-color: #E94560;\n"
"    border-radius: 12px;\n"
"}")
        self.expand_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Controles/Images/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expand_3.setIcon(icon3)
        self.expand_3.setIconSize(QtCore.QSize(20, 25))
        self.expand_3.setFlat(True)
        self.expand_3.setObjectName("expand_3")
        self.horizontalLayout_6.addWidget(self.expand_3)
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
        self.settings_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_2.setStatusTip("")
        self.settings_2.setStyleSheet("background-color: #E94560;\n"
"border-style: outset")
        self.settings_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Controles/Images/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_2.setIcon(icon4)
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
        self.profilePhoto_2.setMinimumSize(QtCore.QSize(45, 45))
        self.profilePhoto_2.setMaximumSize(QtCore.QSize(45, 45))
        self.profilePhoto_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profilePhoto_2.setAutoFillBackground(False)
        self.profilePhoto_2.setStyleSheet("")
        self.profilePhoto_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Controles/Images/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profilePhoto_2.setIcon(icon5)
        self.profilePhoto_2.setIconSize(QtCore.QSize(50, 45))
        self.profilePhoto_2.setAutoDefault(False)
        self.profilePhoto_2.setDefault(False)
        self.profilePhoto_2.setFlat(True)
        self.profilePhoto_2.setObjectName("profilePhoto_2")
        self.horizontalLayout_8.addWidget(self.profilePhoto_2)
        self.horizontalLayout_4.addWidget(self.ProfilePhotoAndSettings_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.header)
        self.mainPage = QtWidgets.QFrame(self.centralwidget)
        self.mainPage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPage.setStyleSheet("border: none;")
        self.mainPage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainPage.setObjectName("mainPage")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mainPage)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.department = QtWidgets.QFrame(self.mainPage)
        self.department.setMinimumSize(QtCore.QSize(0, 100))
        self.department.setMaximumSize(QtCore.QSize(16777215, 100))
        self.department.setStyleSheet("color: white;")
        self.department.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.department.setFrameShadow(QtWidgets.QFrame.Raised)
        self.department.setObjectName("department")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.department)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.department)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(5)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label, 0, QtCore.Qt.AlignBottom)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.department)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_9.addWidget(self.department, 0, QtCore.Qt.AlignHCenter)
        self.photo = QtWidgets.QFrame(self.mainPage)
        self.photo.setMinimumSize(QtCore.QSize(400, 400))
        self.photo.setMaximumSize(QtCore.QSize(400, 400))
        self.photo.setStyleSheet("")
        self.photo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.photo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.photo.setObjectName("photo")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.photo)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.photo)
        self.label_4.setMinimumSize(QtCore.QSize(400, 400))
        self.label_4.setMaximumSize(QtCore.QSize(400, 400))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Vectors/Images/2.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.verticalLayout_9.addWidget(self.photo, 0, QtCore.Qt.AlignHCenter)
        self.buttons = QtWidgets.QFrame(self.mainPage)
        self.buttons.setMinimumSize(QtCore.QSize(0, 130))
        self.buttons.setMaximumSize(QtCore.QSize(16777215, 130))
        self.buttons.setStyleSheet("")
        self.buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons.setObjectName("buttons")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(70)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_2 = QtWidgets.QFrame(self.buttons)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 130))
        self.frame_2.setMaximumSize(QtCore.QSize(200, 130))
        self.frame_2.setStyleSheet("background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 2px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton.clicked.connect(self.Courses_button_func)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: #E94560;\n"
"border-radius: 2px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_11.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.buttons)
        self.frame_3.setMinimumSize(QtCore.QSize(200, 130))
        self.frame_3.setMaximumSize(QtCore.QSize(200, 130))
        self.frame_3.setStyleSheet("background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 2px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_2.clicked.connect(self.Students_button_func)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: #E94560;\n"
"border-radius: 2px;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_11.addWidget(self.frame_3)
        self.verticalLayout_9.addWidget(self.buttons, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem5)
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
        self.close_2.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.expand_2.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.minimize_2.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.expand_3.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.Learn_2.setText(_translate("MainWindow", "Learn"))
        self.Loop_2.setText(_translate("MainWindow", "Loop"))
        self.label.setText(_translate("MainWindow", self.separated_SGname[0]))
        self.label_3.setText(_translate("MainWindow", self.separated_SGname[1]))
        self.label_2.setText(_translate("MainWindow", self.separated_SGname[2]))
        self.label_5.setText(_translate("MainWindow", str(self.coursesNumber)))
        self.label_6.setText(_translate("MainWindow", "Cousrses"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.label_7.setText(_translate("MainWindow", str(self.localStudentNumber)))
        self.label_8.setText(_translate("MainWindow", "Students"))
        self.pushButton_2.setText(_translate("MainWindow", "Enter"))
#import images_rc

    def Courses_button_func(self):
        self.coursesNumber +=1
        self.retranslateUi(MainWindow)

    def Students_button_func(self):
        self.retranslateUi(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
