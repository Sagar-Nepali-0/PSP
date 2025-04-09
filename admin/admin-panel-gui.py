import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os

USERS_FILE = "data/users.csv"
DATA_FILE_PATH = "data/passwords.csv"

# Ensure the student file exists
def initialize_file():
    if not os.path.exists(USERS_FILE):
        df = pd.DataFrame(columns=["ID", "Name","Username","Password","Email","Role"])
        df.to_csv(USERS_FILE, index=False)

# GUI Application Class
class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("700x500")
        self.create_login_page()
        self.var = tk.StringVar(value="Role")

    def create_login_page(self):
        self.clear_root()
        tk.Label(self.root, text="🔐 Admin Login", font=("Arial", 20)).pack(pady=20)
        
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        
        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        
        tk.Button(self.root, text="Login", command=self.check_login).pack(pady=10)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
  
        if not username or not password:
            messagebox.showerror("Input Error", "Both fields are required.")
            return
        try:
            # Read user data
            user_data = pd.read_csv(DATA_FILE_PATH, dtype={'Password': str})
        except FileNotFoundError:
            messagebox.showerror("Error", "Password file not found.")
            return

        # Authenticate user
        user_row = user_data[
            (user_data['Username'] == username) & (user_data['Password'] == password)
        ]

        if user_row.empty:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            return
        else:
            user_role = user_row.iloc[0]["Role"]
            if user_role == "admin" or user_role == "Admin":
                messagebox.showinfo("Success", "Login successful!")
                self.create_admin_panel()
            else:
                messagebox.showinfo("Access Denial", "Access Denial")



    def create_admin_panel(self):
        self.clear_root()
        tk.Label(self.root, text="📋 Admin Panel", font=("Arial", 18)).pack(pady=15)
        tk.Button(self.root, text="➕ Add User", width=20, command=self.create_add_user_page).pack(pady=5)
        tk.Button(self.root, text="📄 View Students", width=20, command=self.create_view_students_page).pack(pady=5)
        tk.Button(self.root, text="➖ Delete User", width=20, command=self.create_delete_user_page).pack(pady=5)
        tk.Button(self.root, text="🚪 Logout", width=20, command=self.create_login_page).pack(pady=5)

    def create_add_user_page(self):
        self.clear_root()
        tk.Label(self.root, text="Add New User", font=("Arial", 16)).pack(pady=10)
        labels = ["ID", "Name","Username","Password","Email"]

        self.entries = {}

        for label in labels:
            tk.Label(self.root, text=label).pack()
            entry = tk.Entry(self.root)
            entry.pack()
            self.entries[label] = entry

            # Add a dropdown for selecting the role
        self.var = tk.StringVar(self.root)
        self.var.set("Select Role")  # Default value (if no role is selected)
        tk.OptionMenu(self.root, self.var, "Admin", "Student").pack()

        tk.Button(self.root, text="Add User", command=self.add_user).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_admin_panel).pack()

    def add_user(self):
        users_data = {key: entry.get().strip() for key, entry in self.entries.items()}
        role = self.var.get() 
        if not all(users_data.values()) or role == "Select Role":
            messagebox.showerror("Error", "All fields are required.")
            return

        df = pd.read_csv(USERS_FILE)
        if users_data["ID"] in df["ID"].astype(str).values:
            messagebox.showerror("Error", "User ID already exists.")
            return
        
        users_data["Role"] = role
        # 
        user_data_to_add = {
            "ID": users_data["ID"],
            "Name": users_data["Name"],
            "Username": users_data["Username"],
            "Password": users_data["Password"],
            "Email": users_data["Email"],
            "Role": users_data["Role"]
        }
        df = pd.read_csv(USERS_FILE)
        df = pd.concat([df, pd.DataFrame([user_data_to_add])], ignore_index=True)
        df.to_csv(USERS_FILE, index=False)

        # Add only Username, Password, and Role to the passwords file
        passwords_data_to_add = {
            "Username": users_data["Username"],
            "Password": users_data["Password"],
            "Role": users_data["Role"]
        }
        passwords_df = pd.read_csv(DATA_FILE_PATH)
        passwords_df = pd.concat([passwords_df, pd.DataFrame([passwords_data_to_add])], ignore_index=True)
        passwords_df.to_csv(DATA_FILE_PATH, index=False)

        messagebox.showinfo("Success", "User added successfully.")
        self.create_admin_panel()

    def create_view_students_page(self):
        self.clear_root()
        tk.Label(self.root, text="All Students", font=("Arial", 16)).pack(pady=10)
        try:
            df = pd.read_csv(USERS_FILE)
            if df.empty:
                tk.Label(self.root, text="No students found.").pack()
            else:
                tree = ttk.Treeview(self.root, columns=list(df.columns), show='headings')
                for col in df.columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=100)
                for _, row in df.iterrows():
                    tree.insert("", "end", values=list(row))
                tree.pack(expand=True, fill="both")
        except FileNotFoundError:
            tk.Label(self.root, text="No student file found.").pack()
        tk.Button(self.root, text="Back", command=self.create_admin_panel).pack(pady=10)

    def create_delete_user_page(self):
        self.clear_root()
        tk.Label(self.root, text="Remove User", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Enter User ID:").pack()
        self.delete_entry = tk.Entry(self.root)
        self.delete_entry.pack()
        tk.Button(self.root, text="Delete", command=self.delete_user).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_admin_panel).pack()

    def delete_user(self):
        user_id = self.delete_entry.get().strip()
        try:
            df = pd.read_csv(USERS_FILE)
            df["ID"] = df["ID"].astype(str)
            if user_id in df["ID"].values:
                user_to_delete = df[df["ID"] == user_id]["Username"].values[0]
                df = df[df["ID"] != user_id]
                df.to_csv(USERS_FILE, index=False)

                passwords_df = pd.read_csv(DATA_FILE_PATH)
                passwords_df["Username"] = passwords_df["Username"].astype(str)
                passwords_df = passwords_df[passwords_df["Username"] != user_to_delete]
                passwords_df.to_csv(DATA_FILE_PATH, index=False)

                messagebox.showinfo("Success", "User removed successfully.")
                self.create_admin_panel()
            else:
                messagebox.showerror("Error", "User ID not found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "User file not found.")

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Main Application Start
if __name__ == "__main__":
    initialize_file()
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()