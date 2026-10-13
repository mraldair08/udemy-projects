programming_dictionary = {
    "bug": "es un bug", 
    "function": "Es una funcion"
    }

#print(programming_dictionary["bug"])

#Add
programming_dictionary["loop"] = "Nueva definicion"

#print(programming_dictionary)

empty_dictionary = {}

#Wipe an existing dictionary
#programing_dictionary = {}
#print(programing_dictionary)

#Edit an item
programming_dictionary["bug"] = 'A moth in the computer'
#print(programming_dictionary)

#Loop
'''for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])'''
 
''' Ejercicio   
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60,
}

student_grades = {}
for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81 and score < 90:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71 and score < 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades) '''

