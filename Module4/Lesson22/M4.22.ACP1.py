# Python program to calculate the product of all numbers in a tuple

numbers = (2, 3, 4, 5)

product = 1

for num in numbers:
    product *= num

print("The product of the tuple elements is:", product)