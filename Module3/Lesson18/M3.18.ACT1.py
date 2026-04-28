try:
    number = int(input(" Please enter a number: "))
    print(number)
except ValueError as e:
    print (" An exception has occured. ",e)
finally:
    print(" ***PROGRAM EXECUTED*** ")