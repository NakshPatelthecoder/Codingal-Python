print(" Select your ride:")
print(" 1. Bike ")
print(" 2. Car ")

choice = int(input("Enter your choice - 1. Bike or 2. Car:"))

if (choice == 1):
    print(" What type of bike? ")
    print(" 1.Scooty\n ")
    print(" 2. SCooter\n ")

    choice2 = int(input(" If you would like a Bike please choose whether you would like a 1. Scooty or 2. Scooter "))
    if choice2 == 1:
        print(" You have selected a scooty. ")
    else:
        print(" You have selected a scooter. ")
elif (choice == 2):
    print(" What type of car? ")
    print(" 1.Sedan\n ")
    print(" 2. XUV\n ")

    choice3 = int(input(" If you would like a Car please choose whether you would like a 1. Sedan or 2. XUV "))
    if choice3 == 1:
        print(" You have selected a Sedan. ")
    else:
        print(" You have selected a XUV. ")

else:
    print(" Invalid input- try again! ")