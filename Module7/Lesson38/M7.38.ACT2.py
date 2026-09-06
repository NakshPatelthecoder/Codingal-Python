from tkinter import *
from datetime import date

R = Tk()
R.title("Getting Started with Widgets")
R.geometry("400x300")

L = Label(text="Hey there!", fg="white", bg="#0004FF")

N_L = Label(text="Full Name", bg="#3895D3")
N_E = Entry()

def D():
    N = N_E.get()
    global M
    M = "Welcome to the Application! \n Today's date is :"
    G = "Hello"+N+"\n"
    TB.insert(END, G)
    TB.insert(END, M)
    TB.insert(END, date.today())

TB = Text(height=3)

BTN = Button(text="Begin", command=D, height=1, bg="#18A073", fg="white")

L.pack()
N_L.pack()
N_E.pack()
BTN.pack()
TB.pack()

R.mainloop()