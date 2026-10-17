import random 
'''
random_integer = random.randint(1, 10)
print(random_integer) 

random_number = random.random() * 10
print(random_number)

random_float = random.uniform(1, 20)
print(random_float) '''

print("Head or Tails Game!")

coin = random.randint(0,1)

if coin == 0:
    print("Head")
else: 
    print("Tails")