#List comprehension
# numbers = [1, 2, 3]
# # new_list = [new item for item in list]
# new_list = [n + 1 for n in numbers]

# print(new_list)
# print(numbers)

# name = "Angela"
# new_name = [letter for letter in name]
# print(new_name)

# range(1, 5)
# range_list = [number * 2 for number in range(1, 5)]
# print(range_list)

# names = ["Dave", "Oscar", "Luis", "Eleanor", "Caroline"]
# short_name = [name for name in names if len(name) <= 4 ]
# print(short_name)
# upper_names = [name.upper() for name in names if len(name) > 5]
# print(upper_names)
import random


# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
#new_dict = {new_key: new_value for (key,value) in dict.items()}

#Lista a diccionario
# names = ["Dave", "Oscar", "Luis", "Eleanor", "Caroline"]
# students_score = {student: random.randint(1, 100) for student in names}

#Diccionario a Diccionario
# students_score = {student: random.randint(1, 100) for student in names}
# pass_students = {student:score for (student, score) in students_score.items() if score >= 60 }

# print(students_score)
# print(pass_students)

# sentence = "Python is a programming language"
# split_sentence = sentence.split()
# new_dict = {word: len(word) for word in sentence.split()}

# print(split_sentence)
# print(new_dict)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:(degrees * 9/5) + 32  for (day, degrees) in weather_c.items()}

# print(weather_f)

numbers = [1, 4, 7, 10, 13, 16, 19, 22]

multiply_numbers = [number * 2 for number in numbers if number % 2 == 0]

print(multiply_numbers)

words = ["python", "java", "javascript", "html"]

upperword = [word.upper() for word in words]

word_lenth = {word:len(word) for word in words}
print(upperword)
print(word_lenth)


# students_score = {student: random.randint(1, 100) for student in names}