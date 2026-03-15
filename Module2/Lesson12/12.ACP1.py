while True:
    print("\nNumber Conversion Program")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        decimal = int(input("Enter a decimal number: "))
        binary = bin(decimal)[2:]   # convert to binary and remove '0b'
        print("Binary:", binary)

    elif choice == "2":
        binary = input("Enter a binary number: ")
        decimal = int(binary, 2)    # convert binary to decimal
        print("Decimal:", decimal)

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")