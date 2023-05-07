# Student-Enrollment-Database-Project
This project offers a Python-based student enrollment database system for colleges. The intuitive interface simplifies data entry and modification, with online server hosting ensuring accessibility. This advanced system streamlines administrative tasks and enhances support for students it allows an administrator to manage study groups, courses, and student information. It includes a graphical user interface (GUI) developed using PyQt5, and a MySQL database hosted on db4free using phpMyAdmin.
# Tables
The database consists of 5 tables:

 ## students
Contains information about each student, including their name, email, id, and other relevant details.

 ## study_groups
Contains information about each study group, including the group id, a cohort id, and name.

 ## courses
Contains information about each course, including the course name, term, number of hours, and course id.

 ## students_with_courses
Contains information about each student's enrollment in a course, including their grade, student id, and course id.

 ## images
Contains any images associated with the student, such as profile pictures.
# ERD 
![ERD](/Images/learn loop.png)
# Purpose
The purpose of this project is to provide a tool for managing student enrollment information, making it easier for the administrator to organize and track student information in a centralized database. By providing a user-friendly interface and well-organized database tables, this project can help reduce the time and effort required to manage student enrollment information.
Features
The application includes the following features:

# Sign-in Page
The sign-in page allows both administrator and student that has an account created to access the application.

 # Admin Features
Once logged in, the administrator can:

Create new study groups and courses, as well as add students to these groups.
Edit and delete existing study groups, courses, and student information.
View the total number of study groups and the number of students and courses in each study group.
View the information and grades for each student in a particular course.
# Student Features
Once logged in, students can only view their own profile, which includes:

The courses they are enrolled in.
Their grades for each course.
# Dependencies
PyQt5
mysql-connector-python
