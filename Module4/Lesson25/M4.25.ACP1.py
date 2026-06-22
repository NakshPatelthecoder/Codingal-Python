# 1. Take a number from the user and create lists of odd and even numbers below it

num = int(input("Enter a number: "))

odd_numbers = [x for x in range(num) if x % 2 != 0]
even_numbers = [x for x in range(num) if x % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

# 2. Create a list of fruits and capitalize the first letter of each fruit

fruits = ["apple", "banana", "orange", "grape", "mango"]
updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Updated fruits list:", updated_fruits)