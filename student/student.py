# Student Login interface
import pandas as pd
import os

# Ensure the CSV file is initialized
STUDENT_PASSFILE = "student_credentials.csv"
if not os.path.exists("student_credentials.csv"):
        df = pd.DataFrame(columns=["ID", "Password"])
        df.to_csv("student_credentials.csv", index=False)

# Student Credentials Maker
STUDENT = input("Enter your student ID: ")
STUDENT_PASSWORD = input("Enter your password: ")

# Check for duplicate ID
def check_duplicate():
    df = pd.read_csv("student_credentials.csv")
    df = df.astype(str)  # Ensure all data is string for comparison
    
    if STUDENT in df['ID'].values:
        print("❌ Error: Student already exists.")
    else:
        new_data = pd.DataFrame([{
            "ID": STUDENT,
            "Password": STUDENT_PASSWORD
        }])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv("student_credentials.csv", index=False)
        print("✅ Student credentials added successfully!")

# Student Login
def student_login():
    print("🔐 Student Login")
    student_id = input("Student ID: ").strip()
    password = input("Password: ").strip()

    df = pd.read_csv("student_credentials.csv")
    df = df.astype(str)  # Ensure all data is string for comparison

    if student_id in df['ID'].values and password in df['Password'].values:
        print("✅ Login successful!\n")
        return True
    else:
        print("❌ Invalid credentials. Access denied.")
        return False

def view_profile():
    print("\n👤 View Profile")
    student_id = input("Enter your Student ID: ").strip()

    df = pd.read_csv("student_credentials.csv")
    df = df.astype(str)  # Ensure all data is string for comparison

    if student_id in df['ID'].values:
        student_data = df[df['ID'] == student_id]
        print(student_data.to_string(index=False))
    else:
        print("❌ Student ID not found.")

# Student Interface
def student_interface():
    print("Welcome to the Student Interface!")
    print("1. View Profile")
    print("2. Logout")

    choice = input("Select an option: ")

    if choice == "1":
        view_profile()
    elif choice == "2":
        print("Logging out...")
    else:
        print("Invalid choice. Please try again.")