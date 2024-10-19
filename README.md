Attendance Management System
Overview

The Attendance Management System is a simple Python-based application that allows teachers to manage student attendance efficiently. It provides functionalities for adding teachers and students, marking attendance, and viewing attendance records. The system utilizes SQLite as its database to store user information and attendance records, ensuring that all data is persistent and easily retrievable.
Features

    Teacher Management:
        Add new teachers with a unique username and password.
        Login functionality for teachers to access their accounts.

    Student Management:
        Add multiple students associated with a specific teacher.

    Attendance Tracking:
        Mark attendance for students on a given date.
        Update attendance records if they already exist.

    Attendance Viewing:
        View attendance records for each student on a specified date.

Technologies Used

    Python
    SQLite
  Usage
Adding a Teacher

    When prompted, enter the teacher's name.
    Provide a unique username for the teacher.
    Set a password for the teacher.

Logging In

    Select "Login as Teacher" from the main menu.
    Enter the username and password to log in.

Adding Students

    After logging in, select the option to add students.
    Specify the number of students you want to add.
    Enter each student's name when prompted.

Marking Attendance

    Select the option to mark attendance after logging in.
    Enter the date for which you want to mark attendance.
    Indicate the presence (y/n) for each student.

Viewing Attendance

    Select the option to view attendance after logging in.
    Enter the date to see the attendance records for that day.

Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.
