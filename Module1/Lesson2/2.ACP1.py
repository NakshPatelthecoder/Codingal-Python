# Raj and his friends' birthdays

# Create an empty dictionary to store names and birthdays
birthdays = {}

# Number of friends
friends = 5

# Ask for names and birthdays
for i in range(friends):
    name = input("Enter friend's name: ")
    birthday = input("Enter birthday (DD/MM/YYYY): ")
    birthdays[name] = birthday

# Print all birthdays
print("\nBirthdays of Raj's friends:")
for name, birthday in birthdays.items():
    print(name, ":", birthday)