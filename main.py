import tkinter as tk
from ui import open_main_menu

# main window
root = tk.Tk()
root.title("HelpBot - Team Issue Tracker")
root.geometry("400x300")

tk.Label(root, text="Welcome to HelpBot", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Open App", command=lambda: open_main_menu(root), width=20).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

root.mainloop()
