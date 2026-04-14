var = int(input(" Please enter a number that is less than 100: "))
while var>100:
    var = int(input(" Please enter a number that is less than 100: "))
num =int(input(" Enter a number that you want to skip "))
while var > 0:
    var -= 1
    if var == num:
        continue
    print(" Current variable value : ", var)
print ("  \n Goodye and we hope to see you again!")