# from nav_bar_ui import *
from Custom_Widgets.Widgets import *
from PySide2 import *
import sys
import pymysql
from PySide2.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector
# from PyQt5.QtGui import QPixmap, QImage
import input_checker as c
import datetime

mydb = mysql.connector.connect(
  host="db4free.net",
  user="learnloop",
  password="learnloop5",
  database="learnloop"
)

student=0;
currentStudyGroupID=2;
currentStudentID=2;
currentCourseID=16;
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
        if(student):
            main=profile2()
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
    def gotoadminpro():
        main =adminprofile()
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
        from signIn_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.label_8.setText("") # FOR EMAIL 
        self.ui.label_5.setText("") #FOR PASSWORD 
        self.ui.pushButton_4.clicked.connect(self.check)
        # self.header.mouseMoveEvent = self.MoveWindow
        # cursor = mydb.cursor()
        # cursor.execute("SELECT * FROM Students")
        # results = cursor.fetchall()
        # print(results)
        # cursor.close()
    def check(self):
      
        
        checkDuplicate = 0;
        cursor = mydb.cursor()

        # Get the email and password entered by the user
        email = self.ui.lineEdit_6.text()
        password = self.ui.lineEdit_8.text()

        # Hide both error labels
        self.ui.label_8.setText("") # FOR EMAIL 
        self.ui.label_5.setText("") #FOR PASSWORD 

        # Check if there is a record in the database with the given email address
        sql = "SELECT * FROM Students WHERE email = %s"
        params = (email,)
        cursor.execute(sql, params)
        results = cursor.fetchall()

        if len(results) == 0:
            self.ui.label_8.setText("E-Mail is Invalid")

        # Check if the password is correct for the record with the given email address
        sql = "SELECT * FROM Students WHERE email = %s AND password = %s"
        params = (email, password)
        cursor.execute(sql, params)
        results = cursor.fetchall()

        if len(results) == 0:
            self.ui.label_5.setText("Password is Incorrect")

        # If both the email and password are incorrect, display both error messages
        elif len(results) == 0 and len(results) == 0:
            self.ui.label_8.setText("E-Mail is Invalid")
            self.ui.label_5.setText("Password is Incorrect")
        else:
        # Login successful, do something here
            checkDuplicate = 1;
            global student
            if len(results) == 1:
                user_id = results[0][0]  # the ID is in the first column of the result
                if user_id==1:
                #CHANGE THE GLOBAL VARIABLE STUDENT = 1 FOR ADMIN 
                    student = 0;
                else:
                    student = 1;
            if checkDuplicate:
                self.close()

                if(student):
                    Base.gotoProfile()
                else:
                    Base.gotoMainPage()
# (1, 1, 'Admin', 'Admin', '11111111111', datetime.date(2000, 1, 1), 'male', 'admin@learnloop.com', 'password123'
class courseCreation(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from courseCreation_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.create)
        self.ui.pushButton_5.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
        self.ui.label_8.setVisible(False)
        self.ui.label_5.setVisible(False)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(100)
        # Store the last known size of the window
        self.last_size = self.size()

    def on_timer(self):
        # This function is called every 100ms by the timer
        if self.width() != self.last_size.width():
            inc = 0.5 * (self.width() - self.last_size.width())
            self.ui.logo_2.setMinimumWidth(self.ui.logo_2.minimumWidth() + int(inc))
            self.last_size = self.size()
    def create(self):
        courseName = self.ui.lineEdit_6.text()
        courseNum = self.ui.lineEdit_8.text()
        self.ui.label_8.setVisible(False)
        self.ui.label_5.setVisible(False)
        self.ui.label_6.setText("")
        
        rightName = 0
        rightNum = 0
        if not(c.check_course_name(courseName)) or not(c.checkNotEmpty(courseName)):
            self.ui.label_8.setVisible(True)
        else:
            self.ui.label_8.setVisible(False)
            rightName = 1
        if not(c.check_digits_only(courseNum)) or not(c.checkNotEmpty(courseNum)):
            self.ui.label_5.setVisible(True)
        else:
            self.ui.label_5.setVisible(False)
            rightNum = 1
        
        if rightName and rightNum:
            nameNotduplicated = 0
            numNotduplicated = 0
            cursor = mydb.cursor()

            # Get the course name, hours entered by the user
            course_name = self.ui.lineEdit_6.text()
            hours = self.ui.lineEdit_8.text()
            term = self.ui.comboBox_2.currentText()

            # Hide any existing error message
            self.ui.label_6.setText("")

            # Check if a record with the given course name already exists
            sql = "SELECT * FROM Courses WHERE courseName = %s and groupId = %s"
            params = (course_name,currentStudyGroupID)
            cursor.execute(sql, params)
            results = cursor.fetchall()

            if len(results) > 0:
                self.ui.label_6.setText("There is another Course with The Same Name")
            else:
                # Insert a new record into the database
                sql = "INSERT INTO Courses (groupId, courseName, numberOfHours, term) VALUES (%s, %s, %s, %s)"
                params = (currentStudyGroupID, course_name, hours, term)
                cursor.execute(sql, params)
                mydb.commit()
                nameNotduplicated = 1

                # Fetch all the student IDs in the group
                sql = "SELECT studentId FROM Students WHERE groupId = %s"
                params = (currentStudyGroupID,)
                cursor.execute(sql, params)
                results = cursor.fetchall()

                if len(results) > 0:
                    # Get the courseId of the newly added course
                    sql = "SELECT courseId FROM Courses WHERE courseName = %s"
                    params = (course_name,)
                    cursor.execute(sql, params)
                    courseId = cursor.fetchone()[0]

                    # Insert a new record into the StudentCourses table for each student in the group
                    for result in results:
                        studentId = result[0]
                        sql = "INSERT INTO StudentsWithCourses (studentId, courseId, courseGrade,groupId ) VALUES (%s, %s, %s, %s)"
                        params = (studentId, courseId,  -1, currentStudyGroupID)
                        cursor.execute(sql, params)
                        mydb.commit()
                    numNotduplicated = 0

                # Show a notification that the record was inserted successfully
                # self.show_notification("Success", "Record inserted successfully")
                if nameNotduplicated and numNotduplicated:
                  self.clear();
    def show_notification(title, message):
            # Create a system tray icon and show a notification
            tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("path/to/icon.png"), parent=app)
            tray_icon.show()
            tray_icon.showMessage(title, message, QtWidgets.QSystemTrayIcon.Information)
                
    def clear(self):
         self.close()
         Base.gotoStudyGroupCoursesMainPage()
                
