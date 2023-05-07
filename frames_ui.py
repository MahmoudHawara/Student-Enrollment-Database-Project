# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frames.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(65, 125))
        self.frame_5.setMaximumSize(QSize(65, 125))
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

        self.frame_4 = QFrame(Form)
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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

