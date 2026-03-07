# Program to calculate how many digits are entered by a user

user_input = input("Enter number: ")

digit_count = 0
index = 0

while index < len(user_input):
    if user_input[index].isdigit():
        digit_count += 1
    index += 1

print("Total digits entered:", digit_count)