class courseEdition(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from courseEdition_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.update)
        self.ui.pushButton_5.clicked.connect(self.delete)
        self.ui.pushButton_6.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
        self.ui.label_8.setVisible(False)
        self.ui.label_5.setVisible(False)
        self.ui.label_6.setText("")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(100)
        # Store the last known size of the window
        self.last_size = self.size()
        

    def on_timer(self):
        # This function is called every 100ms by the timer
        if self.width() != self.last_size.width():
            inc = 0.5 * (self.width() - self.last_size.width())
            self.ui.logo_2.setMinimumWidth(self.ui.logo_2.minimumWidth() + int(inc))
            self.last_size = self.size()
        
    def update(self):
        courseName = self.ui.lineEdit_6.text()
        courseNum = self.ui.lineEdit_8.text()
        self.ui.label_8.setVisible(False)
        self.ui.label_5.setVisible(False)
        rightName = 0
        self.ui.label_6.setText("")
        
        rightNum = 0
        if not(c.check_course_name(courseName)) or not(c.checkNotEmpty(courseName)):
            self.ui.label_8.setVisible(True)
        else:
          self.ui.label_8.setVisible(False)
          rightName = 1
        if not(c.check_digits_only(courseNum)) or not(c.checkNotEmpty(courseNum)):
          self.ui.label_5.setVisible(True)
        else:
          self.ui.label_5.setVisible(False)
          rightNum = 1
        
        if rightName and rightNum:
            nameNotduplicated = 0
            numNotduplicated = 0
            cursor = mydb.cursor()

            # Get the course name, hours entered by the user
            course_name = self.ui.lineEdit_6.text()
            hours = self.ui.lineEdit_8.text()
            term = self.ui.comboBox_2.currentText()

            # Hide any existing error message
            self.ui.label_6.setText("")

            # Check if a record with the given course name already exists
            sql = "SELECT * FROM Courses WHERE courseName = %s and groupId = %s"
            params = (course_name, currentStudyGroupID)
            cursor.execute(sql, params)
            results = cursor.fetchall()

            if len(results) > 0:
                self.ui.label_6.setText("There is another Course with The Same Name")
            else:
                sql = "UPDATE Courses SET courseName = %s, numberOfHours = %s, term = %s WHERE courseId = %s;"
                params = (course_name, hours, term, currentCourseID)
                cursor.execute(sql, params)
                #results = cursor.fetchall()
                
                # Insert a new record into the database
                # sql = "INSERT INTO Courses (groupId, courseName, numberOfHours, term) VALUES (%s, %s, %s, %s)"
                # params = (currentStudyGroupID, course_name, hours, term)
                # cursor.execute(sql, params)
                # mydb.commit()
                # nameNotduplicated = 1

                # # Fetch all the student IDs in the group
                # sql = "SELECT studentId FROM Students WHERE groupId = %s"
                # params = (currentStudyGroupID,)
                # cursor.execute(sql, params)
                # results = cursor.fetchall()

                # if len(results) > 0:
                #     # Get the courseId of the newly added course
                #     sql = "SELECT courseId FROM Courses WHERE courseName = %s"
                #     params = (course_name,)
                #     cursor.execute(sql, params)
                #     courseId = cursor.fetchone()[0]

                #     # Insert a new record into the StudentCourses table for each student in the group
                #     for result in results:
                #         studentId = result[0]
                #         sql = "INSERT INTO StudentsWithCourses (studentId, courseId, courseGrade,groupId ) VALUES (%s, %s, %s, %s)"
                #         params = (studentId, courseId,  -1, currentStudyGroupID)
                #         cursor.execute(sql, params)
                mydb.commit()
                # numNotduplicated = 1

                # Show a notification that the record was inserted successfully
                # self.show_notification("Success", "Record inserted successfully")
                # if nameNotduplicated and numNotduplicated:
                self.clear()
                
    def delete(self):
        courseFound = 0
        cursor = mydb.cursor()

        # Get the course name entered by the user
        # course_name = self.ui.lineEdit_6.text()

        # Hide any existing error message
        #ui.label_6.setText("")

        # Check if a record with the given course name exists
        # Delete all the records for the given course in the StudentsWithCourses table
        sql = "DELETE FROM StudentsWithCourses WHERE courseId = %s"
        params = (currentCourseID,)
        cursor.execute(sql, params)
        sql = "DELETE FROM Courses WHERE courseId = %s"
        params = (currentCourseID,)
        cursor.execute(sql, params)
        mydb.commit()

        # Delete the record for the given course in the Courses table
        # sql = "DELETE FROM Courses WHERE courseName = %s"
        # params = (course_name,)
        # cursor.execute(sql, params)
        # mydb.commit()
        # courseFound = 1
        # Show a notification that the record was deleted successfully
        # self.show_notification("Success", "Record deleted successfully")
        # if courseFound:
        self.clear()

    def show_notification(title, message):
        # Create a system tray icon and show a notification
        tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("path/to/icon.png"), parent=app)
        tray_icon.show()
        tray_icon.showMessage(title, message, QtWidgets.QSystemTrayIcon.Information)
    def clear(self):
        self.close()
        Base.gotoCourse()

class groupCreation(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from studyGroupCreation_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_8.setVisible(False)
        self.ui.label_5.setVisible(False)
        self.ui.pushButton_4.clicked.connect(self.create)
        self.ui.pushButton_5.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
        self.ui.label_8.setVisible(False)
        self.ui.label_6.setText("")
        
        self.ui.label_5.setVisible(False)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(100)
        # Store the last known size of the window
        self.last_size = self.size()

    def on_timer(self):
        # This function is called every 100ms by the timer
        if self.width() != self.last_size.width():
            inc = 0.5 * (self.width() - self.last_size.width())
            self.ui.logo_2.setMinimumWidth(self.ui.logo_2.minimumWidth() + int(inc))
            self.last_size = self.size()
    def create(self):
        cohortName = self.ui.lineEdit_6.text()
        cohortNum = self.ui.lineEdit_8.text()
        self.ui.label_8.setVisible(False)
        self.ui.label_5.setVisible(False)
        
        rightName = 0
        rightNum = 0
        if not(c.check_letters_only(cohortName)) or not(c.checkNotEmpty(cohortName)):
            self.ui.label_8.setVisible(True)
        else:
            self.ui.label_8.setVisible(False)
            rightName = 1
        if not(c.check_digits_only(cohortNum)) or not(c.checkNotEmpty(cohortNum)):
            self.ui.label_5.setVisible(True)
        else:
            self.ui.label_5.setVisible(False)
            rightNum = 1
        
        if rightName and rightNum:
            NotDuplicate = 0
        
            # Create a cursor object to execute SQL queries
            cursor = mydb.cursor()

            # Get the cohort name and number entered by the user
            cohort_name = self.ui.lineEdit_6.text()
            cohort_number = self.ui.lineEdit_8.text()

            # Hide any existing error message
            self.ui.label_6.setText("")

            # Check if a record with the given cohort name and number already exists
            sql = "SELECT * FROM studyGroups WHERE cohortName=%s AND cohortNumber=%s"
            params = (cohort_name, cohort_number)
            cursor.execute(sql, params)
            results = cursor.fetchall()
            if len(results) > 0:
                self.ui.label_6.setText("There is already a study group with the same cohort name and number.")
            else:
                # Insert a new record into the database
                sql = "INSERT INTO studyGroups (cohortName, cohortNumber) VALUES (%s, %s)"
                params = (cohort_name, cohort_number)
                cursor.execute(sql, params)
                mydb.commit()
                NotDuplicate = 1
                # Show a notification that the record was inserted successfully
                # self.show_notification("Success", "Record inserted successfully")
            if NotDuplicate:
                self.clear()

    
    def show_notification(title, message):
        # Create a system tray icon and show a notification
        tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("path/to/icon.png"), parent=app)
        tray_icon.show()
        tray_icon.showMessage(title, message, QtWidgets.QSystemTrayIcon.Information)

        
    def clear(self):
        self.close()
        Base.gotoMainPage()
        # loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
        
        
        
        

