weather=tuple(list(input("In the form of 0s and 1s \n0s for rainy days and 1s for sunny days").split(",")))
sunny = 0
rainy = 0
for i in range(0,len(weather)):
    if(weather[i]==0):
        rainy +=1
    else:
        sunny+=1

if(sunny>rainy):
    print ("The weather is good.")
else:
    print("The weather is bad.")