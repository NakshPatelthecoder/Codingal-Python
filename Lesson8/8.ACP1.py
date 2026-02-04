a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))
c = int(input("Enter value 3: "))
d = int(input("Enter value 4: "))
e = int(input("Enter value 5: "))

# Right rotation
a, b, c, d, e = e, a, b, c, d

print("After right rotation:", a, b, c, d, e)
