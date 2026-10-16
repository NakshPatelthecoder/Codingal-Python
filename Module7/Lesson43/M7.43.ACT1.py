import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order Management System")
        self.menu_items = {
            "Fries Meal": 5.99,
            "Pizza": 8.99,
            "Pasta": 7.49,
            "Salad": 4.99,
            "Soda": 1.99
        }

        self.exchange_rate = 94

        self.setup_background(root) 
        frame = ttk.Frame(root)
        frame.place(x=10, y=10)

        ttk.Label(
            frame,
            text="Restuarnt Order Management System",
            font=("Arial", 20, "bold"),            
        ).grid(row=0, columnspan=3, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}
        for i, (item, price) in enumerate(self.menu_items.items()):
            label = ttk.Label(frame,
                               text=f"{item} - ${price}"
            )
            label.grid(row=i + 1, column=0, padx=10, pady=5)
            self.menu_labels[item] = label
            self.currency_var = tk.StringVar()
            ttk.Label(
                frame,
                text="Currency:",
                font=("Arial", 12)
            ).grid(
                row=len(self.menu_items) + 1, 
                column=0, 
                padx=10, 
                pady=5
            )

            currency_dropdown = ttk.Combobox(
                frame,
                textvariable=self.currency_var,
                values=["USD", "INR"],
            )
            currency_dropdown.current(0)
            self.currency_var.trace("w", self.update_menu_prices)

            order_button = ttk.Button(
                frame,
                text="Place Order",
                command=self.place_order
            )
            order_button.grid(
                row=len(self.menu_items) + 2,
                columnspan=3,
                padx=10,
                pady=10
            )

    def setup_background(self, root):
        bg_width = 800
        bg_height = 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()

    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1


    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        
        for item, price in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item]* rate
                cost = price * quantity
                total_cost += cost

                if quantity > 0:
                    order_summary +=(
                        f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
                    )

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Summary", order_summary)
            messagebox.showinfo("Order Placed", "Your order has been placed successfully!")
        else:
            messagebox.showwarning("No Items Selected", "Please select at least one item to place an order.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.mainloop()