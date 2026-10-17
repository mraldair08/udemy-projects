import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
choosen_word  = random.choice(word_list)
print(choosen_word)

placeholder = ''
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)


game_over = False
correct_letters = []
lives = 6
 
while not game_over:
    print(f"*********************** {lives} / 6 lives left ***********************")
    guess = input("Guess a letter: ").lower()

    display = ""

    if guess in correct_letters:
        print(f"The letter '{guess}' was already use")

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "

    print(display)

    if guess not in choosen_word:
        lives -= 1
        print(f"The letter '{guess}' is not in the choseen word.")

        if guess not in choosen_word:
            if lives == 0:
                game_over = True

                print(f"*********************** The word was '{choosen_word}'    You LOSE! ***********************")

    if "_" not in display:
        game_over = True
        print("*********************** You WIN! ***********************")

    print(display)
    print(stages[lives])
