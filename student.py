students = []

def add_student(name, roll):
    students.append({"name": name, "roll": roll})
    print("Student added")

def show_students():
    for s in students:
        print("Name:", s["name"], "Roll:", s["roll"])

while True:
    print("\n1.Add Student  2.Show Students  3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll no: ")
        add_student(name, roll)

    elif choice == "2":
        show_students()

    elif choice == "3":
        break

    else:
        print("Invalid choice")
