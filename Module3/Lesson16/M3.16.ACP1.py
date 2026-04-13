def shutdown(user_input):
    if user_input == "Yes":
        return "Shutting down..."
    elif user_input == "No":
        return "Abort shutdown."
    else:
        return "Sorry."

# Taking input from user
choice = input("Enter Yes or No: ")

# Calling the function and printing result
result = shutdown(choice)
print(result)