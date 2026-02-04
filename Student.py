import csv
import os

fileName = "Student.csv"
stud = []

# ---------- LOAD DATA ----------
def load():
    if os.path.exists(fileName):
        with open(fileName, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                row[4:] = list(map(int, row[4:]))
                stud.append(row)

# ---------- SAVE DATA ----------
def save():
    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Password", "Name", "Roll No", "English", "Math", "Islamiat", "Urdu"])
        writer.writerows(stud)

# ---------- SIGNUP ----------
def signup():
    print("\n---- Signup ----")
    E_mail = input("Enter Your Email: ")

    for i in stud:
        if i[0] == E_mail:
            print("Email already exists.")
            return

    password = input("Create Password: ")
    name = input("Enter Full Name: ")
    roll_no = input("Enter Roll Number: ")

    while True:
        eng = int(input("English out of 100: "))
        math = int(input("Math out of 100: "))
        isl = int(input("Islamiat out of 75: "))
        urdu = int(input("Urdu out of 100: "))

        if eng > 100 or math > 100 or isl > 75 or urdu > 100:
            print("Invalid numbers! Try again.\n")
        else:
            break

    stud.append([E_mail, password, name, roll_no, eng, math, isl, urdu])
    save()
    print("Signup successful!")

# ---------- LOGIN ----------
def login():
    username = input("Enter Email: ")
    password = input("Enter Password: ")

    for i in stud:
        if i[0] == username and i[1] == password:
            show_marksheet(i)
            return
    print("Invalid credentials.")

# ---------- MARKSHEET ----------
def show_marksheet(i):
    total = i[4] + i[5] + i[6] + i[7]
    percent = total / 4

    print(f"\nName: {i[2]}")
    print(f"Roll: {i[3]}")
    print(f"Total: {total}/375")
    print(f"Percentage: {percent:.2f}%")

# ---------- MENU ----------
def main():
    load()
    while True:
        print("\n===== STUDENT PORTAL =====")
        print("1. SignUp  2. Login  3. Exit")
        ch = input("Choice: ")

        if ch == "1":
            signup()
        elif ch == "2":
            login()
        elif ch == "3":
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()