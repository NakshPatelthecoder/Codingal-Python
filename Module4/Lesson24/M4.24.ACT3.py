import array as arr

# Create an array
array_1 = arr.array("i", [1, 3, 5, 3, 7, 9, 3])
print("Original array:",(array_1))

# Count the numebr of occurences
print("Number of occurences of the number 3 in the said array:", array_1.count)

array_1.reverse()
print("Reverse the order of the items")
print(array_1)