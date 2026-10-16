import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Reading Schedule Planner")
root.geometry("400x300")

title = tk.Label(root, text="Reading Schedule Planner",
                 font=("Arial", 18, "bold"))
title.pack(pady=20)

label = tk.Label(root, text="Plan how many pages to read each day!")
label.pack(pady=10)


# Open the reading planner
def open_planner():
    window = tk.Toplevel(root)
    window.title("Reading Planner")
    window.geometry("400x450")

    # Book title
    tk.Label(window, text="Book title:").pack()
    book_entry = tk.Entry(window)
    book_entry.pack(pady=5)

    # Total pages
    tk.Label(window, text="Total pages in the book:").pack()
    total_entry = tk.Entry(window)
    total_entry.pack(pady=5)

    # Pages per day
    tk.Label(window, text="Pages to read each day:").pack()
    daily_entry = tk.Entry(window)
    daily_entry.pack(pady=5)

    # Results label
    result = tk.Label(window, text="", justify="left")
    result.pack(pady=15)

    # Calculate the reading schedule
    def calculate():
        try:
            total = int(total_entry.get())
            daily = int(daily_entry.get())

            if total <= 0 or daily <= 0:
                messagebox.showerror(
                    "Error", "Enter numbers greater than zero."
                )
                return

            # Floor division and modulo
            full_days = total // daily
            remaining_pages = total % daily

            days = full_days
            if remaining_pages > 0:
                days = days + 1

            book = book_entry.get()
            if book == "":
                book = "Your book"

            result.config(
                text=f"Book: {book}\n"
                     f"Total pages: {total}\n"
                     f"Pages per day: {daily}\n"
                     f"Complete days: {full_days}\n"
                     f"Remaining pages: {remaining_pages}\n"
                     f"Total days needed: {days}\n"
                     f"Progress: 0% (starting)"
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter whole numbers for the pages."
            )

    # Reset the entries and results
    def reset():
        book_entry.delete(0, tk.END)
        total_entry.delete(0, tk.END)
        daily_entry.delete(0, tk.END)
        result.config(text="")

    tk.Button(window, text="Calculate Schedule",
              command=calculate).pack(pady=5)

    tk.Button(window, text="Reset",
              command=reset).pack(pady=5)


# Main window buttons
tk.Button(root, text="Open Reading Planner",
          command=open_planner).pack(pady=15)

tk.Button(root, text="Exit",
          command=root.destroy).pack(pady=5)

# Start the program
root.mainloop()