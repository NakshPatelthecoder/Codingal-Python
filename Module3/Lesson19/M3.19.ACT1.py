import random
playing = True
number = str(random.randint(0,9))

print(" I will generate a random number form 0 to 9 (All Inclusive), and you have to guess the number one digit at a time. ")
print (" This game ends when you guess the correct number! ")
while playing:
    guess = input(" Give me your best guess! \n ")
    if number == guess:
        print (" !!!You win the game!!! ")
        print(" The numebr was ", number)
        break
    else:
        print(" Your guess isn't quite right , try again! \n ")