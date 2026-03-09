num = int(input(" Enter the number which must be 4 or more digits long: "))
t = num
numLen = 0

while t>0:
    numLen = numLen + 1
    t = int(t/10)

if numLen>= 4:
    numLen = int(numLen/2)
    chk = 0
    while num>0:
        rem = num%10
        if chk==numLen:
            mid1 = rem
        elif chk==(numLen-1):
            mid2 = rem
        num = int(num/10)
        chk = chk + 1
    prod = mid1*mid2
    print("\nProduct of the Middle digits (" +str(mid1)+ "*" +str(mid2)+ ") = ", prod)

else:
    print(" The number that you have provided is not 4 or more digits long. Please try again ")