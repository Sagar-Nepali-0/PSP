import pandas as pd
from tkinter import messagebox
from GUI.loginGUI import loginGUI
from GUI.adminGUI import adminGUI
from GUI.studentGUI import studentGUI
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
root, login_btn,username,userpassword= loginGUI()

def login():
    file_path = 'data/passwords.txt'
    name = username.get()
    password = userpassword.get()

    try:
        info = pd.read_csv(file_path, dtype={'password': str})
        match = info[(info['username'] == name) & (info['password'] == password)]

        if not match.empty:
            user_role = match["role"].values[0]  # Extract role for matched user
            messagebox.showinfo("Login Successfully", f"Log In as {user_role.capitalize()}.")
            # Schedule root destruction after messagebox closes
            root.destroy()
            root.quit()
            if user_role == "admin":
                print("ADMIN")
                adminGUI()

            elif user_role == "student":
                print("STUDENT")
                studentGUI()
               
        else:
            messagebox.showinfo("Error", "Please enter valid username and password.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{file_path}' not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))       


login_btn.configure(command=login)

if __name__ == "__main__":
    root.mainloop()