class groupEdition(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from studyGroupEdition_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.update)
        self.ui.pushButton_5.clicked.connect(self.delete)
        self.ui.pushButton_6.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
        self.ui.label_8.setVisible(False)
        self.ui.label_5.setVisible(False)
        self.ui.label_6.setText("")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(100)
        # Store the last known size of the window
        self.last_size = self.size()

    def on_timer(self):
        # This function is called every 100ms by the timer
        if self.width() != self.last_size.width():
            inc = 0.5 * (self.width() - self.last_size.width())
            self.ui.logo_2.setMinimumWidth(self.ui.logo_2.minimumWidth() + int(inc))
            self.last_size = self.size()
    def update(self):
        cohortName = self.ui.lineEdit_6.text()
        cohortNum = self.ui.lineEdit_8.text()
        self.ui.label_8.setVisible(False)
        self.ui.label_5.setVisible(False)
        rightName = 0
        rightNum = 0
        if not(c.check_letters_only(cohortName)) or not(c.checkNotEmpty(cohortName)):
            self.ui.label_8.setVisible(True)
        else:
            self.ui.label_8.setVisible(False)
            rightName = 1
        if not(c.check_digits_only(cohortNum)) or not(c.checkNotEmpty(cohortNum)):
            self.ui.label_5.setVisible(True)
        else:
            self.ui.label_5.setVisible(False)
            rightNum = 1
        
        if rightName and rightNum:
            global currentStudyGroupID
            # Create a cursor object to execute SQL queries
            cursor = mydb.cursor()

            # Get the cohort name and number entered by the user
            cohort_name = self.ui.lineEdit_6.text()
            cohort_number = self.ui.lineEdit_8.text()

            # Hide any existing error message
            self.ui.label_6.setText("")
            print(cohort_name)
            print(cohort_number)
            print(currentStudyGroupID)
            # Check if a record with the given cohort name and number already exists
            sql = "SELECT * FROM studyGroups WHERE cohortName=%s AND cohortNumber=%s"
            params = (cohort_name, cohort_number)
            cursor.execute(sql, params)
            results = cursor.fetchall()

            if len(results) > 0:
                # Display an error message saying that the record already exists
                self.ui.label_6.setText("A study group already exists with the given cohort name and number")

            else:
                self.ui.label_6.setText("ok")
                sql = "UPDATE studyGroups SET cohortName = %s , cohortNumber = %s WHERE groupId = %s;" 
                params = (cohort_name, cohort_number, currentStudyGroupID)
                cursor.execute(sql, params)
                mydb.commit()
                self.clear()
                        #         self.clear()
                        # Check if a record with the given cohort number and group ID exists
                        # sql = "SELECT * FROM studyGroups WHERE cohortNumber=%s AND groupId=%s"
                        # params = (cohort_number, currentStudyGroupID)
                        # cursor.execute(sql, params)
                        # results = cursor.fetchall()

                        # if len(results) > 0:
                        #     # Update the cohort name with the given input
                        #     sql = "UPDATE studyGroups SET cohortName=%s WHERE groupId=%s"
                        #     params = (cohort_name, currentStudyGroupID)
                        #     cursor.execute(sql, params)
                        #     mydb.commit()
                            
                        #     # show_notification("Success", "Record deleted successfully")
                            
                        # else:
                        #     # Check if a record with the given cohort name and group ID exists
                        #     sql = "SELECT * FROM studyGroups WHERE cohortName=%s AND groupId=%s"
                        #     params = (cohort_name, currentStudyGroupID)
                        #     cursor.execute(sql, params)
                        #     results = cursor.fetchall()

                        #     if len(results) > 0:
                        #         # Update the cohort number with the given input
                        #         sql = "UPDATE studyGroups SET cohortNumber=%s WHERE groupId=%s"
                        #         params = (cohort_number, currentStudyGroupID)
                        #         cursor.execute(sql, params)
                        #         
                        #         # show_notification("Success", "Record deleted successfully")
                        #     else:
                        #         self.ui.label_6.setText("No study group found with the given cohort name and group ID")
                    # pass
                        
                #check database part
    def delete(self):
        
            global currentStudyGroupID
            # Create a cursor object to execute SQL queries
            cursor = mydb.cursor()

            # Get the cohort name and number entered by the user
            # cohort_name = self.ui.lineEdit_6.text()
            # cohort_number = self.ui.lineEdit_8.text()

            # Hide any existing error message
            self.ui.label_6.setText("")

            # Check if a record with the given cohort name and number already exists
            # sql = "SELECT * FROM studyGroups WHERE cohortName=%s AND cohortNumber=%s"
            # params = (cohort_name, cohort_number)
            # cursor.execute(sql, params)
            # results = cursor.fetchall()

            # if len(results) > 0:
            #     # Display an error message saying that the record already exists
            #     self.ui.label_6.setText("A study group already exists with the given cohort name and number")

            # else:
            sql = "DELETE FROM studyGroups WHERE groupId = %s;" 
            params = (currentStudyGroupID,)
            cursor.execute(sql, params)
            
            sql = "DELETE FROM Students WHERE groupId = %s;" 
            params = (currentStudyGroupID,)
            cursor.execute(sql, params)
            
            sql = "DELETE FROM Courses WHERE groupId = %s;" 
            params = (currentStudyGroupID,)
            cursor.execute(sql, params)
            
            sql = "DELETE FROM StudentsWithCourses WHERE groupId = %s;" 
            params = (currentStudyGroupID,)
            cursor.execute(sql, params)
            
            mydb.commit()
            self.clear()
                
    def clear(self):
        self.close()
        Base.gotoMainPage()
        # loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow

