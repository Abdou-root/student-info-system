# this script contains our database system initialization
import sqlite3

# connect to sqlite db and create if not exist
conn = sqlite3.connect('student-info-sys.db')

# cursor object
cursor = conn.cursor()

# Create Students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students(
StudentID INT PRIMARY KEY,
Name TEXT,
EnrollmentYear INT,
Major TEXT,
Gender TEXT
)
''')

# Create Courses table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Courses(
CourseID INT PRIMARY KEY,
CourseName TEXT,
Credits INT
)
''')

# Create Enrollments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Enrollments(
EnrollmentID INT PRIMARY KEY,
StudentID INT,
CourseID INT,
Grade TEXT,  
FOREIGN KEY(StudentID) REFERENCES Students(StudentID),
FOREIGN KEY(CourseID) REFERENCES Courses(CourseID)
)
''')

# Create Accommodations table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Accommodations(
AccommodationID INT PRIMARY KEY,
StudentID INT,
Address TEXT,
FOREIGN KEY(StudentID) REFERENCES Students(StudentID)
)
''')

# Create BookPurchases table
cursor.execute('''
CREATE TABLE IF NOT EXISTS BookPurchases(
PurchaseID INT PRIMARY KEY,
StudentID INT,
CourseID INT,
BookName TEXT,
FOREIGN KEY(StudentID) REFERENCES Students(StudentID),
FOREIGN KEY(CourseID) REFERENCES Courses(CourseID)
)
''')

conn.commit()
conn.close()

print('Database initialized')
