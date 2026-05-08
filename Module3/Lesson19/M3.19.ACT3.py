import math

print (" The Floor and Ceiling value of 23.56 are: "+ str(math.ceil(23.56)) + " , " +str(math.floor(23.56)))

x = int(input(" Enter a number: "))
y = int(input(" Enter a  negative number: "))
print (" The value of x after copying the sign from y is: "+str(math.copysign(x,y)))

print(" The absolute value of -96 and 56 are: " +str(math.fabs(-96)) + " , " +str(math.fabs(56)))

print(" The GCD of 24 & 56 : " +str(math.gcd(24,56)))