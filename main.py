# Student Management System

students = []

# Add Student
def add_student():
    print("\nAdd Student")
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")

# View Students
def view_students():
    print("\nStudent List")

    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("----------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])

# Search Student
def search_student():
    print("\nSearch Student")
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            print("Student Found")
            print(student)
            return

    print("Student not found.")

# Delete Student
def delete_student():
    print("\nDelete Student")
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")

# Main Menu
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice. Try again.")