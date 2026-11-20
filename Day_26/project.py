import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper() 

    try:
        phonetic_word = [phonetic_dict[letter] for letter in word]
    except KeyError as error_message:
        print(f"{error_message} is not a letter")
        generate_phonetic()
    else:
        print(phonetic_word)


generate_phonetic()