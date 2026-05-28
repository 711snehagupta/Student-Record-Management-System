import json

FILENAME = "students.json"

def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_data(students):
    with open(FILENAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student(students):
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    subject = input("Enter Subject: ")

    student = {
        "name": name,
        "age": age,
        "marks": marks,
        "subject": subject
    }

    students.append(student)
    save_data(students)

    print("Student Added Successfully!\n")

def view_students(students):
    if len(students) == 0:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")

    for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("Subject:", student["subject"])

def edit_student(students):
    name = input("Enter student name to edit: ")

    for student in students:
        if student["name"].lower() == name.lower():

            student["name"] = input("New Name: ")
            student["age"] = input("New Age: ")
            student["marks"] = input("New Marks: ")
            student["subject"] = input("New Subject: ")

            save_data(students)

            print("Student Record Updated!\n")
            return

    print("Student not found.\n")

def delete_student(students):
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():

            students.remove(student)
            save_data(students)

            print("Student Deleted Successfully!\n")
            return

    print("Student not found.\n")

def main():
    students = load_data()

    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            edit_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice!")

main()
