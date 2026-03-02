num = int(input(" Enter a number: "))
power = len(str(num))
sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10

if num == sum:
    print (num, " is an Armstrong number. ")
else:
    print (num, " is NOT an Armstrong number. ")