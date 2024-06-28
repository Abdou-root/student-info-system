# this is the main script

from modules.database import (
    add_student,
    update_student,
    delete_student,
    query_student,
    student_choose_course,
    manage_accommodation,
    student_buy_book,
    register_or_update_student
)
from modules.analysis import (
    analyze_students_and_majors,
    analyze_major_results,
    analyze_age_and_grades,
    analyze_accommodations,
    analyze_region_and_grades,
    analyze_course_participation
)


def display_main_menu():
    print("\nMain Menu:")
    print("1. Data Operations")
    print("2. Data Analysis")
    print("3. Exit")


def data_operations_menu():
    print("\nData Operations:")
    print("1. Add a new student")
    print("2. Update student information")
    print("3. Delete a student")
    print("4. Query student information")
    print("5. Enroll student in a course")
    print("6. Manage accommodation")
    print("7. Student buys a book")
    print("8. Register or update a student")
    print("9. Return to Main Menu")


def data_analysis_menu():
    print("\nData Analysis:")
    print("1. Analyze students and majors")
    print("2. Analyze major results")
    print("3. Analyze age and grades")
    print("4. Analyze region and grades")
    print("5. Analyze accommodations")
    print("6. Analyze course participation")
    print("7. Return to Main Menu")


def data_operations():
    data_operations_menu()
    while True:
        choice = input("\nData manipulation menu , Enter your choice: ")
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            enrollment_year = input("Enter Enrollment Year: ")
            major = input("Enter Major: ")
            gender = input("Enter Gender: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            Region = input("Enter Region: ")
            add_student(int(student_id), name, int(enrollment_year), major, gender, dob, Region)
            print("\nStudent added successfully\n")
        elif choice == '2':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            enrollment_year = input("Enter Enrollment Year: ")
            major = input("Enter Major: ")
            gender = input("Enter Gender: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            update_student(int(student_id), name, int(enrollment_year), major, gender, dob)
        elif choice == '3':
            student_id = input("Enter Student ID: ")
            delete_student(int(student_id))
        elif choice == '4':
            student_id = input("Enter Student ID: ")
            student_info = query_student(int(student_id))
            print(student_info)
        elif choice == '5':
            enrollment_id = input("Enter Enrollment ID: ")
            student_id = input("Enter Student ID: ")
            course_id = input("Enter Course ID: ")
            student_choose_course(int(enrollment_id), int(student_id), int(course_id))
        elif choice == '6':
            accommodation_id = input("Enter Accommodation ID: ")
            student_id = input("Enter Student ID: ")
            address = input("Enter Address: ")
            manage_accommodation(int(accommodation_id), int(student_id), address)
        elif choice == '7':
            purchase_id = input("Enter Purchase ID: ")
            student_id = input("Enter Student ID: ")
            course_id = input("Enter Course ID: ")
            book_name = input("Enter Book Name: ")
            student_buy_book(int(purchase_id), int(student_id), int(course_id), book_name)
        elif choice == '8':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            enrollment_year = input("Enter Enrollment Year: ")
            major = input("Enter Major: ")
            gender = input("Enter Gender: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            register_or_update_student(int(student_id), name, int(enrollment_year), major, gender, dob)
        elif choice == '9':
            return
        else:
            print("Invalid choice. Please try again.")
            data_operations_menu()
        data_operations_menu()


def data_analysis():
    data_analysis_menu()
    while True:
        choice = input("\nData analysis menu, Enter your choice: ")
        if choice == '1':
            analyze_students_and_majors()
        elif choice == '2':
            analyze_major_results()
        elif choice == '3':
            analyze_age_and_grades()
        elif choice == '4':
            analyze_region_and_grades()
        elif choice == '5':
            analyze_accommodations()
        elif choice == '6':
            analyze_course_participation()
        elif choice == '7':
            return
        else:
            print("Invalid choice. Please try again.")
            data_analysis_menu()
        data_analysis_menu()


def main():
    print("Student Information System")
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            data_operations()
        elif choice == '2':
            data_analysis()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