class studyGroupMain(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from studyGroupMainPage_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.pushButton_3.clicked.connect(self.StudyGCourses)
        self.ui.pushButton_2.clicked.connect(self.StudyGStudents)
        self.ui.settings_2.clicked.connect(self.stt)
        self.ui.expand_3.clicked.connect(self.back)
        self.ui.profilePhoto_2.clicked.connect(self.gotomain)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT COUNT(*) FROM Courses WHERE groupId = {}".format(str(currentStudyGroupID)))
        coursesNumber = mycursor.fetchall()[0][0]

        mycursor.execute("SELECT COUNT(*) FROM Students WHERE groupId = {}".format(str(currentStudyGroupID)))
        localStudentNumber = mycursor.fetchall()[0][0]
       
        mycursor.execute("SELECT cohortNumber,cohortName FROM studyGroups WHERE groupId = {}".format(str(currentStudyGroupID)))
        currentStudyGroupName = mycursor.fetchall()[0]
        
        mycursor.execute("SELECT image FROM Images WHERE imageName = '2'")
        blob_data = mycursor.fetchall()[0][0]
        qimage = QImage.fromData(blob_data)
        studyGroupImage = QPixmap.fromImage(qimage)
        
        mycursor.close()
        print(currentStudyGroupName)
        # separated_SGname = currentStudyGroupName.split(',')
        self.ui.label_9.setText( str(currentStudyGroupName[0]))
        self.ui.label_10.setText( "st")
        self.ui.label_14.setText( str(currentStudyGroupName[1]))
        self.ui.label_11.setText( str(coursesNumber))
        self.ui.label_7.setText(str(localStudentNumber))
        self.ui.label_4.setPixmap(studyGroupImage)
    def stt(self):
        self.close()
        Base.gotoadminpro()
    def back(self):
        self.close()
        Base.gotoMainPage()
    def StudyGCourses(self):
        self.close()
        Base.gotoStudyGroupCoursesMainPage()

    def StudyGStudents(self):
        self.close()
        Base.gotoStudyGroupStudents()
        # self.header.mouseMoveEvent = self.MoveWindow
    def gotomain(self):
        self.close()
        Base.gotoMainPage()

class adminprofile(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from adminProfile_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        # self.ui.pushButton.clicked.connect(self.editcourse)
    
    
    

class courseMain(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from course import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.pushButton.clicked.connect(self.editcourse)
        self.ui.settings_2.clicked.connect(self.stt)

        
    def editcourse(self):
        self.close()
        Base.gotoCourseEdition()
        # self.header.mouseMoveEvent = self.MoveWindow
    def stt(self):
        self.close()
        Base.gotoadminpro()

class profileCourses(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from profile_c import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.lineEdit.textChanged.connect(self.search)
        self.ui.settings_2.clicked.connect(self.stt)

        # self.ui.mode.clicked.connect(self.mode)
        self.mydata=[];

    def search(self):
        srch = self.ui.lineEdit.text()
        if srch != "":
            nedata=[]
            for record in self.ui.mydata:
                if srch in str(record[0]):
                    nedata.append(record)
                elif srch in record[1]:
                    nedata.append(record)
                elif srch in record[2]:
                    nedata.append(record)
            self.ui.on_table_changed(nedata)
        else:
            self.ui.on_table_changed(self.ui.mydata)
        # self.show()
        # self.header.mouseMoveEvent = self.MoveWindow
    def stt(self):
        self.close()
        Base.gotoadminpro()

class profile(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from studentProfileFromAdmin_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.mycourses)
        self.ui.pushButton_3.clicked.connect(self.myset)
        self.ui.settings_2.clicked.connect(self.stt)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
        
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT firstName FROM Students WHERE studentId = {}".format(currentStudentID))
        s = mycursor.fetchall()[0][0]

        mycursor.execute("SELECT lastName FROM Students WHERE studentId = {}".format(currentStudentID))
        s2= mycursor.fetchall()[0][0]
        self.ui.label_14.setText(s)
        mycursor.execute("SELECT profilePhoto FROM Students WHERE studentId = {}".format(currentStudentID))
        blob_data = mycursor.fetchall()[0][0]
        qimage = QImage.fromData(blob_data)
        profilePhoto = QPixmap.fromImage(qimage)
        mycursor.close()
        
        self.ui.label_14.setText( s + ' '+ s2)
        self.ui.label_10.setText(str(currentStudentID))
        # self.ui.icon5.addPixmap(QPixmap(profilePhoto))
        # self.ui.label_4.setPixmap(QPixmap(profilePhoto))
        
    def mycourses(self):
        self.close()
        Base.gotoProfileCourses()
    def stt(self):
        self.close()
        Base.gotoadminpro()
    def myset(self):
        pass
        # self.close()
        # Base.gotoProfileSet()
class profile2(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from studentProfileFromStudent_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.mycourses)
        self.ui.pushButton_3.clicked.connect(self.myset)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
        
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT firstName FROM Students WHERE studentId = {}".format(currentStudentID))
        s = mycursor.fetchall()[0][0]

        mycursor.execute("SELECT lastName FROM Students WHERE studentId = {}".format(currentStudentID))
        s2= mycursor.fetchall()[0][0]
        self.ui.label_14.setText(s)
        mycursor.execute("SELECT profilePhoto FROM Students WHERE studentId = {}".format(currentStudentID))
        blob_data = mycursor.fetchall()[0][0]
        qimage = QImage.fromData(blob_data)
        profilePhoto = QPixmap.fromImage(qimage)
        mycursor.close()
        
        self.ui.label_14.setText( s + ' '+ s2)
        self.ui.label_10.setText(str(currentStudentID))
        # self.ui.icon5.addPixmap(QPixmap(profilePhoto))
        # self.ui.label_4.setPixmap(QPixmap(profilePhoto))
        
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
        from studentAddition_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.add)
        self.ui.pushButton_5.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
        self.ui.label_17.setVisible(False)
        self.ui.label_27.setVisible(False)
        self.ui.label_31.setVisible(False)
        self.ui.label_30.setVisible(False)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(100)
        # Store the last known size of the window
        self.last_size = self.size()

    def on_timer(self):
        # This function is called every 100ms by the timer
        if self.width() != self.last_size.width():
            inc = 0.5 * (self.width() - self.last_size.width())
            self.ui.logo_2.setMinimumWidth(self.ui.logo_2.minimumWidth() + int(inc))
            self.last_size = self.size()
    def add(self):
        firstName = self.ui.lineEdit_12.text()
        lastName = self.ui.lineEdit_18.text()
        phone = self.ui.lineEdit_20.text()
        ID = self.ui.lineEdit_19.text()
        self.ui.label_17.setVisible(False)
        self.ui.label_27.setVisible(False)
        self.ui.label_31.setVisible(False)
        self.ui.label_30.setVisible(False)
        rightFirst = 0
        rightSecond = 0
        rightPhone = 0
        rightId = 0
        
        if not(c.check_letters_only(firstName)) or not(c.checkNotEmpty(firstName)):
            self.ui.label_17.setVisible(True)
        else:
            self.ui.label_17.setVisible(False)
            rightFirst = 1
          
        if not(c.check_letters_only(lastName)) or not(c.checkNotEmpty(lastName)):
            self.ui.label_27.setVisible(True)
        else:
            self.ui.label_27.setVisible(False)
            rightSecond = 1
        if not(c.check_ID(ID)) or not(c.checkNotEmpty(ID)):
            self.ui.label_31.setVisible(True)
        else:
            self.ui.label_31.setVisible(False)
            rightId = 1
          
        if not(c.check_phone_number(phone)) or not(c.checkNotEmpty(phone)):
            self.ui.label_30.setVisible(True)
        else:
            self.ui.label_30.setVisible(False)
            rightPhone = 1
        
        if rightFirst and rightSecond and rightPhone and rightId:
            mycursor = mydb.cursor()
            studentNotduplicated = 0
            # Get the course name, hours entered by the user
            firstName = self.ui.lineEdit_12.text()
            lastName = self.ui.lineEdit_18.text()
            phone = self.ui.lineEdit_20.text()
            ID = self.ui.lineEdit_19.text()
            gender = self.ui.comboBox_2.currentText()
            BDate = self.ui.dateEdit.date().toString('yyyy-MM-dd')
            
            
            # qdatetime_obj = QDateTime.fromString(BDate, 'yyyy-MM-dd')
            # mysql_date = qdatetime_obj.date()
            # qtime_obj = QTime(0, 0, 0)
            # qdatetime_obj = QDateTime( mysql_date, qtime_obj, Qt.LocalTime).toString('yyyy-MM-dd')
            # Hide any existing error message
            #ui.label_6.setText("")            

            sql = "SELECT * FROM Students WHERE studentId = %s"
            params = (ID,)
            mycursor.execute(sql, params)
            results = mycursor.fetchall()
            self.ui.label_6.setText("")
            if len(results) > 0:
                self.ui.label_6.setText("There is another Student with The ID")
            else:
                self.ui.label_6.setText("ok")
                # Insert a new record into the database
                mycursor.execute("SELECT image FROM Images WHERE imageName = 'user' ")
                blob_data = mycursor.fetchall()[0][0]
                # qimage = QImage.fromData(blob_data)
                # defultImage = QPixmap.fromImage(qimage)    
                
                # image_bytes = QByteArray()
                # buffer = QBuffer(blob_data)
                # buffer.open(QIODevice.WriteOnly)
                # my_qpixmap.save(buffer, "PNG")  # save the qpixmap as a PNG image
                # buffer.close()

                # insert the binary data into the MySQL database table
                #cursor.execute("INSERT INTO my_table (image_column) VALUES (%s)", [bytes(image_bytes)])
                
            #     add_student = ("INSERT INTO students "
            #    "(ID, StudyGroupID, FirstName, LastName, Phone, BDate, Gender, Email, UserName, ProfilePic) "
            #    "VALUES (%s, %s, %s, %s, %s, STR_TO_DATE(%s, '%%M %%d, %%Y'), %s, %s, %s, %s)")

            #     # Define the values to insert into the query
            #     data_student = (ID, currentStudyGroupID, firstName, lastName, phone, BDate, gender, str(ID)+ "@learnloop.edu.eg", firstName+ID ,blob_data)
                
                BDate = self.ui.dateEdit.date().toString('MM-dd-yyyy')
                # STR_TO_DATE(%s, '%%M %%d, %%Y')
                # mycursor.execute("SELECT image FROM Images WHERE imageName = 'user' ")
                # blob_data = mycursor.fetchall()[0][0]
                # qimage = QImage.fromData(blob_data)
                # defultImage = QPixmap.fromImage(qimage)    
                sql = "INSERT INTO Students (studentId, groupId, firstName, lastName, phoneNumber, birthDate, gender, email, password, profilePhoto) VALUES (%s, %s, %s, %s, %s,%s, %s, %s,%s, %s)"
                params = (ID, currentStudyGroupID, firstName, lastName, phone, BDate, gender, str(ID)+ "@learnloop.edu.eg", firstName+ID ,blob_data)
                mycursor.execute(sql, params)
                mydb.commit()
                studentNotduplicated = 1
                # sql = "INSERT INTO Students (studentId, groupId, firstName, lastName, phoneNumber, birthDate, gender, email, password, profilePhoto) VALUES (%s, %s, %s, %s,%s, STR_TO_DATE(%s, '%%M %%d, %%Y'), %s, %s,%s, %s)"
                # params = (ID, currentStudyGroupID, firstName, lastName, phone, BDate, gender, str(ID)+ "@learnloop.edu.eg", firstName+ID ,blob_data)
                # mycursor.execute(sql, params)
                # mydb.commit()
                # studentNotduplicated = 1
                self.ui.label_6.setText("OKKKKKKK")
                # Fetch all the student IDs in the group
                sql = "SELECT courseId FROM Courses WHERE groupId = %s"
                params = (currentStudyGroupID,)
                mycursor.execute(sql, params)
                results = mycursor.fetchall()
                if len(results) > 0:
                    # Insert a new record into the StudentCourses table for each student in the group
                    for result in results:
                        courseId = result[0]
                        sql = "INSERT INTO StudentsWithCourses (studentId, courseId, courseGrade, groupId ) VALUES (%s, %s, %s, %s)"
                        params = (ID, courseId,  -1, currentStudyGroupID)
                        mycursor.execute(sql, params)
                        mydb.commit()
                    if studentNotduplicated:
                          self.clear()
                    # if NotDuplicate:
                    #     self.clear()
                    #     show_notification("Success", "Record inserted successfully")

    
    def show_notification(title, message):
        # Create a system tray icon and show a notification
        tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("path/to/icon.png"), parent=app)
        tray_icon.show()
        tray_icon.showMessage(title, message, QtWidgets.QSystemTrayIcon.Information)
        
    def clear(self):
        self.close()
        Base.gotoStudyGroupStudents()
       
class studentEdition(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from studentEdition_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.update)
        self.ui.pushButton_3.clicked.connect(self.delete)
        self.ui.pushButton_4.clicked.connect(self.clear)
        loadJsonStyle(self, self.ui)
        # self.header.mouseMoveEvent = self.MoveWindow
        self.ui.label_17.setVisible(False)
        self.ui.label_27.setVisible(False)
        self.ui.label_31.setVisible(False)
        self.ui.label_30.setVisible(False)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(100)
        # Store the last known size of the window
        self.last_size = self.size()

    def on_timer(self):
        # This function is called every 100ms by the timer
        if self.width() != self.last_size.width():
            inc = 0.5 * (self.width() - self.last_size.width())
            self.ui.logo_2.setMinimumWidth(self.ui.logo_2.minimumWidth() + int(inc))
            self.last_size = self.size()
    def update(self):
        firstName = self.ui.lineEdit_12.text()
        lastName = self.ui.lineEdit_18.text()
        phone = self.ui.lineEdit_20.text()
        ID = self.ui.lineEdit_19.text()
        self.ui.label_17.setVisible(False)
        self.ui.label_27.setVisible(False)
        self.ui.label_31.setVisible(False)
        self.ui.label_30.setVisible(False)
        rightName = 0
        rightNum = 0
        if not(c.check_letters_only(firstName)) or not(c.checkNotEmpty(firstName)):
            self.ui.label_17.setVisible(True)
        else:
            self.ui.label_17.setVisible(False)
            rightName = 1
          
        if not(c.check_letters_only(lastName)) or not(c.checkNotEmpty(lastName)):
            self.ui.label_27.setVisible(True)
        else:
            self.ui.label_27.setVisible(False)
            rightNum = 1
          
        if not(c.check_digits_only(ID)) or not(c.checkNotEmpty(ID)):
            self.ui.label_31.setVisible(True)
        else:
            self.ui.label_31.setVisible(False)
            rightNum = 1
          
        if not(c.check_phone_number(phone)) or not(c.checkNotEmpty(phone)):
            self.ui.label_30.setVisible(True)
        else:
            self.ui.label_30.setVisible(False)
            rightNum = 1
        
        if rightName and rightNum:
            pass
          #check database part
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
        self.ui.lineEdit.textChanged.connect(self.search)
        self.ui.settings_2.clicked.connect(self.stt)
        # self.ui.mode.clicked.connect(self.mode)
        self.mydata=[];
        self.table_init()

    def search(self):
        srch = self.ui.lineEdit.text()
        if srch != "":
            nedata=[]
            for record in self.mydata:
                if srch in str(record[0]):
                    nedata.append(record)
                elif srch in record[1]:
                    nedata.append(record)
                elif srch in record[2]:
                    nedata.append(record)
            self.on_table_changed(nedata)
        else:
            self.on_table_changed(self.mydata)
    def table_init(self):
        conn = pymysql.connect(host="db4free.net", user="learnloop", password="learnloop5", db="learnloop")
        cursor = conn.cursor()
        query = "SELECT studentId,CONCAT(firstName,' ',lastName) as Name,email \
        FROM Students\
        WHERE groupId=2;"
        cursor.execute(query)
        data = cursor.fetchall()
        self.mydata=list(data)
        cursor.close()
        self.on_table_changed(self.mydata)

    def on_table_changed(self,mydata):
                print(f"Table changed: ")
        
        # Clear the table
                x=0;
                for record in mydata:
                        print(record)
                        x=len(record)
                self.ui.table.clearContents()
                self.ui.table.setRowCount(0)
                
                # Refetch data from the database
                # query = QSqlQuery()
                # query.prepare("SELECT * from Persons3;")
                # if not query.exec_():
                #         print("Cannot execute query")
                #         sys.exit(1)
                
                # Repopulate the table with data from the database
                if(x):
                    x+=1
                self.ui.table.setColumnCount(x)
                if(x):
                    x-=1
                # self.table.setRowCount(query.size())
                
                self.ui.table.setHorizontalHeaderLabels(["ID","Name","Email",""])
                self.ui.table.horizontalHeader()
                for record in mydata:
                        row = self.ui.table.rowCount()
                        self.ui.table.insertRow(row)
                        for column in range(x):
                                z=record[column]
                                z=str(z);
                                item = QTableWidgetItem(z)
                                item.setTextAlignment(Qt.AlignCenter);
                                # item(QColor(255, 255, 255))  # Set text color to blue
                                self.ui.table.setItem(row, column, item)
                        button = QPushButton("Click Me")
                        button.setObjectName("but_"+str(record[0]))
                        button.clicked.connect(self.on_button_clicked)
                        self.ui.table.setCellWidget(row, x, button)
                        
                
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
    def stt(self):
            self.close()
            Base.gotoadminpro()
        # self.header.mouseMoveEvent = self.MoveWindow

class studyGroupCoursesMainPage(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from coursesMainPageX_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.pushButton.clicked.connect(self.newcourse)
        self.ui.settings_2.clicked.connect(self.stt)
        self.ui.expand_3.clicked.connect(self.back)
        self.ui.profilePhoto_2.clicked.connect(self.gotomain)
        qure="select courseName, numberOfHours, term from Courses WHERE groupId = 2;"
        cursor = mydb.cursor()
        cursor.execute(qure)
        data = cursor.fetchall()
        self.mydata=list(data)
        cursor.close()
        self.fillscroll(self.mydata)
    
    def createbox(self,l1,l2,l3,num):
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Condensed")
        font2.setPointSize(22)
        font2.setBold(False)
        font2.setWeight(50)
        # self.ui.numOfGroups.setFont(font2)
        font4 = QFont()
        font4.setFamily(u"Bahnschrift Condensed")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setWeight(50)
        self.frame_31 = QFrame()
        self.frame_31.setObjectName(u"fr_"+str(num))
        self.frame_31.setMinimumSize(QSize(240, 180))
        self.frame_31.setMaximumSize(QSize(240, 180))
        self.frame_31.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 2px;")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_31)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verfr_"+str(num))
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_23)

        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frA_"+str(num))
        self.frame_32.setMinimumSize(QSize(0, 30))
        self.frame_32.setMaximumSize(QSize(16777215, 30))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_27.setSpacing(2)
        self.horizontalLayout_27.setObjectName(u"horB_"+str(num))
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_32)
        self.label_26.setObjectName(u"la_"+str(num))
        self.label_26.setMinimumSize(QSize(0, 30))
        self.label_26.setMaximumSize(QSize(16777215, 30))
        self.label_26.setFont(font2)
        self.label_26.setLineWidth(5)


        self.horizontalLayout_27.addWidget(self.label_26, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_14.addWidget(self.frame_32, 0, Qt.AlignHCenter)

        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frB_"+str(num))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_21.setSpacing(2)
        self.horizontalLayout_21.setObjectName(u"horAz_"+str(num))
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_14.addWidget(self.frame_33, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_27 = QLabel(self.frame_31)
        self.label_27.setObjectName(u"laB_"+str(num))
        self.label_27.setMaximumSize(QSize(16777215, 35))
        self.label_27.setFont(font2)
        self.label_27.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.label_27, 0, Qt.AlignHCenter)

        self.label_40 = QLabel(self.frame_31)
        self.label_40.setObjectName(u"laC_"+str(num))
        self.label_40.setMaximumSize(QSize(16777215, 35))
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.label_40, 0, Qt.AlignHCenter)

        self.frame_34 = QFrame(self.frame_31)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 33))
        self.frame_34.setMaximumSize(QSize(16777215, 33))
        self.frame_34.setStyleSheet(u"")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_28.setSpacing(20)
        self.horizontalLayout_28.setObjectName(u"horZA_"+str(num))
        self.horizontalLayout_28.setContentsMargins(0, 5, 0, 0)
        self.pushButton_14 = QPushButton(self.frame_34)
        self.pushButton_14.setObjectName(u"EpushButton_"+str(num))
        self.pushButton_14.setMinimumSize(QSize(75, 28))
        self.pushButton_14.setMaximumSize(QSize(75, 28))
        self.pushButton_14.setSizeIncrement(QSize(0, 0))
        self.pushButton_14.clicked.connect(self.on_button_clicked)
        font7 = QFont()
        font7.setFamily(u"Bahnschrift Condensed")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setWeight(50)
        self.pushButton_14.setFont(font7)
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"background: #E94560;\n"
"border-radius: 3px;\n"
"")     
        self.label_26.setText(l1)
        self.label_27.setText(l2)
        self.label_40.setText(l3+"term")
        self.pushButton_14.setText("Enter")
        self.horizontalLayout_28.addWidget(self.pushButton_14)


        self.verticalLayout_14.addWidget(self.frame_34, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_24)

        # frame.show()
        return self.frame_31
    def fillscroll(self,ls):
        for i in range(0,len(ls),3):
            hbox=QHBoxLayout()
            print(20);
            for j in range(0,min(3,len(ls)-i)):
                z=self.createbox(str(ls[i+j][0]),str(ls[i+j][1]),str(ls[i+j][2]),ls[i+j][3])
                print(z)
                hbox.addWidget(z)
            hbox.setContentsMargins(0,5,0,0)
            self.ui.verticalLayout_3.addLayout(hbox)
    def on_button_clicked(self):
        # print(bu);
        global currentStudentID

        currentStudentID=0
        sending_button = self.sender()
        for x in str(sending_button.objectName()):
                if x<'9':
                    currentStudentID*=10
                    currentStudentID+=int(x)-int('0')
        print('%s Clicked!' % str(sending_button.objectName()))
        # This method will be called when the button is clicked
        print("Button clicked")
        self.close()
        Base.gotoCourse()

    
    def newcourse(self):
            self.close()
            Base.gotoCourseCreate()
    def stt(self):
            self.close()
            Base.gotoadminpro()
    def back(self):
        self.close()
        Base.gotoStudyGroup()
    def gotomain(self):
        self.close()
        Base.gotoMainPage()
        # self.header.mouseMoveEvent = self.MoveWindowclass studyGroupCoursesMainPage(QMainWindow,Base):
    # def __init__(self):
    #     QMainWindow.__init__(self)
    #     from courseMainPage_ui import Ui_MainWindow
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self)
    #     loadJsonStyle(self, self.ui)
    #     self.ui.pushButton.clicked.connect(self.newcourse)
    
    # def newcourse(self):
    #         self.close()
    #         Base.gotoCourseCreate()
        # self.header.mouseMoveEvent = self.MoveWindow
