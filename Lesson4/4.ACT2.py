# Taking the total amount as an input from the user
Amount=int(input("  Please enter the amount for the withdrawal: "))

# Calculating the number of notesof different denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
note_4 = (((Amount%100)%50)%10)//5
note_5 = ((((Amount%100)%50)%10)%5)//1

# Giving the amount and number of notes for the withdrawal
print( " The number of 100 rupee notes is: ", note_1 )
print( " The number of 50 rupee notes is: ", note_2 )
print( " The number of 10 rupee notes is: ", note_3 )
print( " The number of 5 rupee notes is: ", note_4 )
print( " The number of 1 rupee notes is: ", note_5 )