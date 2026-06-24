import tkinter as tk
from tkinter import messagebox


def show_warning():
    root = tk.Tk()
    root.withdraw()

    messagebox.showwarning(
        "Security Awareness Demo",
        "⚠ This is a simulated malicious attachment.\n\n"
        "No malware was executed.\n"
        "For demo purposes only."
    )

    root.destroy()


show_warning()