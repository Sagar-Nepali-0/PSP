
import pandas as pd
from admin.admin_panel import admin_panel

def main():
    login()

def login():
    file_path = 'data/passwords.csv'
    name = input("Username/ID: ")
    password = input("Password: ")

    
    info = pd.read_csv(file_path, dtype={'ID': str})
    match_username = info[(info['Username'] == name) & (info['Password'] == password)]
    match_id = info[(info['ID'] == name) & (info['Password'] == password)]


    if not match_username.empty:
        user_role = match_username["Role"].values[0]
    elif not match_id.empty:
        user_role = match_id["Role"].values[0]
    else:
        print("Invalid or not recorded.")
        return
    
    if user_role == "Admin":
        admin_panel()

    elif user_role == "Student":
        print("STUDENT")
    else:
        print("Invalid or not recorded.")
            

if __name__ == "__main__":
    main()