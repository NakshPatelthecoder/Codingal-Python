import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("ATM PIN Setup")
window.geometry("500x500")

# ---------------- ACCOUNT DETAILS FRAME ----------------

account_frame = tk.Frame(
    window,
    relief="raised",
    borderwidth=3
)
account_frame.place(x=40, y=40, width=420, height=150)

# Title
title = tk.Label(
    account_frame,
    text="Account Details",
    font=("Arial", 16, "bold")
)
title.place(x=130, y=10)

# Account number
account_label = tk.Label(
    account_frame,
    text="Account Number:"
)
account_label.place(x=20, y=55)

account_entry = tk.Entry(account_frame)
account_entry.place(x=150, y=55)

# PIN
pin_label = tk.Label(
    account_frame,
    text="Enter PIN:"
)
pin_label.place(x=20, y=90)

pin_entry = tk.Entry(
    account_frame,
    show="*"
)
pin_entry.place(x=150, y=90)


# ---------------- KEYPAD FRAME ----------------

keypad_frame = tk.Frame(
    window,
    relief="sunken",
    borderwidth=3
)
keypad_frame.place(x=40, y=210, width=420, height=200)

keypad_title = tk.Label(
    keypad_frame,
    text="Keypad",
    font=("Arial", 14, "bold")
)
keypad_title.grid(row=0, column=0, columnspan=3, pady=10)

# Function for keypad buttons
def add_number(number):
    pin_entry.insert(tk.END, number)

# Keypad numbers
numbers = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    "0"
]

row = 1
column = 0

for number in numbers:
    button = tk.Button(
        keypad_frame,
        text=number,
        width=6,
        height=2,
        command=lambda n=number: add_number(n)
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )

    column += 1

    if column == 3:
        column = 0
        row += 1


# ---------------- SUBMIT BUTTON ----------------

def show_details():
    account = account_entry.get()
    pin = pin_entry.get()

    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        "ATM PIN Setup\n\n"
        + "Account Number: " + account + "\n"
        + "PIN: " + "*" * len(pin)
    )

submit_button = tk.Button(
    window,
    text="Set Up PIN",
    font=("Arial", 12, "bold"),
    command=show_details
)
submit_button.place(x=180, y=425, width=140, height=40)


# ---------------- TEXT WIDGET ----------------

output = tk.Text(
    window,
    height=3,
    width=45
)
output.place(x=40, y=470)


# Start the program
window.mainloop()