# Square it Out!

# Ask the user for the start and end numbers
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Create a list of square values
squares = []

for num in range(start, end + 1):
    squares.append(num ** 2)

# Separate odd and even square values
even_squares = []
odd_squares = []

for square in squares:
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

# Display the results
print("\nAll square values:")
print(squares)

print("\nEven square values:")
print(even_squares)

print("\nOdd square values:")
print(odd_squares)