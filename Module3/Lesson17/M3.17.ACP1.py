# Function to calculate change
def calculate_change(bill, paid):
    return paid - bill  # return statement gives back the result

# Given values
bill = 2.50
paid = 4.00

# Call the function
change = calculate_change(bill, paid)

# Output the result
print("Change to return: $", change)