from tkinter import *

root = Tk()
root.title("Number Pad")
root.geometry("250x300")


N = [[9, 8, 7],[6, 5, 4],[3, 2, 1],["#", 0, "*"]]

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(0, 3):
        F = Frame(master=root,
                  relief=RAISED,
                  borderwidth=1
                 )
        F.grid(row=i, column=j)
        L = Label(master=F,text=N[i][j],bg = "#0D8094")       
        L.pack(padx=3, pady=3)



root.mainloop()