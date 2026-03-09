string = input(" Please enter your own word, phrase or sentence: ")
char = input (" Please enter your own charcater to see how many times it appears in your word,phrase or sentence: ")

i = 0
count = 0
while(i < len(string)):

    if(string[i] == char):
        count = count + 1
    i = i + 1

print(" The total number of times  ", char, " appeared = ", count)
