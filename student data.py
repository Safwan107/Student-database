students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\nStudent Records")
        print("-" * 50)
        for student in students:
            print("Roll   :", student["Roll"])
            print("Name   :", student["Name"])
            print("Age    :", student["Age"])
            print("Course :", student["Course"])
            print("-" * 50)


def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["Roll"] == roll:
            print("\nStudent Found")
            print(student)
            return

    print("Student not found.\n")


def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Course"] = input("Enter New Course: ")
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


while True:
    print("\n===== STUDENT DATABASE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")