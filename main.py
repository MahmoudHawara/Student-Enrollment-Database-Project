import sqlite3
import sys
import re
import os
from PySide2 import *
from ui_login import *
from ui_interface import *
from ui_home import *
from ui_contacts import *
from ui_welcome import *
from ui_signUp import *
from ui_splash_screen import Ui_SplashScreen
from Custom_Widgets.Widgets import *
from PyQt5.uic import loadUi, loadUiType
#from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget
from PIL import Image
from PyQt5.QtCore import center, pyqtSlot
import PIL
import platform
from typing import Counter, Text
from functools import partial

# globals
counter = 0
jumper = 0
ph = ""
nm = ""
xxpath = ()

os.chdir(r"D:\pthon-prj2\chatZone")
# os.mkdir("contacts")


class My_contact():
    def __init__(self, phone, username, state="offline", photo=":/appIcon/contacts-512.png"):
        self.phone = phone
        self.username = username
        self.state = state
        self.photo = photo

class Base():
    cur_theme = 0

    def __init__(self):
        self.set_theme(0)

    def set_theme(self, num):
        if num == 1:
            self.Apply_DarkOrange_Style()
        elif num == 2:
            self.Apply_QDark_Style()
        elif num == 3:
            self.Apply_DarkGray_Style()
        elif num == 4:
            self.Apply_QDarkBlue_Style()
        else:
            pass

    # connect main app to welcome screen
    @staticmethod
    def gotochats():
        main = MainWindow()
        main.show()

    @staticmethod
    def gotoWlcome_screen():
        welcome = WelcomeScreen()
        welcome.show()

    @staticmethod
    def gotologin():
        login = LoginScreen()
        login.show()

    @staticmethod
    def gotocreate():
        create = createAccScreen()
        create.show()

    # @staticmethod
    # def goto_theme():
    #     theme = Themes()

    @staticmethod
    def goto_add_contact():
        add_contact = AddContact()
        add_contact.show()

    @staticmethod
    def gotomainscreen():
        mains = MainWindow()
        mains.show()

    @staticmethod
    def gotosetting():
        settings = SettingsWindow()
        settings.show()

    @staticmethod
    def gotocontacts():
        contacts = AddContact()
        contacts.show()

    @staticmethod
    def refresh(obj):
        obj.close()
        obj.show()

    # appling themes
    def Apply_DarkOrange_Style(self):
        style = open('themes/darkorange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Apply_QDark_Style(self):
        style = open('themes/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Apply_DarkGray_Style(self):
        style = open('themes/qdarkgray.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Apply_QDarkBlue_Style(self):
        style = open('themes/dark-blue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

class MainWindow(QMainWindow, Ui_MainWindow, Base):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.chat_widget_list = []
        self.ui.verticalLayout_9 = None
        self.ui.horizontalLayout_8 = None
        self.ui.theChat = None
        self.ui.Profile.clicked.connect(self.settings)
        self.ui.logout.clicked.connect(self.logout)
        self.ui.refresh.clicked.connect(self.ref)
        self.ui.searchbtn.clicked.connect(self.search)
        self.ui.searchLineEdit.textChanged.connect(self.search)
        # self.ui.mode.clicked.connect(self.mode)
        self.ui.contacts.clicked.connect(self.contacts)
        self.initUI()

    def search(self):
        srch = self.ui.searchLineEdit.text()
        
        if srch != "":
            self.hideChats()
            global ph
            ds = []
            user_db = "contacts/" + ph + ".db"
            db = sqlite3.connect(user_db)
            cr = db.cursor()
            cr.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT)")
            cr.execute(f"SELECT * FROM contacts")
            myContacts = cr.fetchall()
            db.close()

            for contact in myContacts:
                if srch in contact[0]:
                    pho = "pictures/" + ph + '.png'
                    ds.append(My_contact(contact[1], contact[0], photo=pho))

            if len(ds):
                for c in range(len(ds)):
                    self.create_chat_contact(ds[c])
                # self.ui.verticalSpacer = QSpacerItem(
                # 20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                # self.ui.verticalLayout_8.addItem(self.ui.verticalSpacer)
                # self.ui.chatScrollArea.setWidget(self.ui.scrollAreaWidgetContents)
            else:
                self.ui.NoResultsMessage.setText(f"No Results for '{srch}'") 
                   
        else:
            self.ui.NoResultsMessage.setText("")
            self.hideChats()
            self.fetch_database_contacts()

    def hideChats(self):
        for chat in self.chat_widget_list:
            chat[0].hide()

    def ref(self):
        self.close()
        Base.gotomainscreen()

    def logout(self):
        self.close()
        Base.gotoWlcome_screen()

    def settings(self):
        self.close()
        Base.gotosetting()

    def contacts(self):
        self.close()
        Base.gotocontacts()

    def getHeight(self,string):
        l = string.split()
        counter = 0
        cnt__ = 0
        outputString = ''
        for i in l:
            if counter + len(i) <= 35:
                counter += len(i)
                outputString +=" "+ i

            else:
                counter = len(i)
                cnt__ += 1
                outputString += '\n'+i

        return [cnt__+1,outputString]

    def initUI(self):
        # fetch contacts from data base
        self.fetch_database_contacts()

    # adding contacts in main screen
    @pyqtSlot()
    def send_message(self, contact):
        if self.ui.messageInput.text() != "":
            messege_frame = QFrame(self.ui.scrollAreaWidgetContents_2)
            messege_frame.setMinimumSize(QSize(0, 80))
            messege_frame.setStyleSheet(u"background-color: #22303C;")
            messege_frame.setFrameShape(QFrame.StyledPanel)
            messege_frame.setFrameShadow(QFrame.Raised)
            messege= QLabel(text =self.getHeight(self.ui.messageInput.text())[1],parent=messege_frame)
            messege.setFrameShape(QLabel.NoFrame)
            messege.setFrameShadow(QLabel.Plain)
            messege.setStyleSheet("color:white;\npadding:10px;\nfont-size:22px;\n")
            
            messege_frame.setMinimumHeight(self.getHeight(self.ui.messageInput.text())[0]*45)

            if 1:
                messege_frame.setStyleSheet("background-color: #22303C;\nmargin-left:100px;")
            else:
                messege_frame.setStyleSheet("background-color: #22303C;\nmargin-right:100px;")
            
            self.ui.verticalLayout_11.addWidget(messege_frame)
            messege_frame.show()
            messege.show()

            db = sqlite3.connect("contacts/" + ph + ".db")
            cr = db.cursor()
            cr.execute(f"CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT)")
            cr.execute(f"SELECT name from contacts WHERE phone = '{contact.phone}'")
            c = cr.fetchone()
            if(c): Name = c[0]
            else: Name = contact.phone
            db.close()

            ct = ph + '/' + "chats.db"
            db = sqlite3.connect(ct)
            cr = db.cursor()
            cr.execute(f"CREATE TABLE IF NOT EXISTS chat (user TEXT, phone TEXT)")
            cr.execute(f"SELECT user from chat WHERE phone = '{contact.phone}'")
            t = cr.fetchone()
            if t == None: cr.execute(f"INSERT INTO chat(user, phone) values('{Name}', '{contact.phone}')")
            db.commit()
            db.close()

            ct = ph + "/" + contact.phone + '.db'
            db = sqlite3.connect(ct)
            db.execute(f"CREATE TABLE IF NOT EXISTS chat (massage TEXT, side INTEGER)")
            cr = db.cursor()
            lst = [self.ui.messageInput.text(), 0]
            cr.execute("INSERT INTO chat (massage,side) values(?,?)", lst)
            lst.clear()
            db.commit()
            db.close()

            db = sqlite3.connect("contacts/" + contact.phone + ".db")
            cr = db.cursor()
            cr.execute(f"CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT)")
            cr.execute(f"SELECT name from contacts WHERE phone = '{ph}'")
            c = cr.fetchone()
            if(c): Name = c[0]
            else: Name = ph
            db.close()

            ct = contact.phone + '/' + "chats.db"
            db = sqlite3.connect(ct)
            cr = db.cursor()
            cr.execute(f"CREATE TABLE IF NOT EXISTS chat (user TEXT, phone TEXT)")
            cr.execute(f"SELECT user from chat WHERE phone = '{ph}'")
            t = cr.fetchone()
            if t == None: cr.execute(f"INSERT INTO chat(user, phone) values('{Name}', '{ph}')")
            db.commit()
            db.close()

            ct = contact.phone + "/" + ph + '.db'
            db = sqlite3.connect(ct)
            db.execute(f"CREATE TABLE IF NOT EXISTS chat (massage TEXT, side INTEGER)")
            cr = db.cursor()
            lst = [self.ui.messageInput.text(), 1]
            cr.execute("INSERT INTO chat (massage,side) values(?,?)", lst)
            db.commit()
            db.close()
            self.ui.messageInput.setText("")
        else:
            # making a record
            pass

    @pyqtSlot()
    def whenClick(self, contact, event):
        self.create_chat_ui(contact)
        self.load_messeges(contact)
        print(contact.username)

    def create_chat_ui(self, contact):
        # ..........cleraring
        if self.ui.theChat is not None:
            self.ui.theChat.deleteLater()
        # ...............................
        self.ui.theChat = QFrame(self.ui.theChat_0)
        # self.ui.theChat.setStyleSheet('background-color: red;')
        self.ui.verticalLayout_9 = QVBoxLayout(self.ui.theChat)
        self.ui.verticalLayout_9.setSpacing(0)
        self.ui.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ui.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.ui.userInfo = QFrame(self.ui.theChat)
        self.ui.userInfo.setObjectName(u"userInfo")
        self.ui.userInfo.setStyleSheet(u"background-color: transparent;")
        self.ui.userInfo.setFrameShape(QFrame.StyledPanel)
        self.ui.userInfo.setFrameShadow(QFrame.Raised)
        self.ui.horizontalLayout_8 = QHBoxLayout(self.ui.userInfo)
        self.ui.horizontalLayout_8.setSpacing(0)
        self.ui.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.ui.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.ui.logoAndName = QFrame(self.ui.userInfo)
        self.ui.logoAndName.setObjectName(u"logoAndName")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ui.logoAndName.sizePolicy().hasHeightForWidth())
        self.ui.logoAndName.setSizePolicy(sizePolicy2)
        self.ui.logoAndName.setFrameShape(QFrame.StyledPanel)
        self.ui.logoAndName.setFrameShadow(QFrame.Raised)
        self.ui.horizontalLayout_6 = QHBoxLayout(self.ui.logoAndName)
        self.ui.horizontalLayout_6.setSpacing(10)
        self.ui.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ui.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ui.photo = QLabel(self.ui.logoAndName)
        self.ui.photo.setObjectName(u"photo")
        self.ui.photo.setMaximumSize(QSize(50, 50))
        self.ui.photo.setPixmap(QPixmap(f"{contact.photo}"))
        self.ui.photo.setScaledContents(True)
        self.ui.horizontalLayout_6.addWidget(self.ui.photo)
        self.ui.userNameAndState = QVBoxLayout()
        self.ui.userNameAndState.setSpacing(10)
        self.ui.userNameAndState.setObjectName(u"userNameAndState")
        self.ui.userName = QLabel(contact.username, self.ui.logoAndName)
        self.ui.userName.setObjectName(u"userName")
        font7 = QFont()
        font7.setFamily(u"Trebuchet MS")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.ui.userName.setFont(font7)
        self.ui.userNameAndState.addWidget(self.ui.userName, 0, Qt.AlignBottom)
        self.ui.state = QLabel(contact.state, self.ui.logoAndName)
        self.ui.state.setObjectName(u"state")
        font8 = QFont()
        font8.setPointSize(10)
        self.ui.state.setFont(font8)
        self.ui.userNameAndState.addWidget(self.ui.state, 0, Qt.AlignTop)
        self.ui.horizontalLayout_6.addLayout(self.ui.userNameAndState)
        self.ui.horizontalLayout_8.addWidget(self.ui.logoAndName)
        self.ui.optionsForChat = QHBoxLayout()
        self.ui.optionsForChat.setSpacing(15)
        self.ui.optionsForChat.setObjectName(u"optionsForChat")
        self.ui.label_2 = QLabel(self.ui.userInfo)
        self.ui.label_2.setObjectName(u"label_2")
        self.ui.label_2.setMaximumSize(QSize(30, 30))
        self.ui.label_2.setPixmap(QPixmap(u":/appIcon/zoom (1).png"))
        self.ui.label_2.setScaledContents(True)
        self.ui.optionsForChat.addWidget(self.ui.label_2)
        self.ui.label_3 = QLabel(self.ui.userInfo)
        self.ui.label_3.setObjectName(u"label_3")
        self.ui.label_3.setMaximumSize(QSize(20, 20))
        self.ui.label_3.setPixmap(QPixmap(u":/appIcon/phone-call (1).png"))
        self.ui.label_3.setScaledContents(True)
        self.ui.optionsForChat.addWidget(self.ui.label_3)
        self.ui.label = QLabel(self.ui.userInfo)
        self.ui.label.setObjectName(u"label")
        self.ui.label.setMaximumSize(QSize(20, 20))
        self.ui.label.setPixmap(QPixmap(u":/appIcon/option (1).png"))
        self.ui.label.setScaledContents(True)
        self.ui.optionsForChat.addWidget(self.ui.label)
        self.ui.horizontalLayout_8.addLayout(self.ui.optionsForChat)
        self.ui.verticalLayout_9.addWidget(self.ui.userInfo)
        self.ui.frame = QFrame(self.ui.theChat)
        self.ui.frame.setObjectName(u"frame")
        self.ui.frame.setFrameShape(QFrame.StyledPanel)
        self.ui.frame.setFrameShadow(QFrame.Raised)
        self.ui.horizontalLayout_7 = QHBoxLayout(self.ui.frame)
        self.ui.horizontalLayout_7.setSpacing(0)
        self.ui.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ui.horizontalLayout_7.setContentsMargins(0, 12, 0, 12)
        self.ui.line = QFrame(self.ui.frame)
        self.ui.line.setObjectName(u"line")
        self.ui.line.setStyleSheet(u"background-color: lightgrey")
        self.ui.line.setFrameShape(QFrame.HLine)
        self.ui.line.setFrameShadow(QFrame.Sunken)
        self.ui.horizontalLayout_7.addWidget(self.ui.line)
        self.ui.verticalLayout_9.addWidget(self.ui.frame)
        # ........................................................
        self.ui.scrollArea = QScrollArea(self.ui.theChat)
        self.ui.scrollArea.setObjectName(u"scrollArea")
        self.ui.scrollArea.setStyleSheet("background-color: rgb(21, 32, 43);\nborder: none;\nborder-radius: 10px;\n")
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.scrollAreaWidgetContents_2 = QWidget()
        self.ui.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.ui.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 948, 671))
        self.ui.size_grip = QFrame(self.ui.scrollAreaWidgetContents_2)
        # 000 scroll messege
        self.ui.verticalLayout_11 = QVBoxLayout(self.ui.scrollAreaWidgetContents_2)
        self.ui.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.ui.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.verticalLayout_11.addItem(self.ui.verticalSpacer_2)
        # 000
        self.ui.size_grip.setObjectName(u"size_grip")
        self.ui.size_grip.setGeometry(QRect(-520, 730, 1565, 10))
        self.ui.size_grip.setMinimumSize(QSize(10, 10))
        self.ui.size_grip.setFrameShape(QFrame.StyledPanel)
        self.ui.size_grip.setFrameShadow(QFrame.Raised)
        self.ui.scrollArea.setWidget(self.ui.scrollAreaWidgetContents_2)
        self.ui.verticalLayout_9.addWidget(self.ui.scrollArea)
        self.ui.frame_3 = QFrame(self.ui.theChat)
        self.ui.frame_3.setObjectName(u"frame_3")
        self.ui.frame_3.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_3.setFrameShadow(QFrame.Raised)
        self.ui.horizontalLayout_9 = QHBoxLayout(self.ui.frame_3)
        self.ui.horizontalLayout_9.setSpacing(0)
        self.ui.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.ui.horizontalLayout_9.setContentsMargins(0, 12, 0, 12)
        self.ui.line_2 = QFrame(self.ui.frame_3)
        self.ui.line_2.setObjectName(u"line_2")
        self.ui.line_2.setStyleSheet(u"background-color: lightgrey")
        self.ui.line_2.setFrameShape(QFrame.HLine)
        self.ui.line_2.setFrameShadow(QFrame.Sunken)
        self.ui.horizontalLayout_9.addWidget(self.ui.line_2)
        self.ui.verticalLayout_9.addWidget(self.ui.frame_3)
        # ....................................................
        self.ui.sendMessageFrame = QFrame(self.ui.theChat)
        self.ui.sendMessageFrame.setObjectName(u"sendMessageFrame")
        self.ui.sendMessageFrame.setMinimumSize(QSize(0, 0))
        self.ui.sendMessageFrame.setFrameShape(QFrame.StyledPanel)
        self.ui.sendMessageFrame.setFrameShadow(QFrame.Raised)
        self.ui.horizontalLayout_10 = QHBoxLayout(self.ui.sendMessageFrame)
        self.ui.horizontalLayout_10.setSpacing(25)
        self.ui.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.ui.horizontalLayout_10.setContentsMargins(10, 0, 10, 0)
        self.ui.attachmentBtn = QPushButton(self.ui.sendMessageFrame)
        self.ui.attachmentBtn.setObjectName(u"attachmentBtn")

        icon8 = QIcon()
        icon8.addFile(u":/appIcon/attach-paperclip-symbol (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.attachmentBtn.setIcon(icon8)
        self.ui.attachmentBtn.setIconSize(QSize(25, 25))
        self.ui.horizontalLayout_10.addWidget(self.ui.attachmentBtn)
        self.ui.messageInput = QLineEdit(self.ui.sendMessageFrame)
        self.ui.messageInput.setObjectName(u"messageInput")
        self.ui.messageInput.setPlaceholderText("Enter a messege....")
        self.ui.messageInput.setStyleSheet("background-color: transparent;\ncolor: #fff;\nheight: 35px; border:none;")
        font9 = QFont()
        font9.setFamily(u"Trebuchet MS")
        font9.setPointSize(11)
        self.ui.messageInput.setFont(font9)
        self.ui.horizontalLayout_10.addWidget(self.ui.messageInput)
        self.ui.recordBtn = QPushButton(self.ui.sendMessageFrame)
        self.ui.recordBtn.setObjectName(u"recordBtn")
        icon9 = QIcon()
        icon9.addFile(u":/appIcon/voice (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.recordBtn.setIcon(icon9)
        self.ui.recordBtn.setIconSize(QSize(30, 30))
        self.ui.horizontalLayout_10.addWidget(self.ui.recordBtn)
        self.ui.verticalLayout_9.addWidget(self.ui.sendMessageFrame)
        self.ui.horizontalLayout_4.addWidget(self.ui.theChat)
        self.ui.recordBtn.setStyleSheet("background-color: transparent;\ncolor: #fff\n")
        self.ui.attachmentBtn.setStyleSheet("background-color: transparent;\ncolor: #fff\n")
        # sending messege
        self.ui.messageInput.textChanged.connect(self.change_send_icon)
        display_a = partial(self.send_message, contact)
        self.ui.messageInput.returnPressed.connect(display_a)
        self.ui.recordBtn.clicked.connect(display_a)  # making send putton

    def change_send_icon(self):
        icon9 = QIcon()
        if self.ui.messageInput.text() == "":
            icon9.addFile(u":/appIcon/voice (2).png",QSize(), QIcon.Normal, QIcon.Off)
        else:
            icon9.addFile(u":/appIcon/telegram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.recordBtn.setIcon(icon9)

    def create_chat_contact(self, user):
        self.ui.chat_widget = QFrame(self.ui.scrollAreaWidgetContents)    
        self.ui.chat_widget.setObjectName(f"chat-widget")
        self.ui.chat_widget.name = user.username
        self.ui.chat_widget.setMinimumSize(QSize(0, 140))
        self.ui.chat_widget.setMaximumSize(QSize(440, 140))
        self.ui.chat_widget.setStyleSheet(u"background-color: #22303C;")
        self.ui.chat_widget.setFrameShape(QFrame.StyledPanel)
        self.ui.chat_widget.setFrameShadow(QFrame.Raised)
        self.ui.chat_widget.show()
        self.chat_widget_list.append((self.ui.chat_widget, user.username))
        self.ui.chat_widget.mouseReleaseEvent = lambda e: self.whenClick(event=e, contact=user)
        l = QLabel(f"{user.username}", self.ui.chat_widget)
        l.setMinimumSize(30, 50)
        l.setFont(self.ui.font4)
        l.setStyleSheet(u"color: #fff\n""\n""")
        l.show()
        self.ui.verticalLayout_8.addWidget(self.ui.chat_widget)

    def fetch_database_contacts(self):
        my_contacts = []
        # fetching contacts and store in the list
        mydata = ph + '/' + 'chats.db'
        db = sqlite3.connect(mydata)
        cr = db.cursor()
        cr.execute("CREATE TABLE IF NOT EXISTS chat (user TEXT, phone TEXT)")
        cr.execute(f"SELECT * FROM chat")
        data = cr.fetchall()
        # db.commit()
        db.close()

        for i in data:
            pho = "pictures/" + i[1] + '.png'
            my_contacts.append(My_contact(i[1], i[0], photo=pho))
        # creating widget
        for i in range(len(my_contacts)):
            self.create_chat_contact(my_contacts[i])
        self.ui.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.verticalLayout_8.addItem(self.ui.verticalSpacer)
        self.ui.chatScrollArea.setWidget(self.ui.scrollAreaWidgetContents)

    def load_messeges(self, contact):
        exist_messeges = []
        # fetching messeges from database
        ct = ph + "/" + contact.phone + '.db'
        db = sqlite3.connect(ct)
        db.execute(f"CREATE TABLE IF NOT EXISTS chat (massage TEXT, side INTEGER)")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM chat")
        exist_messeges = cr.fetchall()
        db.close()
        # showing messeges
        for i in range(len(exist_messeges)):
            messege_frame = QFrame(self.ui.scrollAreaWidgetContents_2)
            messege_frame.setMinimumSize(QSize(0, 80))
            messege_frame.setStyleSheet(u"background-color: #22303C;")
            messege_frame.setFrameShape(QFrame.StyledPanel)
            messege_frame.setFrameShadow(QFrame.Raised)
            messege_frame.setMinimumHeight(self.getHeight(exist_messeges[i][0])[0]*45)
            messege= QLabel(text =self.getHeight(exist_messeges[i][0])[1],parent=messege_frame)
            messege.setFrameShape(QLabel.NoFrame)
            messege.setFrameShadow(QLabel.Plain)
            messege.setStyleSheet("color:white;\npadding:10px;\nfont-size:22px;\n")
            if not exist_messeges[i][1]:
                messege_frame.setStyleSheet("background-color: #22303C;\nmargin-left:100px;\n")
            else:
                messege_frame.setStyleSheet("background-color: #22303C;\nmargin-right:100px;\n")
            self.ui.verticalLayout_11.addWidget(messege_frame)
            messege_frame.show()
            messege.show()
            
class WelcomeScreen(QMainWindow, Base):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        self.ui = Ui_MainWindowWelcome()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.ui.loginB.clicked.connect(self.goLI)
        self.ui.CreateaccB.clicked.connect(self.goCA)

    def goLI(self):
        self.close()
        Base.gotologin()

    def goCA(self):
        self.close()
        Base.gotocreate()

class LoginScreen(QMainWindow, Base):
    def __init__(self):
        super(LoginScreen, self).__init__()
        self.ui = Ui_MainWindowLI()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.ui.signInButton.clicked.connect(self.loginfunction)
        self.ui.signInButton.shortcut.activated.connect(self.loginfunction)
        self.ui.leftBtn.clicked.connect(self.back)

    def back(self):
        self.close()
        Base.gotoWlcome_screen()
#start here----------------------------------------------------------------------------------------------------------------
    def loginfunction(self):
        phone = self.ui.userNameInput.text()
        password = self.ui.passInput.text()

        if len(phone) == 0 or len(password) == 0:
            self.ui.toUserFromPassFrame.setText("Please, fill all fields")
        else:
            dataB = sqlite3.connect("usersdata.db")
            cur = dataB.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS USERS (phone TEXT, pass TEXT)")
            fnd = f"SELECT pass From USERS WHERE phone ='{phone}'"
            cur.execute(fnd)
            one = cur.fetchone()
            if one == None:
                self.ui.toUserFromUserNameFrame.setText("invalid phone number")
                self.ui.toUserFromPassFrame.setText("")

            elif (list(one))[0] == password:
                # go to main screen ui
                global ph, nm
                ph = phone
                cur.execute(f"SELECT UserName From extradata WHERE phone ='{phone}'")
                n = cur.fetchone()
                nm = n[0]
                self.ui.toUserFromPassFrame.setText("")
                self.ui.toUserFromUserNameFrame.setText("")
                self.close()
                Base.gotomainscreen()

               # MainApp.gotoMainApp()

            else:
                self.ui.toUserFromPassFrame.setText("invalid  password")
                self.ui.toUserFromUserNameFrame.setText("")

class createAccScreen(QMainWindow, Base):
    def __init__(self):
        super(createAccScreen, self).__init__()
        self.ui = Ui_MainWindowSU()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.ui.signUpButton.clicked.connect(self.SignUpFun)
        self.ui.signUpButton.shortcut.activated.connect(self.SignUpFun)
        self.ui.leftBtn.clicked.connect(self.back)

    def back(self):
        self.close()
        Base.gotoWlcome_screen()

    def clear(self):
        self.ui.toUserFromPhoneFrame.setText("")
        self.ui.toUserFromPassFrame.setText("")
        self.ui.toUserFromConfPassFrame.setText("")
        self.ui.toUserFromFirstNameFrame.setText("")
        self.ui.toUserFromLastNameFrame.setText("")
        self.ui.toUserFromPinFrame.setText("")
        self.ui.toUserFromUserNameFrame.setText("")

    def SignUpFun(self):
        global ph, nm
        ph = self.ui.phoneInput.text()
        password = self.ui.passInput.text()
        Cpass = self.ui.confPassInput.text()
        pin = self.ui.pinInput.text()
        firstN = self.ui.firstNameInput.text()
        lastN = self.ui.lastNameInput.text()
        username = self.ui.userNameInput.text()
        nm = username

        # check if phone number already exists
        db = sqlite3.connect("usersdata.db")
        db.execute("CREATE TABLE IF NOT EXISTS USERS (phone TEXT, pass TEXT)")
        cr = db.cursor()
        cr.execute(f"SELECT phone FROM USERS WHERE phone = '{ph}'")
        phone = cr.fetchone()
        db.commit()
        db.close()

        # password validation
        if len(ph) == 0 or len(password) == 0 or len(Cpass) == 0 or len(pin) == 0 or len(firstN) == 0 or len(lastN) == 0 or len(username) == 0:
            if len(ph) == 0:
                self.clear()
                self.ui.toUserFromPhoneFrame.setText("you must fill this field")
            elif len(password) == 0:
                self.clear()
                self.ui.toUserFromPassFrame.setText("you must fill this field")
            elif len(Cpass) == 0:
                self.clear()
                self.ui.toUserFromConfPassFrame.setText("you must fill this field")
            elif len(firstN) == 0:
                self.clear()
                self.ui.toUserFromFirstNameFrame.setText("you must fill this field")
            elif len(lastN) == 0:
                self.clear()
                self.ui.toUserFromLastNameFrame.setText("you must fill this field")
            elif len(pin) == 0:
                self.clear()
                self.ui.toUserFromPinFrame.setText("you must fill this field")
            else:
                self.clear()
                self.ui.toUserFromUserNameFrame.setText("you must fill this field")
        elif phone != None:
            self.clear()
            self.ui.toUserFromPhoneFrame.setText("phone number already exists")

        elif len(password) < 8:
            self.clear()
            self.ui.toUserFromPassFrame.setText("Make sure your password is at least 8 letters")
        elif re.search('[0-9]', password) is None:
            self.clear()
            self.ui.toUserFromPassFrame.setText("password must contain number")
        elif re.search('[A-Z]', password) is None and re.search('[a-z]', password) is None:
            self.clear()
            self.ui.toUserFromPassFrame.setText("Make sure your password a letter")
        elif password != Cpass:
            self.clear()
            self.ui.toUserFromConfPassFrame.setText("passwords dont match")
        elif (not ph.isdigit()) or ph[0] != '0' or ph[1] != '1' or (ph[2] != '0' and ph[2] != '1' and ph[2] != '2' and ph[2] != '5') or len(ph) != 11:
            self.clear()
            self.ui.toUserFromPhoneFrame.setText("enter Egyptian phone number")
        elif len(pin) != 4 or (not pin.isdigit()):
            self.clear()
            self.ui.toUserFromPinFrame.setText("pin must be 4 numbers")
        else:
            self.clear()
            Dsave = sqlite3.connect("usersdata.db")
            cur = Dsave.cursor()
            mylist = [ph, password]
            bio = "Hey, there..."
            myextralist = [ph, username, firstN, lastN, pin, bio]
            cur.execute("INSERT INTO USERS (phone, pass) values(?, ?)", mylist)
            Dsave.execute("CREATE TABLE IF NOT EXISTS extradata (phone TEXT, UserName TEXT, firstN TEXT, Lname TEXT, pin TEXT, BIO TEXT)")
            cur.execute("INSERT INTO extradata (phone, UserName, firstN, Lname, pin,BIO) values(?,?,?,?,?,?)", myextralist)
            Dsave.commit()
            Dsave.close()
            placeholderimg = "placeholder.png"
            im1 = Image.open(placeholderimg)
            fpath = f"pictures\{ph}.png"
            im1 = im1.save(fpath)
            os.mkdir(ph)
            self.close()
            Base.gotomainscreen()

class AddContact(QMainWindow, Base):
    def __init__(self):
        super(AddContact, self).__init__()
        self.ui = Ui_MainWindowContacts()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.ui.Profile.clicked.connect(self.settings)
        self.ui.messages.clicked.connect(self.chat)
        self.ui.logout.clicked.connect(self.logout)
        self.ui.refresh.clicked.connect(self.ref)
        # self.ui.mode.clicked.connect(self.mode)
        self.ui.addButton.clicked.connect(self.add)
        self.ui.addButton.shortcut.activated.connect(self.add)

    def ref(self):
        self.close()
        Base.gotocontacts()

    def logout(self):
        self.close()
        Base.gotoWlcome_screen()

    def settings(self):
        self.close()
        Base.gotosetting()

    def chat(self):
        self.close()
        Base.gotochats()

    def add(self):
        self.ui.doneMessage.clear()
        name = self.ui.contactName.text()
        phone = self.ui.contactPhone.text()

        global ph
        user_db = "contacts/" + ph + ".db"
        db = sqlite3.connect(user_db)
        cr = db.cursor()
        cr.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT)")
        cr.execute(f"SELECT phone FROM contacts WHERE phone = '{phone}'")
        p = cr.fetchone()
        db = sqlite3.connect("usersdata.db")
        cr = db.cursor()
        cr.execute(f"SELECT phone FROM USERS WHERE phone = '{phone}'")
        p2 = cr.fetchone()
        db.commit()
        db.close()

        if len(phone) == 0 or len(name) == 0:
            self.ui.toUserFromPhoneFrame.setText("fill all fields")
        elif (not phone.isdigit()) or phone[0] != '0' or phone[1] != '1' or (phone[2] != '0' and phone[2] != '1' and phone[2] != '2' and phone[2] != '5') or len(phone) != 11:
            self.ui.toUserFromPhoneFrame.setText("phone must consist of numbers and eg phone number")
        elif p != None:
            self.ui.toUserFromPhoneFrame.setText("This contact already exists")
        elif phone == ph:
            self.ui.toUserFromPhoneFrame.setText("contact cannot be added")
        elif p2 == None:
            self.ui.toUserFromPhoneFrame.setText("unavailable contact")
        else:
            db = sqlite3.connect(user_db)
            cr = db.cursor()
            cr.execute(f"INSERT INTO contacts(name, phone) values('{name}', '{phone}')")
            self.ui.doneMessage.setText(f" {name} is added to your contacts")
            db.commit()
            db.close()

            user_db = ph + '/' + "chats.db"
            db = sqlite3.connect(user_db)
            cr = db.cursor()
            cr.execute(f"CREATE TABLE IF NOT EXISTS chat (user TEXT, phone TEXT)")
            cr.execute(f"SELECT user from chat WHERE phone = '{phone}'")
            t = cr.fetchone()
            if t != None: cr.execute(f"UPDATE chat SET user = '{name}' WHERE phone = '{phone}'")
            db.commit()
            db.close()

class SettingsWindow(QMainWindow, Base):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = Ui_MainWindowsettings()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.initPlaceholders()
        self.ui.editUserNameButton.clicked.connect(lambda: self.edit(1))
        self.ui.username.returnPressed.connect(lambda: self.edit(1))

        self.ui.editFirstNameButton.clicked.connect(lambda: self.edit(2))
        self.ui.firstName.returnPressed.connect(lambda: self.edit(2))
        
        self.ui.editLastNameButton.clicked.connect(lambda: self.edit(3))
        self.ui.Lastname.returnPressed.connect(lambda: self.edit(3))

        # self.ui.editPhoneButton.clicked.connect(lambda: self.edit(4))
        
        self.ui.editPasswordButton.clicked.connect(lambda: self.edit(5))
        self.ui.password.returnPressed.connect(lambda: self.edit(5))

        self.ui.editBioButton.clicked.connect(lambda: self.edit(6))
        self.ui.bio.returnPressed.connect(lambda: self.edit(6))

        self.ui.changePhotoButton.clicked.connect(lambda: self.edit(7))
        
        self.ui.messages.clicked.connect(self.chat)
        # self.ui.Profile.clicked.connect(self.settings)
        self.ui.logout.clicked.connect(self.logout)
        self.ui.refresh.clicked.connect(self.ref)
        # self.ui.mode.clicked.connect(self.mode)
        self.ui.contacts.clicked.connect(self.contacts)

    def ref(self):
        self.close()
        Base.gotosetting()

    def logout(self):
        self.close()
        Base.gotoWlcome_screen()

    def contacts(self):
        self.close()
        Base.goto_add_contact()

    def chat(self):
        self.close()
        Base.gotochats()

    def initPlaceholders(self):
        global ph
        db = sqlite3.connect("usersdata.db")
        cr = db.cursor()
        cr.execute(f"SELECT * FROM extradata WHERE phone = '{ph}'")
        p = cr.fetchone()  # (phone, username, first name, last name, gender, bio)
        self.ui.phoneNumber.setPlaceholderText(p[0])
        self.ui.username.setPlaceholderText(p[1])
        self.ui.user_name.setText(p[1])
        self.ui.firstName.setPlaceholderText(p[2])
        self.ui.Lastname.setPlaceholderText(p[3])
        cr.execute(f"SELECT pass FROM USERS WHERE phone = '{ph}'")
        p2 = cr.fetchone()
        self.ui.password.setPlaceholderText(p2[0])
        self.ui.bio.setPlaceholderText(p[5])
        self.ui.bioContent.setText(p[5])
        self.ui.UserFullName.setText(p[2] + " " + p[3])
        self.ui.changePhotoButton.setIcon(QIcon(QPixmap(f"pictures\{ph}.png")))
        self.ui.changePhotoButton.setIconSize(self.ui.changePhotoButton.size())
        db.commit()
        db.close()

    def edit(self, n):
        global ph
        db = sqlite3.connect("usersdata.db")
        cr = db.cursor()
        cr.execute(f"SELECT firstN, Lname FROM extradata WHERE phone = '{ph}'")
        fl = cr.fetchone()

        if n == 1:  # edit username
            new_userName = self.ui.username.text()
            if new_userName != "":
                cr.execute(
                    f"UPDATE extradata SET UserName = '{new_userName}' WHERE phone = '{ph}'")
                self.ui.username.setPlaceholderText(new_userName)
                self.ui.user_name.setText(new_userName)
                self.ui.username.setText("")

        elif n == 2:  # edit firt name
            new_firstName = self.ui.firstName.text()
            if new_firstName != "":
                cr.execute(
                    f"UPDATE extradata SET firstN = '{new_firstName}' WHERE phone = '{ph}'")
                self.ui.firstName.setPlaceholderText(new_firstName)
                self.ui.UserFullName.setText(new_firstName + " " + fl[1])
                self.ui.firstName.setText("")

        elif n == 3:  # edit last name
            new_lasstName = self.ui.Lastname.text()
            if new_lasstName != "":
                cr.execute(
                    f"UPDATE extradata SET Lname = '{new_lasstName}' WHERE phone = '{ph}'")
                self.ui.Lastname.setPlaceholderText(new_lasstName)
                self.ui.UserFullName.setText(fl[0] + " " + new_lasstName)
                self.ui.Lastname.setText("")

        # elif n == 4:  # edit phone number
        #     new_phone = self.ui.phoneNumber.text()
        #     if new_phone != "":
        #         cr.execute(
        #             f"UPDATE extradata SET phone = '{new_phone}' WHERE phone = '{ph}'")
        #         cr.execute(
        #             f"UPDATE USERS SET phone = '{new_phone}' WHERE phone = '{ph}'")
        #         self.ui.phoneNumber.setPlaceholderText(new_phone)
        #         self.ui.phoneNumber.setText("")

        elif n == 5:  # edit password
            new_pass = self.ui.password.text()
            if new_pass != "":
                cr.execute(
                    f"UPDATE USERS SET pass = '{new_pass}' WHERE phone = '{ph}'")
                self.ui.password.setPlaceholderText(new_pass)
                self.ui.password.setText("")

        elif n == 6:  # edit bio
            new_bio = self.ui.bio.text()
            if new_bio != "" and len(new_bio) <= 30:
                cr.execute(
                    f"UPDATE extradata SET bio = '{new_bio}' WHERE phone = '{ph}'")
                self.ui.bio.setPlaceholderText(new_bio)
                self.ui.bioContent.setText(new_bio)
                self.ui.bio.setText("")

        elif n == 7:  # change photo
            xpath = QFileDialog.getOpenFileName(
                self, 'Open a file', '', "Images (*.png *.xpm *.jpg *.jpeg)")
            if xpath != ('', ''):
                im1 = Image.open(xpath[0])
                fpath = f"pictures\{ph}.png"
                im1 = im1.save(fpath)
                self.ui.changePhotoButton.setIcon(QIcon(QPixmap(xpath[0])))
                self.ui.changePhotoButton.setIconSize(
                    self.ui.changePhotoButton.size())

        db.commit()
        db.close()

class SplashScreen(QMainWindow, Base):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # set initial progress bar to zero
        self.progressBarValue(0)

        # REMOVE STANDARED TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        # set background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply Drop Shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        # QTIMER
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        ##timer in millisecond
        self.timer.start(15)

        # show
        # self.show()

    # def to loading
    def progress(self):
        global counter
        global jumper
        value = counter

        # HTML text presentage
        htmlText = """
        <p><span style=" font-size:48pt;">{VALUE}</span><span style=" font-size:48pt; vertical-align:super;">%</span></p>
        """
        # Replace value in html
        newHtml = htmlText.replace("{VALUE}", str(jumper))
        if(value > jumper):
            # apply new presentage
            self.ui.labelPercontage.setText(newHtml)
            jumper += 10

        # set value to progress bar
        # fix max value error if > than 100
        if value >= 100:
            value = 1.000
        self.progressBarValue(value)
        # closs splash screen and open app
        if counter > 100:
            # stop timer
            self.timer.stop()
            # show main window
            self.main = WelcomeScreen()
            self.main.show()
            # close splash screen
            # Base.gotoWlcome_screen()
            self.close()

        # increase counter
        counter += 0.5

    # def progressbar
    def progressBarValue(self, value):

        # progressbar stylesheet
        styleSheet = """
        QFrame{
	        border-radius:150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));

             }
        """
        # GUT PROGRESS BAR VALUE,CONVERT TO FLOAT ANDINVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100-value)/100.0
        # GET NEW VALUE
        stop_1 = str(progress-0.001)
        stop_2 = str(progress)
        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace(
            "{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SplashScreen()
    # main = WelcomeScreen()
    main.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
