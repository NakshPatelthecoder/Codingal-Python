n = int(input("How many first n natural numbers would you like to add?"))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print ("Sum =", sum)