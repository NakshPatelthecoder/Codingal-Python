student_data = {
"id1": {"Name": "Sara", "Class": "V", "subject_integration": "English, Math, Science"},
"id2": {"Name": "David", "Class": "V", "subject_integration": "English, Math, Science"},
"id4": {"Name": "Surya", "Class": "V", "subject_integration": "English, Math, Science"},
}



result = {}
seen_keys = [] #Using a list instead of a set

for student_ID, details in student_data.items():
    unique_key = (details["Name"], details["Class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_ID] = details

#Print Output Line by Line
for k, v in result.items():
    print(k, ":", v)
