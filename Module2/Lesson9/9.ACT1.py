# Taking  inputs for students eligilbility for the exam

#Taking Medical Cause Input
medical_cause = input(" Do you have a valid medical cause - Yes or No: ").lower()

#Taking attendance input
atten = int(input(" Enter the attendance of the student: "))

# Checking the user input to check if the students is eligible for the exam

if medical_cause == 'yes':  #Checking Condition 'Medical Cause'
    print (" You are eligible for the exam. Please see details to come")
else:
    if atten>=75:   #Checking condition 'Attendance'
        print (" You are eligible for the exam.Please see detatils to come.")
    else:
        print (" You are NOT permitted to complete the exam. ")