# #File not found

try:
    file = open("file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["valor"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Test")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise  KeyError

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human should not be over 3 meters.")