class mainwindow(QMainWindow,Base):
    def __init__(self):
        QMainWindow.__init__(self)
        from adminMainPage_ui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # nam="PU_"+str(id)
        self.ui.pushButton.clicked.connect(self.newstudygroup)
        self.ui.settings_2.clicked.connect(self.stt)
        loadJsonStyle(self, self.ui)
        # self.box_init([["1","Electrical Power"],["2","Electrical Power"],["3","Computer"],["4","computer"],["3","Computer"],["4","computer"]])
        # self.header.mouseMoveEvent = self.MoveWindow
        # self.ui.lineEdit_6.textChanged.connect(self.search)
        # self.ui.mode.clicked.connect(self.mode)
        self.mydata=[];
        
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT COUNT(*) FROM Students;")
        s = mycursor.fetchall()[0][0]
        
        mycursor.execute("SELECT COUNT(*) FROM Courses;")
        s2 = mycursor.fetchall()[0][0]
        
        mycursor.execute("SELECT COUNT(*) FROM studyGroups;")
        s3 = mycursor.fetchall()[0][0]
        self.ui.numOfGroups.setText(str(s))
        self.ui.numOfGroups_2.setText(str(s))
        self.ui.numOfGroups_3.setText(str(s))
        mycursor.execute("SELECT groupId, cohortName, cohortNumber FROM studyGroups;")
        self.s4=[]
        # print(mycursor.fetchall())
        for x in mycursor.fetchall():
            print(x)
            self.s4.append(x)
        # mycursor.execute("SELECT lastName FROM Students WHERE studentId = {}".format(currentStudentID))
        # s2= mycursor.fetchall()[0][0]
        # self.ui.label.setText(s)
        # mycursor.execute("SELECT profilePhoto FROM Students WHERE studentId = {}".format(currentStudentID))
        # blob_data = mycursor.fetchall()[0][0]
        # qimage = QImage.fromData(blob_data)
        # profilePhoto = QPixmap.fromImage(qimage)
        print(self.s4)
        
        mycursor.close()
        self.fillscroll(self.s4)
