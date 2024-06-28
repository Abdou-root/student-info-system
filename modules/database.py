# this script contains basic CRUD functions and data manipulation functions
import sqlite3

DB_PATH = 'db/student-info-sys.db'


# adding a new student
def add_student(student_id, name, enrollment_year, major, gender, dob, Region):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Students (StudentID, Name, EnrollmentYear, Major, Gender, DOB, Region) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (student_id, name, enrollment_year, major, gender, dob, Region))
    conn.commit()
    conn.close()


# update student info
def update_student(student_id, name, enrollment_year, major, gender, dob):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Students SET Name = ?, EnrollmentYear = ?, Major = ?, Gender = ?, DOB = ? WHERE StudentID = ?",
        (name, enrollment_year, major, gender, dob, student_id))
    conn.commit()
    conn.close()


# delete student from db
def delete_student(student_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE StudentID = ?", (student_id,))
    conn.commit()
    conn.close()


# query student information
def query_student(student_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE StudentID = ?", (student_id,))
    student_info = cursor.fetchall()
    conn.close()
    return student_info

# f1. student enlisting in a course
def student_choose_course(enrollment_id, student_id, course_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID, Grade) VALUES (?, ?, ?, 'Not Graded')",
                   (enrollment_id, student_id, course_id))
    conn.commit()
    conn.close()


# f2. managing accomodation change
def manage_accommodation(accommodation_id, student_id, address):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("REPLACE INTO Accommodations (AccommodationID, StudentID, Address) VALUES (?, ?, ?)",
                   (accommodation_id, student_id, address))
    conn.commit()
    conn.close()


# f3. student book purchase
def student_buy_book(purchase_id, student_id, course_id, book_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO BookPurchases (PurchaseID, StudentID, CourseID, BookName) VALUES (?, ?, ?, ?)",
                   (purchase_id, student_id, course_id, book_name))
    conn.commit()
    conn.close()


# f4. register or update students

def register_or_update_student(student_id, name, enrollment_year, major, gender, dob):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # if the student already exists
    cursor.execute("SELECT * FROM Students WHERE StudentID = ?", (student_id,))
    student_exists = cursor.fetchone()

    if student_exists:
        # Update existing student's information
        cursor.execute(
            "UPDATE Students SET Name = ?, EnrollmentYear = ?, Major = ?, Gender = ?, DOB = ? WHERE StudentID = ?",
            (name, enrollment_year, major, gender, dob, student_id))
        print(f"Student {student_id} updated.")
    else:
        # Add new student
        cursor.execute(
            "INSERT INTO Students (StudentID, Name, EnrollmentYear, Major, Gender, DOB) VALUES (?, ?, ?, ?, ?, ?)",
            (student_id, name, enrollment_year, major, gender, dob))
        print(f"Student {student_id} added.")

    conn.commit()
    conn.close()
