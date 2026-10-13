import random
from game_data import data
from art import logo, versus

def random_choice():
    random_number = random.randrange(len(data))
    name = data[random_number]['name']
    description = data[random_number]['description']
    country = data[random_number]['country']
    follower_count = data[random_number]['follower_count']
    compare = f"{name}, is {description}, from {country}"
    return compare, follower_count

def play_game():    
    print(logo)
    score = 0
    is_game_over = False
    option_a, followers_a = random_choice()
    option_b, followers_b = random_choice()
    
    #Asegurar que las opciones sean diferentes antes de iniciar
    # while option_a == option_b:
    #     option_b, followers_b = random_choice()
      
    while not is_game_over:
        
        while option_a == option_b:
            option_b, followers_b = random_choice()
        
        
        print(f"Score {score}")
        print(f"Option A: {option_a}")
        print(versus)
        print(f"Option B: {option_b}")
        
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
                
        if followers_a > followers_b:
            correct_answer = 'a'
        else:
            correct_answer = 'b'
            
        if user_choice == correct_answer:
            score += 1
            print(f"\nYou're right! Current score: {score}.\n")
            
            if correct_answer == 'b':
                option_a = option_b
                followers_a = followers_b
                
            option_b, followers_b = random_choice()
            
        else:
            is_game_over = True
            print(f"Wrong Answer. YOU LOSE! final score: {score}")
           
play_game()