# SELECT COUNT(*) FROM Students;
# SELECT COUNT(*) FROM Courses;
# SELECT COUNT(*) FROM studyGroups;


# SELECT groupId, cohortName, cohortNumber FROM studyGroups;
    def search(self):
        srch = self.ui.lineEdit_6.text()
        # self.ui.verticalLayout_5.deleteLater()
        # while self.ui.verticalLayout_5.count():
        #     child = self.ui.verticalLayout_5.takeAt(0)
        #     if child.widget():
        #         child.widget().setParent(None)
        # from adminMainPage_ui import Ui_MainWindow
        # self.ui = Ui_MainWindow()
        if srch != "":
            nedata=[]
            for record in self.s4:
                if srch in str(record[0]):
                    nedata.append(record)
                elif srch in str(record[1]):
                    nedata.append(record)
                # elif srch in str(record[2]):
                #     nedata.append(record)
            self.fillscroll(nedata)
        else:
            self.fillscroll(self.s4)
        self.close()
        Base.gotoMainPage()
    def newstudygroup(self):
        self.close()
        Base.gotoStudyGroupCreate()
    def stt(self):
        self.close()
        Base.gotoadminpro()
    def createbox(self,l1,l2,num):
        l3="st"
        if(l1=="1"):
            l3="st"
        elif(l1=="2"):
            l3="nd"
        elif(l1=="3"):
            l3="rd"
        else: 
            l3="th"
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Condensed")
        font2.setPointSize(22)
        font2.setBold(False)
        font2.setWeight(50)
        self.ui.numOfGroups.setFont(font2)
        font4 = QFont()
        font4.setFamily(u"Bahnschrift Condensed")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setWeight(50)
        frame_23 = QFrame()
        frame_23.setObjectName(u"fr_"+str(num))
        frame_23.setMinimumSize(QSize(240, 150))
        frame_23.setMaximumSize(QSize(240, 150))
        frame_23.setStyleSheet(u"background: #0F3460;\n"
"color: white;\n"
"border-radius: 5px;\n"
"letter-spacing: 2px;")
        frame_23.setFrameShape(QFrame.StyledPanel)
        frame_23.setFrameShadow(QFrame.Raised)
        verticalLayout_12 = QVBoxLayout(frame_23)
        verticalLayout_12.setSpacing(5)
        verticalLayout_12.setObjectName(u"vertfr_"+str(num))
        verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        verticalLayout_12.addItem(verticalSpacer_19)

        frame_24 = QFrame(frame_23)
        frame_24.setObjectName(u"frA_"+str(num))
        frame_24.setMinimumSize(QSize(0, 30))
        frame_24.setMaximumSize(QSize(16777215, 30))
        frame_24.setFrameShape(QFrame.StyledPanel)
        frame_24.setFrameShadow(QFrame.Raised)
        horizontalLayout_23 = QHBoxLayout(frame_24)
        horizontalLayout_23.setSpacing(2)
        horizontalLayout_23.setObjectName(u"horfr_"+str(num))
        horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        label_22 = QLabel(frame_24)
        label_22.setObjectName(u"Alabel_"+str(num))
        label_22.setMinimumSize(QSize(0, 30))
        label_22.setMaximumSize(QSize(16777215, 30))
        label_22.setFont(font2)
        label_22.setLineWidth(5)
        label_22.setText(l1)

        horizontalLayout_23.addWidget(label_22, 0, Qt.AlignRight|Qt.AlignBottom)

        label_23 = QLabel(frame_24)
        label_23.setObjectName(u"Blabel_"+str(num))
        label_23.setMinimumSize(QSize(0, 20))
        label_23.setMaximumSize(QSize(16777215, 20))
        label_23.setFont(font4)
        label_23.setFrameShadow(QFrame.Plain)
        label_23.setAlignment(Qt.AlignCenter)
        label_23.setIndent(-1)
        label_23.setText(l3)

        horizontalLayout_23.addWidget(label_23, 0, Qt.AlignLeft|Qt.AlignBottom)


        verticalLayout_12.addWidget(frame_24, 0, Qt.AlignHCenter)

        frame_25 = QFrame(frame_23)
        frame_25.setObjectName(u"frB_"+str(num))
        frame_25.setFrameShape(QFrame.StyledPanel)
        frame_25.setFrameShadow(QFrame.Raised)
        horizontalLayout_18 = QHBoxLayout(frame_25)
        horizontalLayout_18.setSpacing(2)
        horizontalLayout_18.setObjectName(u"horfrB_"+str(num))
        horizontalLayout_18.setContentsMargins(0, 0, 0, 0)

        verticalLayout_12.addWidget(frame_25, 0, Qt.AlignHCenter|Qt.AlignBottom)

        label_24 = QLabel(frame_23)
        label_24.setObjectName(u"Clabel_"+str(num))
        label_24.setMaximumSize(QSize(16777215, 35))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift Condensed")
        font6.setPointSize(18)
        font6.setBold(False)
        font6.setWeight(50)
        label_24.setFont(font6)
        label_24.setStyleSheet(u"")
        label_24.setText(l2)

        verticalLayout_12.addWidget(label_24, 0, Qt.AlignHCenter)

        frame_26 = QFrame(frame_23)
        frame_26.setObjectName(u"frBu_"+str(num))
        frame_26.setMinimumSize(QSize(0, 33))
        frame_26.setMaximumSize(QSize(16777215, 33))
        frame_26.setStyleSheet(u"")
        frame_26.setFrameShape(QFrame.StyledPanel)
        frame_26.setFrameShadow(QFrame.Raised)
        horizontalLayout_24 = QHBoxLayout(frame_26)
        horizontalLayout_24.setSpacing(20)
        horizontalLayout_24.setObjectName(u"horBU_"+str(num))
        horizontalLayout_24.setContentsMargins(0, 5, 0, 0)
        pushButton_12 = QPushButton(frame_26)
        pushButton_12.setObjectName(u"EpushButton_"+str(num))
        pushButton_12.setMinimumSize(QSize(75, 28))
        pushButton_12.setMaximumSize(QSize(75, 28))
        pushButton_12.setSizeIncrement(QSize(0, 0))
        font7 = QFont()
        font7.setFamily(u"Bahnschrift Condensed")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setWeight(50)
        pushButton_12.setFont(font7)
        pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        pushButton_12.setText("Enter")
        pushButton_12.clicked.connect(self.on_button_clicked)
        pushButton_12.setStyleSheet(u"background: #E94560;\n"
"border-radius: 3px;\n"
"")

        horizontalLayout_24.addWidget(pushButton_12)

        pushButton_13 = QPushButton(frame_26)
        pushButton_13.setObjectName(u"FpushButton_"+str(num))
        pushButton_13.setMinimumSize(QSize(75, 28))
        pushButton_13.setMaximumSize(QSize(75, 28))
        pushButton_13.setSizeIncrement(QSize(0, 0))
        pushButton_13.setFont(font7)
        pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        pushButton_13.setText("Edit")
        pushButton_13.clicked.connect(self.on_button_clicked2)
        pushButton_13.setStyleSheet(u"background: #E94560;\n"
"border-radius: 3px;\n"
"")

        horizontalLayout_24.addWidget(pushButton_13)


        verticalLayout_12.addWidget(frame_26, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        verticalLayout_12.addItem(verticalSpacer_20)
        # frame.show()
        return frame_23
    def fillscroll(self,ls):
        for i in range(0,len(ls),3):
            hbox=QHBoxLayout()
            print(20);
            for j in range(0,min(3,len(ls)-i)):
                z=self.createbox(str(ls[i+j][2]),ls[i+j][1],ls[i+j][0])
                print(z)
                hbox.addWidget(z)
            hbox.setContentsMargins(0,5,0,0)
            self.ui.verticalLayout_5.addLayout(hbox)
    def on_button_clicked(self):
        # print(bu);
        global currentStudyGroupID

        currentStudyGroupID=0
        sending_button = self.sender()
        for x in str(sending_button.objectName()):
                if x<'9':
                    currentStudyGroupID*=10
                    currentStudyGroupID+=int(x)-int('0')
        print('%s Clicked!' % str(sending_button.objectName()))
        # This method will be called when the button is clicked
        print("Button clicked")
        self.close()
        Base.gotoStudyGroup()
    def on_button_clicked2(self):
        # print(bu);
        global currentStudyGroupID
        currentStudyGroupID=0
        
        sending_button = self.sender()
        for x in str(sending_button.objectName()):
            if x<'9':
                currentStudyGroupID*=10
                currentStudyGroupID+=int(x)-int('0')
        print('%s Clicked!' % str(sending_button.objectName()))
        # This method will be called when the button is clicked
        print("Button clicked")
        self.close()
        Base.gotoStudyGroupEdition()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainwindow()
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