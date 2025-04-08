
import pandas as pd
def main():
    login()

def login():
    file_path = 'data/passwords.csv'
    name = input("Username: ")
    password = input("Password: ")

    
    info = pd.read_csv(file_path, dtype={'password': str})
    match = info[(info['username'] == name) & (info['password'] == password)]

    if not match.empty:
        user_role = match["role"].values[0]
        if user_role == "admin":
            print("ADMIN")

        elif user_role == "student":
            print("STUDENT")
    else:
        print("Invalid or not recorded.")
            

if __name__ == "__main__":
    main()