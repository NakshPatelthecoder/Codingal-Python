import tkinter as tk
from tkinter import filedialog


# Open an existing letter
def open_letter():
    filename = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if filename:
        with open(filename, "r") as file:
            letter = file.read()

        text_box.delete("1.0", tk.END)
        text_box.insert("1.0", letter)


# Save the current letter
def save_letter():
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if filename:
        letter = text_box.get("1.0", tk.END)

        with open(filename, "w") as file:
            file.write(letter)


# Create the window
window = tk.Tk()
window.title("Letter Writing Application")
window.geometry("700x500")


# Title
title = tk.Label(window, text="Letter Writing Application", font=("Arial", 18))
title.grid(row=0, column=0, columnspan=2, pady=10)


# Text editor
text_box = tk.Text(window, width=80, height=20)
text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


# Buttons
open_button = tk.Button(window, text="Open Letter", command=open_letter)
open_button.grid(row=2, column=0, padx=10, pady=10)

save_button = tk.Button(window, text="Save Letter", command=save_letter)
save_button.grid(row=2, column=1, padx=10, pady=10)


# Run the application
window.mainloop()