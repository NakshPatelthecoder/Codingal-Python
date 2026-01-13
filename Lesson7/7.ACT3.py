print(" Enter Marks obtained in 5 Subjects ")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

tot = mark1 + mark2 + mark3 + mark4 + mark5
avg = tot/5

if avg>=90 and avg<=100:
    print (" You have passed with a Distinctionn and A* ")
elif avg>=89 and avg<=70:
    print(" You haved passed with a Credit and A  ")
else:
    print(" You have failed and will have a concerns meeting ")