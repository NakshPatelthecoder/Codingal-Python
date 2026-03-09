lower = int(input(" Enter a Lower Range: "))
upper = int(input(" Enter a Upper Range: "))

print(" Prime Numbers between  ", lower, " and ", upper, "  are: ")
for num in range(lower,upper + 1):
    # All Prime Numbers are GREATER than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        
        else:
            print(num)
