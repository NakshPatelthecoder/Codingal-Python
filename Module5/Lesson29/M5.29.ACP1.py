class Account:
    def __init__(self, account_name, pin):
        self.__account_name = account_name
        self.__pin = pin

    # Getter
    def get_pin(self):
        return "*" * len(str(self.__pin))

    # Setter
    def set_pin(self, new_pin):
        if len(str(new_pin)) == 4 and str(new_pin).isdigit():
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("PIN must be exactly 4 digits.")

    # Check entered PIN
    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("Access Granted")
        else:
            print("Incorrect PIN")

    # Special function
    def __str__(self):
        return f"Account Holder: {self.__account_name}\nStored PIN: {self.get_pin()}"


# Main Program
name = input("Enter account holder name: ")
pin = input("Create a 4-digit PIN: ")

while len(pin) != 4 or not pin.isdigit():
    pin = input("Invalid. Enter a 4-digit PIN: ")

account = Account(name, pin)

while True:
    print("\n--- Account PIN Safety Checker ---")
    print("1. View Account")
    print("2. Check PIN")
    print("3. Change PIN")
    print("4. Try to Access Private PIN")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(account)

    elif choice == "2":
        entered = input("Enter your PIN: ")
        account.check_pin(entered)

    elif choice == "3":
        new_pin = input("Enter a new 4-digit PIN: ")
        account.set_pin(new_pin)

    elif choice == "4":
        try:
            print(account.__pin)
        except AttributeError:
            print("Private attribute cannot be accessed directly.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")