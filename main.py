import sqlite3
from getpass import getpass

conn = sqlite3.connect('attendance_system.db')
c = conn.cursor()

# Create tables if they do not exist
c.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT UNIQUE,
    password TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    date TEXT,
    status TEXT,
    FOREIGN KEY (student_id) REFERENCES students (id)
)
''')

conn.commit()

def add_teacher():
    name = input("Enter the teacher's name: ")
    username = input("Enter a username for the teacher: ")
    password = input("Enter a password for the teacher: ")
    try:
        c.execute('INSERT INTO teachers (name, username, password) VALUES (?, ?, ?)', (name, username, password))
        conn.commit()
        print("Teacher added successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")

def login():
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    c.execute('SELECT * FROM teachers WHERE username=? AND password=?', (user, pwd))
    return c.fetchone()

def add_student(teacher_id):
    try:
        num_students = int(input("How many students do you want to add? "))
        for _ in range(num_students):
            name = input("Enter student name: ")
            c.execute('INSERT INTO students (name, teacher_id) VALUES (?, ?)', (name, teacher_id))
            conn.commit()
            print(f"Student {name} added successfully.")
    except ValueError:
        print("Please enter a valid number.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def mark_attendance(teacher_id):
    date = input("Enter date (YYYY-MM-DD): ")
    c.execute('SELECT * FROM students WHERE teacher_id=?', (teacher_id,))
    students = c.fetchall()
    
    for student in students:
        name = student[1]
        status = input(f"Is {name} present? (y/n): ")
        status_value = 'Present' if status.lower() == 'y' else 'Absent'
        
        c.execute('SELECT * FROM attendance WHERE student_id=? AND date=?', (student[0], date))
        if c.fetchone() is None:
            c.execute('INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)', (student[0], date, status_value))
        else:
            c.execute('UPDATE attendance SET status=? WHERE student_id=? AND date=?', (status_value, student[0], date))
    
    conn.commit()
    print("Attendance marked successfully.")

def view_attendance(teacher_id):
    date = input("Enter date to view attendance (YYYY-MM-DD): ")
    c.execute('SELECT * FROM students WHERE teacher_id=?', (teacher_id,))
    students = c.fetchall()
    
    print(f"\nAttendance for date: {date}\n")
    for student in students:
        student_id = student[0]
        c.execute('SELECT status FROM attendance WHERE student_id=? AND date=?', (student_id, date))
        attendance_record = c.fetchone()
        status = attendance_record[0] if attendance_record else 'Absent'
        print(f"Student: {student[1]}, Status: {status}")

def main():
    if not c.execute('SELECT * FROM teachers').fetchall():
        add_teacher()
    
    while True:
        print("\n1. Login as Teacher")
        print("2. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            teacher = login()
            if teacher:
                teacher_id = teacher[0]
                print("Login successful.")
                
                while True:
                    print("\n1. Add Student")
                    print("2. Mark Attendance")
                    print("3. View Attendance")
                    print("4. Logout")
                    option = input("Select an option: ")
                    
                    if option == '1':
                        add_student(teacher_id)
                    elif option == '2':
                        mark_attendance(teacher_id)
                    elif option == '3':
                        view_attendance(teacher_id)
                    elif option == '4':
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Login failed. Please check your username and password.")
        
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

conn.close()
