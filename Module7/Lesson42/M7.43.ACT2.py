from tkinter import *
from tkinter import messagebox 


root = Tk()
root.title("Denomination Calculator")
root.configure(bg="lightblue")
root.geometry("650x400")



label1 = Label(
    root,
    text= "Hey User! Welcome to the Denomination Calculator. This app will help you calculate the number of notes and coins needed for a given amount.",
    bg="lightblue",
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    )
    if MsgBox == "ok":
        topwin()

button1 = Button(
    root,
    text="Click Here to Calculate Denomination Count",
    command=msg,
    bg="brown",
    fg="white",
)
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="lightblue")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter the amount to calculate denomination count:", bg="lightgrey")
    entry = Entry(top)

    lb1 = Label(
        top,
        text="Denomination Count",
        bg="lightgrey"
    )

    l1 = Label(top, text="2000: ", bg="lightgrey")
    l2 = Label(top, text="500: ", bg="lightgrey")
    l3 = Label(top, text="100: ", bg="lightgrey")

    t1  = Entry(top)
    t2  = Entry(top)
    t3  = Entry(top)

    def calculate():
        try:
            amount = int(entry.get())
            count_2000 = amount // 2000
            amount %= 2000
            count_500 = amount // 500
            amount %= 500
            count_100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, str(count_2000))
            t2.insert(0, str(count_500))
            t3.insert(0, str(count_100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    button = Button(top, text="Calculate", command=calculate, bg="brown", fg="white"
    )

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    button.place(x=220, y=110)

    lb1.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()