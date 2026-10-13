import random

def random_number():
    return random.randint(1, 100)
     
def get_lives(number_of_attempts):
    if number_of_attempts == "easy":
        return 10
    elif number_of_attempts == "hard":
        return 5

def compare_number(number, guess):
    if guess > number:
        print("Guess is too high")
        
    elif guess < number:
        print("Guess is too low")
        
def get_user_guess():
    return int(input("Make a guess: "))

def play_game():
    guess_number = random_number()

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    u_lives = get_lives(number_of_attempts=level)
    print(f"You have {u_lives} attempts")

    user_guess = get_user_guess()

    while guess_number != user_guess and u_lives >= 1:
        compare_number(number= guess_number, guess= user_guess)
        u_lives -= 1
        print(f"You have {u_lives} attempts remaining")
        if u_lives >= 1:
            user_guess = int(input("Make another guess: "))
        
        
    if guess_number == user_guess:
        print(f"You Win! The right number is {guess_number}")
    else:
        print(f"You lose! The right number is {guess_number}")
    
    
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
play_game()