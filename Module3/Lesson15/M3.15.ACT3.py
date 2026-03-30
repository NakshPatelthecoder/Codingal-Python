def add (P , Q):
    # This function is used for adding 2 numbers
    return P + Q
def subtract (P , Q):
    # This function is used for subtracting 2 numbers
    return P - Q
def multiply (P , Q):
    # This function is used for multipling 2 numbers
    return P * Q
def divide (P , Q):
    # This function is used for dividing 2 numbers
    return P / Q

# Phase 2: Inputs
print (" Please selct the operation. ")
print (" a. Addition ")
print (" b. Subtraction ")
print (" c. Multiplication ")
print (" d. Division ")

choice = input(" Please enter your choice (It must be a./b./c./d.) ")

num1 = int(input(" Please enter the first number: "))
num2 = int(input(" Please enter the second number: "))

if choice == 'a':
    print (num1, " + ", num2, " = ", add(num1, num2))

elif  choice == 'b':
    print (num1, " - ", num2, " = ", subtract(num1, num2))

elif  choice == 'c':
    print (num1, " * ", num2, " = ", multiply(num1, num2))

elif  choice == 'd':
    print (num1, " / ", num2, " = ", divide(num1, num2))

else:
    print (" Error : Invalid Input - Try again")