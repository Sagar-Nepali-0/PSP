import customtkinter as ctk
# No need to set theme here, it's done globally in login.py

def loginGUI():
    """Creates and returns the login GUI window and its relevant widgets."""
    # Basic set up for GUI interface
    root = ctk.CTk()
    root.title("Login - Student Profile System")
    root.iconbitmap('')  # Add an icon path if desired e.g., 'path/to/icon.ico'

    # Center the window
    window_width = 400
    window_height = 330 # Slightly taller to accommodate padding
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    root.resizable(False, False) # Prevent resizing

    # Frame for better organization
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Logo/school name
    logo = ctk.CTkLabel(main_frame,
                        text="Student Profile Management System",
                        font=ctk.CTkFont(size=18, weight="bold")) # Use CTkFont
    logo.pack(pady=(10, 25)) # More padding below logo

    # Label and entry for username
    label_username = ctk.CTkLabel(main_frame, text="Username", font=ctk.CTkFont(size=14))
    username = ctk.CTkEntry(main_frame, width=200, placeholder_text="Enter username")
    label_username.pack(pady=(5,2))
    username.pack(pady=(0,10))

    # Label and entry for password
    label_userpassword = ctk.CTkLabel(main_frame, text="Password", font=ctk.CTkFont(size=14))
    userpassword = ctk.CTkEntry(main_frame, show="*", width=200, placeholder_text="Enter password")
    label_userpassword.pack(pady=(5,2))
    userpassword.pack(pady=(0,10))

    # Button for LogIn
    button_login = ctk.CTkButton(main_frame,
                                 text="Log In",
                                 height=35, # Slightly taller button
                                 width=200,
                                 font=ctk.CTkFont(size=14, weight="bold"),
                                 # Colors can be kept or adjusted
                                 # text_color="white",
                                 # fg_color="#5e63eb",
                                 # hover_color="#4f54e3",
                                 corner_radius=8)
                                 # border_width=2 # Optional border
                                 # state="normal" # Default state
    button_login.pack(pady=20)

    # Return the root window and the widgets needed by login.py
    return root, button_login, username, userpassword