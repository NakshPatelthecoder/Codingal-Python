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