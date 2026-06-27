import random

# Characters to choose from
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

# Combine letters and numbers
characters = letters + numbers

# Create an empty password
password = ""

# Generate an 8-character password
for i in range(8):
    password = password + random.choice(characters)

# Display the password
print("Random Password:", password)