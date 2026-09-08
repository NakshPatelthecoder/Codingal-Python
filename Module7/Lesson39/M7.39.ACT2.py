from tkinter import *

root = Tk()
root.title("A1 Company Login - Finance Department")
root.geometry("400x400")

F = Frame(master=root, height=200, width=360, bg="#000000")

lbl1 = Label(F, text="Full Name", bg="#1F51FF", fg="#FFFFFF",width=12)
lbl2 = Label(F, text="Employee ID", bg="#FF3131", fg="#FFFFFF",width=12)
lbl3 = Label(F, text="Email ID", bg="#FFB931", fg="#FFFFFF",width=12)
lbl4 = Label(F, text="Password", bg="#31FF3F", fg="#FFFFFF",width=12)

name_entry = Entry(F)
id_entry = Entry(F)
email_entry = Entry(F)
password_entry = Entry(F)

def display():
    name = name_entry.get()
    message = "Hello " + name + ", Welcome to A1 Company! Your shift has been logged and your Line Manager is awarred of your login."
    textbox.insert(END, message)

textbox = Text(bg="#00008b", fg="#FFFFFF")

btn = Button(text="Login", bg="#FF31A6", fg="#FFFFFF", command=display)

F.place(x=20, y=0)
lbl1.place(x=20, y=20)
lbl2.place(x=20, y=50)
lbl3.place(x=20, y=80)
lbl4.place(x=20, y=110)
name_entry.place(x=150, y=20)
id_entry.place(x=150, y=50)
email_entry.place(x=150, y=80)
password_entry.place(x=150, y=110)
btn.place(x=150, y=140)
textbox.place(x=20, y=180)
F.place(x=20, y=0)

root.mainloop()