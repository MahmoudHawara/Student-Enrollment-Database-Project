# from nav_bar_ui import *
from Custom_Widgets.Widgets import *
from PySide2 import *
import sys
from PySide2.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector
from PyQt5.QtGui import QPixmap, QImage

mydb = mysql.connector.connect(
  host="db4free.net",
  user="reemmahmoud",
  password="dbfinalproject",
  database="dbfinalproject"
)

student=0;

class Base():
    cur_theme = 0
    # connect main app to welcome screen
    @staticmethod
    def gotoSingIn():
        main = SignIn()
        main.show()

    # hawara 
    @staticmethod
    def gotoMainPage():
        main = mainwindow()
        main.show()

    @staticmethod
    def gotoStudyGroup():
        main = studyGroupMain()
        main.show()
    # hawara 
    # @staticmethod
    # def gotoStudyGroupCourses():
    #     main = StudyGroupCourses()
    #     main.show()
    
    # rana 
    # @staticmethod
    # def gotoStudyGroupCourses():
    #     main = StudyGroupCourses()
    #     main.show()
    
    @staticmethod
    def gotoStudyGroupStudents():
        main = studyGroupStudents()
        main.show()

    @staticmethod
    def gotoCourse():
        main = courseMain()
        main.show()

    # @staticmethod
    # def gotoStudentCourses():
    #     main = profileCourses()
    #     main.show()
    
    @staticmethod
    def gotoProfile():
        main = profile()
        main.show()
    
    @staticmethod
    def gotoProfileCourses():
        x = profileCourses()
        print(x);
        print(113321);
        x.show()
        print(113321);
    
    def gotoStudyGroupCoursesMainPage():
        x = studyGroupCoursesMainPage()
        print(x);
        x.show()

    @staticmethod
    def gotoStudyGroupCreate():
        main = groupCreation()
        main.show()
    
    @staticmethod
    def gotoStudyGroupEdition():
        main = groupEdition()
        main.show()
        
    @staticmethod
    def gotoStudentAddtion():
        main = studentAddition()
        main.show()
    
    @staticmethod
    def gotoStudentEdition():
        main = studentEdition()
        main.show()
    
    @staticmethod
    def gotoCourseCreate():
        main = courseCreation()
        main.show()
    
    @staticmethod
    def gotoCourseEdition():
        main = courseEdition()
        main.show()

    # @staticmethod
    # def gotocontacts():
    #     contacts = AddContact()
    #     contacts.show()

    # @staticmethod
    # def refresh(obj):
    #     obj.close()
    #     obj.show()



