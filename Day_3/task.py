print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age <= 12:
        bill = 5
        print("Child tickets are $5 dollars.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7 dollars")
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 12
        print("Adult tickets are $12 dollars.")

    photo = input("Would you like get a picture? Y / N ")

    if photo == "Y":
        bill += 3
        
    print (f" The price will be: ${bill}")

else:
    print("Sorry you have to be taller before you can ride.")
'''

modulo = 10%3

print(modulo)


print("Even number!")

number = int(input("Ingresa un número para saber si es entero: "))

if number % 2 > 0:
    print(f"{number} es unnumero impar")
else:
    print(f"{number} es un numero par")

    '''