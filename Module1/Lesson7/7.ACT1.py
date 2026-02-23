x = 5
if (type(x) is int):
    print (" True ")
else:
    print (" False ")

x = 5.5
if (type(x) is not float):
    print (" True ")
else:
    print(" False ")

x = 20
y = 20
if (x is y):
    print (" x & y have the SAME identity ")
else:
    print (" x & y  have the DIFFERENT identities ")

y = 30
if (x is not y ):
    print(" x & y have the DIFFERENT identities ")
else:
    print (" x & y have the SAME identity  ")