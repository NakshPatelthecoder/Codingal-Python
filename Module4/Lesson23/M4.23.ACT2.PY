# Intialize dictionary
test_dict = {"Codingal":2, "is":2, "for":2, "Coding":1}

# Printing the original dictionary
print("The Original Dictionary :" + str(test_dict))

# Intialize value
K=2

#Using a loop
#Using selective key values in a dictionary
res = 0
for key in test_dict:
    if test_dict[key] ==K:
        res += 1

# Printing the result
print("The frequencey of K is :" + str(res))