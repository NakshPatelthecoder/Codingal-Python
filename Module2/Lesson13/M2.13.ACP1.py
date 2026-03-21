rowSize = int(input("Enter the number of rows: "))

space = rowSize - 1

for i in range(1, rowSize + 1):
    # Print spaces
    for j in range(1, space + 1):
        print(end="  ")
    
    space = space - 1

    # Print stars
    for j in range(1, i + 1):
        print("*", end=" ")

    print()