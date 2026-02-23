a = int(input( " Please enter your first number." ))
b = int(input( " Please enter your second number." ))
c = int(input( " Please enter your third and final number." ))

if a and b and c :
    print (" All the numbers have booleans value as True. ") 
else:
    print (" At least one number has boolean value as False. ")

# Or version#

if a > 0 or b > 0 or c > 0 :
    print (" Either numbers are greater than 0 ")
else:
    print (" No number is greater than 0 ")