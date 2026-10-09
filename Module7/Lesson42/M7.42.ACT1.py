from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Window Top")

def top_window():
    top = Toplevel()
    top.geometry("180x100")
    top.title("Top Window")
    label = Label(top, text="This is a Top Level Window")
    label.pack(pady=20)

    top.mainloop()

label = Label(root, text="This is the Root Window")
btn = Button(root, text="Click here to open another window", command=top_window)

label.pack(pady=20)
btn.pack(pady=10)

root.mainloop()