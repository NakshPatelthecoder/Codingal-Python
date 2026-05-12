import random
import time

def getRandomDate(startDate , endDate): #Defining the Function
    print(" Printing a random date between ", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = " %m/%d/%Y "

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime   = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print (" The Random Date is  ", getRandomDate(input( " Please enter a start date in the mm/dd/yy format "),(input( " Please enter a end date in the mm/dd/yy format "))))