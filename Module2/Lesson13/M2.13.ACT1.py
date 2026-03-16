print(" Half Pyramid of Stars (*): ")
n = int(input(" Enter the number of of rows the Half Pyramid should be for your preference: "))
for i in range (n):
    for j in range(i+1):
        print("*", end="")
    print( )