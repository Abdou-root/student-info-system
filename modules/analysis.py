# this script contains SQL analysis queries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

DB_PATH = 'db/student-info-sys.db'


# i. Number of students and gender ratio for each major
def analyze_students_and_majors():
    conn = sqlite3.connect(DB_PATH)

    query_1 = """
    SELECT Major, COUNT(*) AS Total_Students,
           SUM(CASE WHEN Gender = 'Male' THEN 1 ELSE 0 END) AS Males,
           SUM(CASE WHEN Gender = 'Female' THEN 1 ELSE 0 END) AS Females
    FROM Students
    GROUP BY Major;
    """
    df_majors = pd.read_sql_query(query_1, conn)
    df_majors['Gender_Ratio'] = df_majors['Males'] / df_majors['Females']
    print(df_majors)
    # Create a bar chart
    df_majors.plot(x='Major', y=['Total_Students', 'Gender_Ratio'], kind='bar', figsize=(10, 6))
    plt.title('Number of Students and Gender Ratio for Each Major')
    plt.ylabel('Count')
    plt.xlabel('Major')
    plt.xticks(rotation=45)
    plt.legend(['Total Students', 'Gender Ratio'])
    plt.show()

    conn.close()


# ii. Comparison of results in different majors
def analyze_major_results():
    conn = sqlite3.connect(DB_PATH)

    query_2 = """
    SELECT s.Major, AVG(e.Grade) AS Average_Grade
    FROM Students s
    JOIN Enrollments e ON s.StudentID = e.StudentID
    GROUP BY s.Major;
    """
    df_results = pd.read_sql_query(query_2, conn)
    print(df_results)
    # Create a bar chart for average grades in different majors
    df_results.plot(x='Major', y='Average_Grade', kind='bar', figsize=(10, 6))
    plt.title('Average Grades in Different Majors')
    plt.ylabel('Average Grade')
    plt.xlabel('Major')
    plt.xticks(rotation=45)
    plt.show()

    conn.close()


# iii. Relationship between age and grades
def analyze_age_and_grades():
    conn = sqlite3.connect(DB_PATH)

    query_3 = """
    SELECT
        s.StudentID,
        s.DOB,
        e.Grade,
        (strftime('%Y', 'now') - strftime('%Y', s.DOB)) - (strftime('%m-%d', 'now') < strftime('%m-%d', s.DOB)) AS Age
    FROM
        Students s
    JOIN
        Enrollments e ON s.StudentID = e.StudentID;
    """
    df_age_grade = pd.read_sql_query(query_3, conn)
    df_age_grade['Grade'] = pd.to_numeric(df_age_grade['Grade'], errors='coerce')
    # calculate average grade for every age
    average_scores_by_age = df_age_grade.groupby('Age')['Grade'].mean().reset_index()
    print(average_scores_by_age)

    # Create a line plot for average grades by age
    plt.figure(figsize=(10, 6))
    plt.plot(average_scores_by_age['Age'], average_scores_by_age['Grade'], marker='o')
    plt.title('Relationship between Age and Average Grade')
    plt.xlabel('Age')
    plt.ylabel('Average Grade')
    plt.grid(True)
    plt.show()

    conn.close()


# iv. Relationship between Regional distribution and grades
def analyze_region_and_grades():
    conn = sqlite3.connect(DB_PATH)

    query_4 = """
         SELECT
            s.Region,
            e.Grade
        FROM
            Students s
        JOIN
            Enrollments e ON s.StudentID = e.StudentID;
        """
    df_region_grade = pd.read_sql_query(query_4, conn)
    df_region_grade['Grade'] = pd.to_numeric(df_region_grade['Grade'], errors='coerce')
    # Calculate average grade for each region
    average_scores_by_region = df_region_grade.groupby('Region')['Grade'].mean().reset_index()
    print(average_scores_by_region)

    # Create a bar chart for average grades by region
    plt.figure(figsize=(12, 8))
    plt.bar(average_scores_by_region['Region'], average_scores_by_region['Grade'], color='skyblue')
    plt.title('Average Grades by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Grade')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    conn.close()


# v. Analysis of Student Accommodations
def analyze_accommodations():
    conn = sqlite3.connect(DB_PATH)

    pd.set_option('display.max_columns', None)
    query_5 = """
    SELECT
        s.Major,
        COUNT(DISTINCT a.StudentID) AS HasAccommodation,
        (SELECT COUNT(*) FROM Students WHERE Major = s.Major) - COUNT(DISTINCT a.StudentID) AS NoAccommodation
    FROM
        Students s
    LEFT JOIN
        Accommodations a ON s.StudentID = a.StudentID
    GROUP BY
        s.Major
    ORDER BY
        s.Major;
    """

    df_accom = pd.read_sql_query(query_5, conn)
    df_accom['Accommodation Ratio'] = df_accom['HasAccommodation'] / (
            df_accom['HasAccommodation'] + df_accom['NoAccommodation'])
    print(df_accom)

    # Create a pie chart for accommodation ratios in different majors
    plt.figure(figsize=(10, 6))
    plt.pie(df_accom['Accommodation Ratio'], labels=df_accom['Major'], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Accommodation Ratio in Different Majors')
    plt.show()

    conn.close()


# vi. Student Participation in Courses by Year
def analyze_course_participation():
    conn = sqlite3.connect(DB_PATH)

    query_6 = """
    SELECT 
        c.CourseName, 
        s.EnrollmentYear, 
        COUNT(DISTINCT e.StudentID) AS NumberOfStudents
    FROM 
        Enrollments e
    JOIN 
        Courses c ON e.CourseID = c.CourseID
    JOIN 
        Students s ON e.StudentID = s.StudentID
    GROUP BY 
        c.CourseName, s.EnrollmentYear
    ORDER BY 
        c.CourseName, s.EnrollmentYear;
    """
    df_courses = pd.read_sql_query(query_6, conn)
    print(df_courses)

    # Create a stacked bar chart for student participation in courses by year
    df_courses_pivot = df_courses.pivot(index='CourseName', columns='EnrollmentYear', values='NumberOfStudents')
    df_courses_pivot.plot(kind='bar', stacked=True, figsize=(12, 8))
    plt.title('Student Participation in Courses by Year')
    plt.xlabel('Course Name')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45)
    plt.legend(title='Enrollment Year')
    plt.show()

    conn.close()
