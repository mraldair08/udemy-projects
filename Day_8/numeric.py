text = "The project is $500 dlls."
words = text.split()

just_words = [word for word in words if word.isalpha()]
print(just_words)