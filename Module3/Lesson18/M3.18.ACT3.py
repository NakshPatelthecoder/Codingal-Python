valid = False
while not valid: # Using a nested while loop
    try:
        n = int(input(" Please enter a number: "))
        # Enter an even number
        while n%2==0:

            print(" Bye. Have a nice day ")
        valid =True
    except ValueError:
        print (" Invalid ")