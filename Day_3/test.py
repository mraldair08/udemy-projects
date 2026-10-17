print("Wlcome to Python Pizza Deliveries!")

size = input("What size do you want?  S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == 'S':
    total = 15
elif size == "M":
    total = 20
else:
    total = 25

if pepperoni == "Y":
    if size == "S":
        total += 2
    elif size == "M" or "L":
        total += 3
else:
    if extra_cheese == "Y":
        total += 1
print(f"You final bill is ${total}")