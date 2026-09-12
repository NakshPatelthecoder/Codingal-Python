
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x300")


def info():
    messagebox.showinfo(
        "Information",
        "This is a virus scanner app\n\n"
        "click on scan button to start.")

def remove_virus():
    response = messagebox.askyesno(
        "Remove Virus",
        "Are you sure you want to remove the virus?\n\n"
        "Action is required to remove the virus. "
        "Please click Yes to remove the virus or No to cancel."
    )

    if response:
        messagebox.showinfo("Virus Removed", "The virus has been removed.")
    else:
        messagebox.showinfo("Virus Not Removed", "The virus has not been removed.")
        
def virus():
    messagebox.showerror(
        "Virus Detected",
        "A virus has been detected on your device.\n\n"
        "Action is required to remove the virus. "
        "Please click OK to acknowledge and continue."
    )
    remove_virus()

        
def warning():
    messagebox.showwarning(
        "Warning",
        "This is a warning message.\n\n"
        "Please be advised that a scan has been successfully completed on your device. "
        "As a result, a warning has been issued because a potential threat was detected. "
        "Please click OK to acknowledge and continue."
    )
    virus()


def scan_confirmation():
    response = messagebox.askyesno(
        "Scan Confirmation",
        "Are you sure you want to scan your device?\n\n"
        "Please click Yes to start the scan or No to cancel."
    )

    if response:
        messagebox.showinfo("Scan Started", "The scan has started.")
        warning()
    else:
        messagebox.showinfo("Scan Cancelled", "The scan has been cancelled.")




tk.Button(root, text="About", command=info).pack(pady=5)
tk.Button(root, text="Scan", command=scan_confirmation).pack(pady=5)

root.mainloop()