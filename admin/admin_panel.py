import pandas as pd
import os,sys

# Making a student management system with admin login and student data handling
USERS_FILE = "data/users.csv"
PASSWORD_FILE = "data/passwords.csv"


def initialize_file():
    if not os.path.exists(USERS_FILE) and os.path.exists(PASSWORD_FILE):
        df = pd.DataFrame(columns=["ID", "Name", "Username", "Password", "Email","Role"])
        password_df = pd.DataFrame(columns=["ID", "Name", "Username", "Password","Role"])
        df.to_csv(USERS_FILE, index=False)
        password_df.to_csv(PASSWORD_FILE, index=False)

def add_user():
    print("Admin or Student")
    user_role = input("Role: ").strip()
    

    print(f"\n➕ Add New {user_role}")
    user_id = input("User ID: ").strip()
    
    # Check for duplicate ID
    if os.path.exists(USERS_FILE) and os.path.exists(PASSWORD_FILE):
        df = pd.read_csv(USERS_FILE)
        password_df = pd.read_csv(PASSWORD_FILE)
        df['ID'] = df['ID'].astype(str)
        password_df['ID'] = password_df['ID'].astype(str)  # Ensure ID is string for comparison
        if user_id in df['ID'].values:
            if user_id in password_df['ID'].values:
                print("❌ Error: User ID already exists.\n")
                return
    else:
        df = pd.DataFrame(columns=["ID", "Name", "Username", "Password", "Email","Role"])
        password_df = pd.DataFrame(columns= ["ID", "Name", "Username", "Password","Role"])

    name = input("Full Name: ").strip()
    username = input("Username :").strip()
    password = input("Password: ").strip()
    email = input("Email: ").strip()
    role = user_role

    # Check for empty fields
    if not all([user_id, name, username,password,email,role]):
        print("❌ Error: All fields are required. User not added.\n")
        return

    # Add the new student
    new_data = pd.DataFrame([{
        "ID": user_id,
        "Name": name,
        "Username": username,
        "Password": password,
        "Email": email,
        "Role": role
    }])

    newpassword_data = pd.DataFrame([{
        "ID": user_id,
        "Name": name,
        "Username": username,
        "Password": password,
        "Role": role
    }])

    # Append new student to the CSV file
    df = pd.concat([df, new_data], ignore_index=True)
    df = df.sort_values(by='ID', ascending=True)
    df.to_csv(USERS_FILE, index=False)

    password_df = pd.concat([password_df, newpassword_data], ignore_index=True)
    password_df = password_df.sort_values(by='ID', ascending=True)
    password_df.to_csv(PASSWORD_FILE, index=False)

    print(f"✅ {user_role} added to database successfully!\n")


def remove_student():
    print("\n ➖ Remove Student")
    rm_id = input("Enter Student ID to remove: ")
    try:
        df = pd.read_csv(USERS_FILE)
               
        # Cast 'ID' column to string for accurate comparison
        df['ID'] = df['ID'].astype(str)

        if rm_id in df['ID'].values:
            df = df[df['ID'] != rm_id]
            df.to_csv(USERS_FILE, index=False)
            print("✅ Student removed successfully!\n")
        else:
            print("❗ Student ID not found.\n")
    except FileNotFoundError:
        print("❗ No student file found.\n")

def view_students():
    print("\n📄 All Students Information:")
    
    try:
        df = pd.read_csv(USERS_FILE)
        if df.empty:
            print("No students found.\n")
        else:
            print(df.to_string(index=False))
            print()
    except FileNotFoundError:
        print("No student file found.\n")

def admin_panel():
    print("📋 Admin Panel - Choose an Option:")
    print("1. Add New User")
    print("2. Remove Student")
    print("3. View All Students")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        remove_student()
    elif choice == '3':
        view_students()
    elif choice == '4':
        print("👋 Exiting Admin Panel.")
        sys.exit()
    else:
        print("❗ Invalid option. Please try again.\n")

# Main Program
if __name__ == "__main__":
    initialize_file()
    admin_panel()
