'''fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    
student_scores = [150, 250, 100, 135, 200]
total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score
 
print(sum)
print(total_exam_score)

print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score) 

#Range Function
total = 0
for number in range(1,101):
    total += number
print(total) 

for number in range(1, 101):
    if number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    elif number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    else: 
        print(number) '''
import random        
        
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]
symbols = ['!', '@', '#', '$', '%', '^', '&' ]
password = []
print("Password Generator")
number_letters = int(input("How many letters would you like in your password: "))
number_numbers = int(input("How many numbers would you like in your password: "))
number_symbols = int(input("How many symbols would you like in your password: "))

for i in range(number_letters):
    password.append(random.choice(letters))
    
for i in range(number_numbers):
    password.append(random.choice(numbers))
    
for i in range(number_symbols):
    password.append(random.choice(symbols))
    
''' En orden
password_string = "".join(password)
print(f"Your password is: {password_string}")'''


random.shuffle(password)
password_string = "".join(password)
print(f"Your password is: {password_string}")

password_str = ""
for char in password:
    password_str += char
    
print(f"Your password is: {password_str}")
    
    