class SignIn(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from sign_H_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.pushButton_4.clicked.connect(self.check)
        # self.header.mouseMoveEvent = self.MoveWindow
    def check(self):
        self.close()
        if(student):
            Base.gotoProfile()
        else:
            Base.gotoMainPage()

class courseCreation(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from coursecreation_H import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.create)
        self.ui.pushButton_5.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
    def create(self):
        self.clear();
    def clear(self):
        self.close()
        Base.gotoStudyGroupCoursesMainPage()
class courseEdition(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from courseEdition_H import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.update)
        self.ui.pushButton_5.clicked.connect(self.delete)
        self.ui.pushButton_6.clicked.connect(self.clear)
        
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
    def update(self):
        self.clear();
    def delete(self):
        self.clear();
    def clear(self):
        self.close()
        Base.gotoCourse()

class groupCreation(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from groupcreation_H_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.create)
        self.ui.pushButton_5.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
    def create(self):
        self.clear()
    def clear(self):
        self.close()
        Base.gotoMainPage()
        # loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow

class groupEdition(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from groupedition_H_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.update)
        self.ui.pushButton_5.clicked.connect(self.delete)
        self.ui.pushButton_6.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
    def update(self):
        self.clear()
    def delete(self):
        self.clear()
    def clear(self):
        self.close()
        Base.gotoMainPage()
        # loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow

class studyGroupMain(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from fsg_H_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.pushButton.clicked.connect(self.StudyGCourses)
        self.ui.pushButton_2.clicked.connect(self.StudyGStudents)
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT COUNT(*) FROM Courses WHERE groupId = {}".format(str(currentStudyGroupID)))
        self.ui.coursesNumber = mycursor.fetchall()[0][0]

        mycursor.execute("SELECT COUNT(*) FROM Students WHERE groupId = {}".format(str(currentStudyGroupID)))
        self.ui.localStudentNumber = mycursor.fetchall()[0][0]
       
        mycursor.execute("SELECT cohortName FROM studyGroups WHERE groupId = {}".format(str(currentStudyGroupID)))
        self.ui.currentStudyGroupName = mycursor.fetchall()[0][0]
        
        mycursor.execute("SELECT image FROM Images WHERE imageName = '4'")
        self.blob_data = mycursor.fetchall()[0][0]
        self.ui.qimage = QImage.fromData(self.blob_data)
        self.ui.studyGroupImage = QPixmap.fromImage(qimage)
        
        mydb.close()
        
        self.ui.separated_SGname = self.currentStudyGroupName.split(',')
        self.ui.label.setText(_translate("MainWindow", self.ui.separated_SGname[0]))
        self.ui.label_3.setText(_translate("MainWindow", self.ui.separated_SGname[1]))
        self.ui.label_2.setText(_translate("MainWindow", self.ui.separated_SGname[2]))
        self.ui.label_5.setText(_translate("MainWindow", str(self.ui.coursesNumber)))
        self.ui.label_7.setText(_translate("MainWindow", str(self.ui.localStudentNumber)))
        self.ui.label_4.setPixmap(self.ui.studyGroupImage)
        
    def StudyGCourses(self):
        self.close()
        Base.gotoStudyGroupCoursesMainPage()

    def StudyGStudents(self):
        self.close()
        Base.gotoStudyGroupStudents()
        # self.header.mouseMoveEvent = self.MoveWindow

class courseMain(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from course import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.pushButton.clicked.connect(self.editcourse)
        
    def editcourse(self):
        self.close()
        Base.gotoCourseEdition()
        # self.header.mouseMoveEvent = self.MoveWindow

class profileCourses(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from profile_c import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        # self.show()
        # self.header.mouseMoveEvent = self.MoveWindow

class profile(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from profile_H_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.mycourses)
        self.ui.pushButton.clicked.connect(self.myset)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
        
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT firstName FROM Students WHERE studentId = {}".format(currentStudentID))
        self.ui.firstName = mycursor.fetchall()[0][0]

        mycursor.execute("SELECT lastName FROM STUDENTS WHERE studentId = {}".format(currentStudentID))
        self.ui.lastName = mycursor.fetchall()[0][0]
        
        mycursor.execute("SELECT profilePhoto FROM STUDENTS WHERE studentId = {}".format(currentStudentID))
        self.ui.blob_data = mycursor.fetchall()[0][0]
        self.ui.qimage = QImage.fromData(self.blob_data)
        self.ui.profile_image = QPixmap.fromImage(qimage)
        mydb.close()
        
        self.ui.label.setText(_translate("MainWindow", self.ui.firstName + ' '+ self.ui.lastName))
        self.ui.label_2.setText(_translate("MainWindow", str(currentStudentID)))
        self.ui.icon5.addPixmap(QtGui.QPixmap(self.ui.profile_image))
        self.ui.label_4.setPixmap(profile_image)
        
    def mycourses(self):
        self.close()
        Base.gotoProfileCourses()
    def myset(self):
        pass
        # self.close()
        # Base.gotoProfileSet()

class studentAddition(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from studentaddition_H_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.add)
        self.ui.pushButton_5.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
    def add(self):
        self.clear()
    def clear(self):
        self.close()
        Base.gotoStudyGroupStudents()
       
class studentEdition(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from studentedition_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.update)
        self.ui.pushButton_3.clicked.connect(self.delete)
        self.ui.pushButton_4.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
    def update(self):
        self.clear();
    def delete(self):
        self.clear();
    def clear(self):
        self.close()
        Base.gotoStudyGroupStudents()
        # loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow

class studyGroupStudents(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from study_g2 import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.pushButton.clicked.connect(self.newstudent)
        self.on_table_changed();
    
    def on_table_changed(self):
                print(f"Table changed: ")
        
        # Clear the table
                db = QSqlDatabase.addDatabase("QSQLITE")
                db.setHostName("localhost")
                db.setDatabaseName("mydatabase.db")
                if not db.open():
                        print("Cannot open database")
                        sys.exit(1)
                self.ui.table.clearContents()
                self.ui.table.setRowCount(0)
                
                # Refetch data from the database
                query = QSqlQuery()
                query.prepare("SELECT * from Persons3;")
                if not query.exec_():
                        print("Cannot execute query")
                        sys.exit(1)
                
                # Repopulate the table with data from the database
                self.ui.table.setColumnCount(query.record().count()+1)
                # self.table.setRowCount(query.size())
                
                self.ui.table.setHorizontalHeaderLabels([query.record().fieldName(i) for i in range(query.record().count())])
                self.ui.table.horizontalHeader()
                while query.next():
                        row = self.ui.table.rowCount()
                        self.ui.table.insertRow(row)
                        for column in range(query.record().count()):
                                item = QTableWidgetItem(str(query.value(column)))
                                item.setTextAlignment(Qt.AlignCenter);
                                # item(QColor(255, 255, 255))  # Set text color to blue
                                self.ui.table.setItem(row, column, item)
                        button = QPushButton("Click Me")
                        button.setObjectName("but_"+str(row))
                        button.clicked.connect(self.on_button_clicked)
                        self.ui.table.setCellWidget(row, query.record().count(), button)
                        
                
                odd_color = QColor(22,33,62) # light gray
                even_color = QColor(15, 52, 96)  # darker gray
                print(self.ui.table.rowCount())
                # Use a stylesheet to set background colors for odd and even rows
                self.ui.table.setStyleSheet(f"QTableView {{ alternate-background-color: {odd_color.name()};background-color: {even_color.name()};border:none;padding:0;}} "
                                        f"QTableWidget::item {{color: white;border:none;}}"
                                        "QTableWidget::section {{ border: none;padding:none; }}"
                                        # f"QHeaderView  {{ background-color: {even_color.name()}; }} "
                                        # f"QHeaderView::item {{color: white;}}"
                                        )
                self.ui.table.horizontalHeader().setStyleSheet(f"QHeaderView::section {{color: white; background-color:{odd_color.name()}; border: none; }}"
                                                        "QHeaderView::section:hover { background-color: odd_color.name(); border: none;padding:none; }")
                self.ui.table.verticalHeader().setVisible(False);
                
                # self.table.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 10px; }")
                # self.table.verticalScrollBar().setStyleSheet("QScrollBar:vertical { width: 10px; } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { height: 0px; }")
                # self.table.verticalScrollBar().
                self.ui.table.verticalScrollBar().setStyleSheet("""QScrollBar:vertical {
                width: 2px;
                background: #f1f1f1;
                }

                QScrollBar::handle:vertical {
                background: #888;
                }

                QScrollBar::add-line:vertical {
                border: 2px solid gray;
                background: #f1f1f1;
                }

                QScrollBar::sub-line:horizontal {
                border: 2px solid gray;
                background: #f1f1f1;
                }

                QScrollBar::handle:hover:vertical {
                background: #555;
                }"""
                )
                # self.table.horizontalHeader().setStyleSheet(
                #                         )
                self.ui.table.setAlternatingRowColors(True)
    def on_button_clicked(self):
        # print(bu);
        sending_button = self.sender()
        print('%s Clicked!' % str(sending_button.objectName()))
        # This method will be called when the button is clicked
        print("Button clicked")

    def newstudent(self):
            self.close()
            Base.gotoStudentAddtion()
        # self.header.mouseMoveEvent = self.MoveWindow

class studyGroupCoursesMainPage(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from courseMainPage_H_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.pushButton.clicked.connect(self.newcourse)
    
    def newcourse(self):
            self.close()
            Base.gotoCourseCreate()
        # self.header.mouseMoveEvent = self.MoveWindow
class mainwindow(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from adminMainPage_H_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # nam="PU_"+str(id)
        self.ui.pushButton.clicked.connect(self.newstudygroup)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
    def newstudygroup(self):
        self.close()
        Base.gotoStudyGroupCreate()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignIn()
    window.show()
    # widget = QStackedWidget()
    # widget.setWindowFlags(Qt.CustomizeWindowHint)
    # widget.setWindowFlags(Qt.FramelessWindowHint)
    # mainwindow = MainWindow()
    # exscreen1 = exScreen1()
    # invscreen1 = invScreen1()
    # helpinv = invHelp()
    # helpexam = examHelp()
    # widget.addWidget(window)
    # widget.addWidget(mainwindow)
    # widget.addWidget(exscreen1)
    # widget.addWidget(invscreen1)
    # widget.addWidget(helpinv)
    # widget.addWidget(helpexam)
    # widget.setMinimumWidth(900)
    # widget.setMinimumHeight(750)
    # widget.move(300, 0)
    # widget.show()
    sys.exit(app.exec_())
