# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nav_bar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import  QtCore,QtGui, QtWidgets
from  PySide2 import  QtCore,QtGui, QtWidgets
def circleImage(imagePath):
    source = QtGui.QPixmap(imagePath)
    size = min(source.width(), source.height())

    target = QtGui.QPixmap(size, size)
    target.fill(QtCore.Qt.transparent)

    qp = QtGui.QPainter(target)
    qp.setRenderHints(qp.Antialiasing)
    path = QtGui.QPainterPath()
    path.addEllipse(0, 0, size, size)
    qp.setClipPath(path)

    sourceRect = QtCore.QRect(0, 0, size, size)
    sourceRect.moveCenter(source.rect().center())
    qp.drawPixmap(target.rect(), source, sourceRect)
    qp.end()

    return target

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 770)
        MainWindow.setMinimumSize(880, 770)
        MainWindow.setStyleSheet("background:  #16213E")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(0, 50)
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setStyleSheet("background: #0F3460")
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ControlButtons = QtWidgets.QFrame(self.header)
        self.ControlButtons.setObjectName("ControlButtons")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.ControlButtons)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.close = QtWidgets.QPushButton(self.ControlButtons)
        self.close.setMinimumSize(QtCore.QSize(20, 0))
        self.close.setMaximumSize(QtCore.QSize(20, 16777215))
        self.close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setIconSize(QtCore.QSize(13, 16))
        self.close.setFlat(True)
        self.close.setObjectName("close")
        self.horizontalLayout_5.addWidget(self.close)
        self.expand = QtWidgets.QPushButton(self.ControlButtons)
        self.expand.setMinimumSize(QtCore.QSize(20, 25))
        self.expand.setMaximumSize(QtCore.QSize(20, 25))
        self.expand.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Downloads/expand-arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expand.setIcon(icon1)
        self.expand.setIconSize(QtCore.QSize(20, 25))
        self.expand.setFlat(True)
        self.expand.setObjectName("expand")
        self.horizontalLayout_5.addWidget(self.expand)
        self.minimize = QtWidgets.QPushButton(self.ControlButtons)
        self.minimize.setMinimumSize(QtCore.QSize(20, 20))
        self.minimize.setMaximumSize(QtCore.QSize(20, 20))
        self.minimize.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../Downloads/minimize-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize.setIcon(icon2)
        self.minimize.setIconSize(QtCore.QSize(13, 16))
        self.minimize.setFlat(True)
        self.minimize.setObjectName("minimize")
        self.horizontalLayout_5.addWidget(self.minimize)
        self.horizontalLayout.addWidget(self.ControlButtons, 0, QtCore.Qt.AlignLeft)
        self.Logo = QtWidgets.QFrame(self.header)
        self.Logo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Logo.setObjectName("Logo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Logo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Learn = QtWidgets.QLabel(self.Logo)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Learn.setFont(font)
        self.Learn.setStyleSheet("color: white")
        self.Learn.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Learn.setWordWrap(False)
        self.Learn.setObjectName("Learn")
        self.horizontalLayout_2.addWidget(self.Learn)
        self.Loop = QtWidgets.QLabel(self.Logo)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Loop.setFont(font)
        self.Loop.setStyleSheet("color: #E94560")
        self.Loop.setObjectName("Loop")
        self.horizontalLayout_2.addWidget(self.Loop)
        self.horizontalLayout.addWidget(self.Logo)
        self.ProfilePhotoAndSettings = QtWidgets.QFrame(self.header)
        self.ProfilePhotoAndSettings.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ProfilePhotoAndSettings.setObjectName("ProfilePhotoAndSettings")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ProfilePhotoAndSettings)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.settings = QtWidgets.QPushButton(self.ProfilePhotoAndSettings)
        self.settings.setMinimumSize(QtCore.QSize(45, 50))
        self.settings.setMaximumSize(QtCore.QSize(45, 50))
        self.settings.setStatusTip("")
        self.settings.setStyleSheet("background-color: #E94560;\n"
"border-style: outset")
        self.settings.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../Downloads/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon3)
        self.settings.setIconSize(QtCore.QSize(30, 30))
        self.settings.setCheckable(False)
        self.settings.setAutoRepeat(False)
        self.settings.setAutoExclusive(False)
        self.settings.setAutoDefault(False)
        self.settings.setDefault(False)
        self.settings.setFlat(True)
        self.settings.setObjectName("settings")
        self.horizontalLayout_3.addWidget(self.settings)
        self.profilePhoto = QtWidgets.QPushButton(self.ProfilePhotoAndSettings)
        self.profilePhoto.setMinimumSize(QtCore.QSize(50, 50))
        self.profilePhoto.setMaximumSize(QtCore.QSize(50, 50))
        self.profilePhoto.setAutoFillBackground(False)
        self.profilePhoto.setStyleSheet("")
        self.profilePhoto.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(circleImage("../../../../Desktop/59022631_810914472627047_3797622654492475392_n.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profilePhoto.setIcon(icon4)
        self.profilePhoto.setIconSize(QtCore.QSize(50, 45))
        self.profilePhoto.setAutoDefault(False)
        self.profilePhoto.setDefault(False)
        self.profilePhoto.setFlat(True)
        self.profilePhoto.setObjectName("profilePhoto")
        self.horizontalLayout_3.addWidget(self.profilePhoto)
        self.horizontalLayout.addWidget(self.ProfilePhotoAndSettings, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.header)
        self.mainPage = QtWidgets.QFrame(self.centralwidget)
        self.mainPage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainPage.setObjectName("mainPage")
        self.verticalLayout.addWidget(self.mainPage)
        self.ControlSize = QtWidgets.QFrame(self.centralwidget)
        self.ControlSize.setMinimumSize(QtCore.QSize(0, 15))
        self.ControlSize.setMaximumSize(QtCore.QSize(16777215, 15))
        self.ControlSize.setObjectName("ControlSize")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ControlSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        # self.size_grip = QtWidgets.QFrame(self.ControlSize)
        # self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.size_grip.setObjectName("size_grip")
        #  chat
        self.size_grip = QtWidgets.QFrame(self.centralwidget)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QtCore.QSize(10, 10))
        self.size_grip.setMaximumSize(QtCore.QSize(10, 10))
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_3.addWidget(
        self.size_grip, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.ControlSize)#
        
        # self.verticalLayout_3.addWidget(self.size_grip)
        # self.verticalLayout.addWidget(self.ControlSize)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Learn.setText(_translate("MainWindow", "Learn"))
        self.Loop.setText(_translate("MainWindow", "Loop"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
