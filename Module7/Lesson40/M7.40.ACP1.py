import tkinter as tk
from tkinter import messagebox

routine = ["Homework", "Snack", "Exercise", "Revision", "Relax"]
number = 0

def last_character(event):
    task = entry.get()
    if task:
        last.config(text="Last character: " + task[-1])

def clicked(event):
    click.config(text="You clicked the routine area!")

def next_task():
    global number
    if entry.get() == "":
        messagebox.showwarning("Warning", "Enter a task first!")
    else:
        next_label.config(text="Next task: " + routine[number])
        number += 1
        if number == len(routine):
            number = 0

window = tk.Tk()
window.title("After-School Routine Checker")
window.geometry("450x400")

title = tk.Label(
    window,
    text="After-School Routine Checker",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

tk.Label(window, text="Enter an after-school task:").pack()

entry = tk.Entry(window, width=35)
entry.pack(pady=10)
entry.bind("<KeyRelease>", last_character)

last = tk.Label(window, text="Last character:")
last.pack()

routine_box = tk.Label(
    window,
    text="CLICK THE ROUTINE AREA",
    width=30,
    height=3,
    relief="raised"
)
routine_box.pack(pady=15)
routine_box.bind("<Button-1>", clicked)

click = tk.Label(window, text="")
click.pack()

button = tk.Button(
    window,
    text="Show Next Task",
    command=next_task
)
button.pack(pady=15)

next_label = tk.Label(
    window,
    text="Next task:",
    font=("Arial", 12, "bold")
)
next_label.pack()

window.mainloop()