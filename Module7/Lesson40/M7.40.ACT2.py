from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")

def info():
    messagebox.showinfo("Information", "This is an info message.","Please be advised that a scan has been successfully completed on your device." )

def warning():
    messagebox.showwarning("Warning", "This is a warning message.","Please be advised that a scan has been successfully completed on your device. As a result a warning has been issued as there has been a potential threat detected. Please click OK to acknowledge and continue.")
    scanconformation()

def scanconformation():
    response = messagebox.askyesno("Scan Confirmation", "Are you sure you want to scan your device?","Please be advised that a scan has been successfully completed on your device. As a result a warning has been issued as there has been a potential threat detected. Please click OK to acknowledge and continue." )
    if response:
        messagebox.showinfo("Scan Started", "The scan has started.")
    else:
        messagebox.showinfo("Scan Cancelled", "The scan has been cancelled.")

def virus():
    messagebox.showerror("Virus Detected", "A virus has been detected on your device.","Action is required to remove the virus. Please click OK to acknowledge and continue.")
    remove_virus()

def remove_virus():
    response = messagebox.askyesno("Remove Virus", "Are you sure you want to remove the virus?","Action is required to remove the virus. Please click OK to acknowledge and continue." )
    if response:
        messagebox.showinfo("Virus Removed", "The virus has been removed.")
    else:
        messagebox.showinfo("Virus Not Removed", "The virus has not been removed.")

Button(root, text="Scan Started", command=info).pack()
Button(root, text="Scan Warning", command=warning).pack()
Button(root, text="Detect Virus", command=virus).pack()

root.mainloop()