import random

choices = ["rock","paper","scissors"]

while True:
    user = input(" Choose rock, paper or scissors: ").lower()
    if user not in choices:
        print (" Ivalid Choice. Please try agian by selecting rock, paper or scissor ")
        continue
    computer = random.choice(choices)

    print(f" \nYou: {user} | Computer: {computer} ")

    if user == computer:
        print(" It's a tie! ")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper") :
        print (" You win! ")
    else:
        print (" You lose! ")

    if input ("  Do you want to play again?  Answer with - Y (To play another match) or N (To QUIT becuase the computer's too good)").lower() != "y":
        break