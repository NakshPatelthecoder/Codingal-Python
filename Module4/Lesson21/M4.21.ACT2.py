def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print(" List of words with the first and last character are the same: ", lst)
    return ctr
number_of_elmts = int(input(" How many elements / characters do you want to be found? "))
nums = []
for i in range(number_of_elmts):
    nums.append(input(" Please enter your choosen elements/characters: "))
print(nums)
count = match_words(nums)
print(" The number of words that have the same first and last character are: ", count)