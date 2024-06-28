# this script helps populate the database with our mock data
import csv
import sqlite3
from datetime import datetime, timedelta
import random


# helper function to faciliate importing mock data from CSVs to our db
def import_csv_to_db(csv_file, table_name, columns):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            placeholders = ', '.join(['?'] * len(row))  # Create placeholders
            query = f'INSERT OR IGNORE INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})'
            cursor.execute(query, row)
        conn.commit()


# helper function to return a random date between two date objects
def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)


conn = sqlite3.connect('student-info-sys.db')
cursor = conn.cursor()

# define corresponding tables and columns with the CSVs
csv_mappings = [
    ('Students.csv', 'Students', ['StudentID', 'Name', 'EnrollmentYear', 'Major', 'Gender']),
    ('Courses.csv', 'Courses', ['CourseID', 'CourseName', 'Credits']),
    ('Enrollments.csv', 'Enrollments', ['EnrollmentID', 'StudentID', 'CourseID', 'Grade']),
    ('Accommodation.csv', 'Accommodations', ['AccommodationID', 'StudentID', 'Address']),
    ('BookPurchases.csv', 'BookPurchases', ['PurchaseID', 'StudentID', 'CourseID', 'BookName'])
]

# import CSVs into db tables
for csv_file, table_name, columns in csv_mappings:
    import_csv_to_db(csv_file, table_name, columns)

# Add a region to the students table
cursor.execute("ALTER TABLE Students ADD COLUMN Region ;")
# populate the region column

states = ['Guangdong', 'Jiangsu', 'Shandong', 'Zhejiang', 'Sichuan',
          'Shanghai', 'Hubei', 'Chongqing', 'Shaanxi', 'Foreigner',
          'Xinjiang', 'Hong Kong', 'Macau'
          ]
cursor.execute("SELECT StudentID FROM Students;")
students = cursor.fetchall()

for student in students:
    Region = random.choice(states)
    cursor.execute("UPDATE Students SET Region = ? WHERE StudentID = ?;", (Region, student[0]))

# Add a DOB column to the Students table
cursor.execute("ALTER TABLE Students ADD COLUMN DOB DATE;")
# Define the start and end dates for the random DOB range
start_date = datetime.strptime('2000-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2004-12-31', '%Y-%m-%d')

# Get all StudentIDs
cursor.execute("SELECT StudentID FROM Students;")
students = cursor.fetchall()

for student in students:
    # Generate a random date within the range for each student
    rand_dob = random_date(start_date, end_date).strftime('%Y-%m-%d')

    # Update the DOB for each student by StudentID
    cursor.execute("UPDATE Students SET DOB = ? WHERE StudentID = ?;", (rand_dob, student[0]))

conn.commit()
conn.close()
