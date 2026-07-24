class DailyDataHelper:
    def __init__(self):
        self.data = []
        print("Daily Data Helper started.")

    def add_data(self, value):
        self.data.append(value)
        print(f"{value} added.")

    def show_data(self):
        if len(self.data) == 0:
            print("No data available.")
        else:
            print("\nDaily Data:")
            for index, value in enumerate(self.data):
                print(f"{index}: {value}")

    def search_data(self, target):
        found = False
        for index, value in enumerate(self.data):
            if value == target:
                print(f"'{target}' found at index {index}.")
                found = True

        if not found:
            print(f"'{target}' was not found.")

    def __del__(self):
        print("Daily Data Helper object destroyed.")


# Main Program
helper = DailyDataHelper()

while True:
    print("\n--- Daily Data Helper ---")
    print("1. Add Data")
    print("2. Show Data")
    print("3. Search Data")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter data: ")
        helper.add_data(item)

    elif choice == "2":
        helper.show_data()

    elif choice == "3":
        search = input("Enter value to search: ")
        helper.search_data(search)

    elif choice == "4":
        print("Goodbye!")
        del helper
        break

    else:
        print("Invalid choice. Try again.")