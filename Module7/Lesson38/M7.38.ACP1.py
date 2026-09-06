import tkinter as tk

def check_in():
    # 1. Get the participant's name from the Entry widget
    name = name_entry.get().strip()
    
    # Use a default name if the field is empty
    if not name:
        name = "Participant"
        
    # 2. Clear any existing content in the Text area
    output_text.delete("1.0", tk.END)
    
    # 3. Create a multi-line welcome message
    welcome_message = (
        f"Welcome, {name}!\n"
        "Thank you for checking in to our workshop.\n"
        "Date: September 6, 2026\n"
        "We hope you have a great learning experience!"
    )
    
    # 4. Insert the message into the Text area
    output_text.insert(tk.END, welcome_message)

# Create the main desktop window
root = tk.Tk()
root.title("Workshop Participant Greeting")
root.geometry("450x350")

# Instruction Label
instruction_label = tk.Label(
    root, 
    text="Please enter your name below and click 'Check In' to receive your welcome message:",
    wraplength=400,
    justify="left"
)
instruction_label.pack(pady=10)

# Label for the entry field
name_label = tk.Label(root, text="Participant Name:")
name_label.pack(pady=(5, 0))

# Entry Widget to collect the participant's name
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

# Check In Button that runs the greeting function
check_in_button = tk.Button(root, text="Check In", command=check_in)
check_in_button.pack(pady=10)

# Output Area Label
output_label = tk.Label(root, text="Welcome Message:")
output_label.pack(pady=(10, 0))

# Text Widget for the multi-line welcome message
output_text = tk.Text(root, height=6, width=50)
output_text.pack(pady=5)

# Start the application loop
root.mainloop()
