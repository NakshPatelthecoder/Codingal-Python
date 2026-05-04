try:
    age = int(input("Enter your age: "))

    if age <= 0:
        print("Invalid age. Age must be a positive number.")
    else:
        print("Valid age entered.")

        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")

except ValueError:
    print("Invalid input. Please enter a numeric value.")