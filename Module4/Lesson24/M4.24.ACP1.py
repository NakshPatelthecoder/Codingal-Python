# Input two sets
set1 = set(map(int, input("Enter elements of first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by spaces: ").split()))

# Find symmetric difference
result = set1.symmetric_difference(set2)

# Display result
print("Symmetric Difference:", result)