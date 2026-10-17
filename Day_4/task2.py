'''states_of_america = ["Delaware", 'Pensylvania', 'New Jersey']

states_of_america[1] = "PencilVania"

states_of_america.append('Angelaland')

print(states_of_america) 

import random

friends = ['Daniela', 'Angel', 'David']
whoPay = random.randint(0, 2)

print(friends[whoPay])
print(random.choice(friends)) '''
 
import random
rock = '''
 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
 
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

options = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n"))
if player >= 0 and player <= 2:
    print(options[player])
computer = random.randint(0, 2)
print(f"Computer choose: {options[computer]}")

if player >= 3 and player < 0:
   print("You typed an invalid number. You Lose!")
elif player == 0 and computer == 2:
    print("You win!")
elif computer == 0 and player == 2:
    print("You lose!")
elif computer > player:
    print("You lose!")
elif player > computer:
    print("You win!")
elif player == computer:
    print("It;s a draw!")