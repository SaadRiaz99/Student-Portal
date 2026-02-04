import csv
import os

fileName = "Student.csv"


def load_students():
    stud = []
    if os.path.exists(fileName):
        with open(fileName, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                row[4:] = list(map(int, row[4:]))
                stud.append(row)
    return stud

# ---------- SAVE STUDENTS ----------
def save_students(stud):
    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Password", "Name", "Roll No", "English", "Math", "Islamiat", "Urdu"])
        writer.writerows(stud)


def admin_login():
    username = input("Admin Username: ")
    password = input("Admin Password: ")
    
    if username == "malik.saad.riaz.96@gmail.com" and password == "saad123":
        return True
    else:
        print("Invalid admin credentials!")
        return False


def show_all_students():
    stud = load_students()
    if not stud:
        print("No students found.")
        return
    print("\n===== ALL STUDENTS =====")
    for s in stud:
        print(f"Name: {s[2]} | Roll No: {s[3]} | Email: {s[0]}")
    print("=======================")


def update_student():
    stud = load_students()
    email = input("Enter Email to Update: ")
    for s in stud:
        if s[0] == email:
            s[2] = input("New Name: ") or s[2]
            s[3] = input("New Roll No: ") or s[3]
            s[4] = int(input("New English: ") or s[4])
            s[5] = int(input("New Math: ") or s[5])
            s[6] = int(input("New Islamiat: ") or s[6])
            s[7] = int(input("New Urdu: ") or s[7])
            save_students(stud)
            print("Updated successfully!")
            return
    print("Student not found.")


def delete_student():
    stud = load_students()
    email = input("Enter Email to Delete: ")
    for s in stud:
        if s[0] == email:
            stud.remove(s)
            save_students(stud)
            print("Deleted successfully!")
            return
    print("Student not found.")

# ---------- ADMIN PANEL ----------
def admin_panel():
    if not admin_login():
        return
    while True:
        print("\n===== ADMIN PANEL =====")
        print("1. Show All Students")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Exit")
        ch = input("Choice: ")

        if ch == "1":
            show_all_students()
        elif ch == "2":
            update_student()
        elif ch == "3":
            delete_student()
        elif ch == "4":
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    admin_panel()