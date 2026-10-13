'''def greet():
    print("Good morning")
    print("Good afternoon")
    print("Good evening")
    
greet()

def greet_with_name(name):
    print(f"Good morning {name}")
    print(f"Good afternoon {name}")
    print(f"Good evening {name}")
    
greet_with_name("Louis")

def life_in_weeks(age):
    age =  (90 - age) * 52
    
    print(f"You have {age} weeks left.")
     
life_in_weeks(56)

def greet_with (name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Angela", "Liverpool") 

def calculate_love_score(name1, name2):
    list1 = ['t','r', 'u', 'e']
    list2 = ['l','o', 'v', 'e']
    cuenta = 0
    cuenta2 = 0
    
    for letter in list1:
        cuenta += name1.lower().count(letter)
        cuenta += name2.lower().count(letter)
    for letter in list2:
        cuenta2 += name1.lower().count(letter)
        cuenta2 += name2.lower().count(letter)
       
    print(f"{cuenta}{cuenta2}")
calculate_love_score("Angela Yu", "Jack Bauer") '''

def calculate_love_score(name1, name2):
    word1 = "true"
    word2 = "love"
    cuenta = 0
    cuenta2 = 0
    
    for letter in word1:
        cuenta += name1.lower().count(letter)
        cuenta += name2.lower().count(letter)
    for letter in word2:
        cuenta2 += name1.lower().count(letter)
        cuenta2 += name2.lower().count(letter)
       
    print(f"{cuenta}{cuenta2}")
    
calculate_love_score("Kanye West", "Kim Kardashian") 

'''
def calculate_love_score(name1, name2):

    cuenta = 0
    cuenta2 = 0
    cuenta = sum(name1.count(letter) for letter in "true")
    cuenta = sum(name2.count(letter) for letter in "true")
    cuenta2 = sum(name1.count(letter) for letter in "love")
    cuenta2 = sum(name2.count(letter) for letter in "love")
       
    print(f"{cuenta}{cuenta2}")
calculate_love_score("Kanye West", "Kim Kardashian")'''