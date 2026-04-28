try:
    num1,num2 = eval(input(" Please enter 2 numbers that are separated by a comma each like this :- 1,2 "))
    result = num1 / num2
    print (" The result is : ", result)
# Using multiple except locks for differnt types of error that may appear in a program
except ZeroDivisionError:
    print (" Division by 0 results in an error. Due to this please try again without dividing by 0. ")
except SyntaxError:
    print (" Inputting numbers that are not separted with a comma will result in an error .Due to this please try again and separate your numbers with a comma like this :- 1,2")
except:
    print (" Inputting a wrong / invalid input wil result in an error.Due to this please try again and input a correct & valid input. ")
else:
    print (" No Errors detected within the system or input ")
finally:
    print (" ***PROGRAM EXECUTED INVETABILY*** ")