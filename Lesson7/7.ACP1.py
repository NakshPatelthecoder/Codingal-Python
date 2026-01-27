# ASCII Value Checker

character = input("Enter a single character: ")

# Check if only one character is entered
if len(character) == 1:
    ascii_value = ord(character)
    print("The ASCII value of", character, "is:", ascii_value)
else:
    print("Please enter only ONE character.")
