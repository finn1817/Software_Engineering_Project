import tkinter as tk
from tkinter import messagebox, simpledialog
import issue_manager

def open_main_menu(root):
    """Open role selection menu."""
    root.withdraw()
    menu = tk.Toplevel()
    menu.title("Select Role")
    menu.geometry("400x300")

    tk.Label(menu, text="Choose your role:", font=("Arial", 12)).pack(pady=10)
    tk.Button(menu, text="User (Report Issue)", command=lambda: user_ui(menu), width=20).pack(pady=5)
    tk.Button(menu, text="Admin (Manage Reports)", command=lambda: admin_ui(menu), width=20).pack(pady=5)
    tk.Button(menu, text="Support Staff (Review)", command=lambda: support_ui(menu), width=20).pack(pady=5)
    tk.Button(menu, text="Manager (Oversee System)", command=lambda: manager_ui(menu), width=20).pack(pady=5)
    tk.Button(menu, text="Exit", command=root.quit, width=20).pack(pady=10)

def user_ui(parent):
    """User Interface - Report an Issue."""
    parent.withdraw()
    user_window = tk.Toplevel()
    user_window
