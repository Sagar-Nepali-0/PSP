import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os

STUDENT_FILE = "students.csv"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Ensure the student file exists
def initialize_file():
    if not os.path.exists(STUDENT_FILE):
        df = pd.DataFrame(columns=["ID", "Name", "Age", "Grade", "Email"])
        df.to_csv(STUDENT_FILE, index=False)

# GUI Application Class
class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("700x500")
        self.create_login_page()

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
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            messagebox.showinfo("Success", "Login successful!")
            self.create_admin_panel()
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def create_admin_panel(self):
        self.clear_root()
        tk.Label(self.root, text="📋 Admin Panel", font=("Arial", 18)).pack(pady=15)
        tk.Button(self.root, text="➕ Add Student", width=20, command=self.create_add_student_page).pack(pady=5)
        tk.Button(self.root, text="📄 View Students", width=20, command=self.create_view_students_page).pack(pady=5)
        tk.Button(self.root, text="➖ Delete Student", width=20, command=self.create_delete_student_page).pack(pady=5)
        tk.Button(self.root, text="🚪 Logout", width=20, command=self.create_login_page).pack(pady=5)

    def create_add_student_page(self):
        self.clear_root()
        tk.Label(self.root, text="Add New Student", font=("Arial", 16)).pack(pady=10)
        labels = ["ID", "Name", "Age", "Grade", "Email"]
        self.entries = {}

        for label in labels:
            tk.Label(self.root, text=label).pack()
            entry = tk.Entry(self.root)
            entry.pack()
            self.entries[label] = entry

        tk.Button(self.root, text="Add Student", command=self.add_student).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_admin_panel).pack()

    def add_student(self):
        student_data = {key: entry.get().strip() for key, entry in self.entries.items()}
        if not all(student_data.values()):
            messagebox.showerror("Error", "All fields are required.")
            return

        df = pd.read_csv(STUDENT_FILE)
        if student_data["ID"] in df["ID"].astype(str).values:
            messagebox.showerror("Error", "Student ID already exists.")
            return

        df = pd.concat([df, pd.DataFrame([student_data])], ignore_index=True)
        df.to_csv(STUDENT_FILE, index=False)
        messagebox.showinfo("Success", "Student added successfully.")
        self.create_admin_panel()

    def create_view_students_page(self):
        self.clear_root()
        tk.Label(self.root, text="All Students", font=("Arial", 16)).pack(pady=10)
        try:
            df = pd.read_csv(STUDENT_FILE)
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

    def create_delete_student_page(self):
        self.clear_root()
        tk.Label(self.root, text="Remove Student", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Enter Student ID:").pack()
        self.delete_entry = tk.Entry(self.root)
        self.delete_entry.pack()
        tk.Button(self.root, text="Delete", command=self.delete_student).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_admin_panel).pack()

    def delete_student(self):
        student_id = self.delete_entry.get().strip()
        try:
            df = pd.read_csv(STUDENT_FILE)
            df["ID"] = df["ID"].astype(str)
            if student_id in df["ID"].values:
                df = df[df["ID"] != student_id]
                df.to_csv(STUDENT_FILE, index=False)
                messagebox.showinfo("Success", "Student removed successfully.")
                self.create_admin_panel()
            else:
                messagebox.showerror("Error", "Student ID not found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Student file not found.")

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Main Application Start
if __name__ == "__main__":
    initialize_file()
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()