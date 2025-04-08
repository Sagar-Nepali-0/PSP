import pandas as pd
import os

# Making a student management system with admin login and student data handling
STUDENT_FILE = "data/students.csv"

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Making a Data Frame to store student data
def initialize_file():
    if not os.path.exists(STUDENT_FILE):
        df = pd.DataFrame(columns=["ID", "Name", "Age", "Grade", "Email"])
        df.to_csv(STUDENT_FILE, index=False)

def admin_login():
    print("🔐 Admin Login")
    username = input("Username: ")
    password = input("Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("✅ Login successful!\n")
        return True
    else:
        print("❌ Invalid credentials. Access denied.")
        return False

def add_student():
    print("\n➕ Add New Student")
    student_id = input("Student ID: ").strip()
    
    # Check for duplicate ID
    if os.path.exists(STUDENT_FILE):
        df = pd.read_csv(STUDENT_FILE)
        df['ID'] = df['ID'].astype(str)  # Ensure ID is string for comparison
        if student_id in df['ID'].values:
            print("❌ Error: Student ID already exists.\n")
            return
    else:
        df = pd.DataFrame(columns=["ID", "Name", "Age", "Grade", "Email"])

    name = input("Full Name: ").strip()
    age = input("Age: ").strip()
    grade = input("Grade/Class: ").strip()
    email = input("Email: ").strip()

    # Check for empty fields
    if not all([student_id, name, age, grade, email]):
        print("❌ Error: All fields are required. Student not added.\n")
        return

    # Add the new student
    new_data = pd.DataFrame([{
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Grade": grade,
        "Email": email
    }])

    # Append new student to the CSV file
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(STUDENT_FILE, index=False)
    print("✅ Student added to database successfully!\n")

def remove_student():
    print("\n ➖ Remove Student")
    rm_id = input("Enter Student ID to remove: ")
    try:
        df = pd.read_csv(STUDENT_FILE)
               
        # Cast 'ID' column to string for accurate comparison
        df['ID'] = df['ID'].astype(str)

        if rm_id in df['ID'].values:
            df = df[df['ID'] != rm_id]
            df.to_csv(STUDENT_FILE, index=False)
            print("✅ Student removed successfully!\n")
        else:
            print("❗ Student ID not found.\n")
    except FileNotFoundError:
        print("❗ No student file found.\n")

def view_students():
    print("\n📄 All Students Information:")
    
    try:
        df = pd.read_csv(STUDENT_FILE)
        if df.empty:
            print("No students found.\n")
        else:
            print(df.to_string(index=False))
            print()
    except FileNotFoundError:
        print("No student file found.\n")

def admin_panel():
    while True:
        print("📋 Admin Panel - Choose an Option:")
        print("1. Add New Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            view_students()
        elif choice == '4':
            print("👋 Exiting Admin Panel.")
            break
        else:
            print("❗ Invalid option. Please try again.\n")

# Main Program
if __name__ == "__main__":
    initialize_file()
    if admin_login():
        admin_panel()
