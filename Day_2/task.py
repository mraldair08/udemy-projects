'''name = input("Enter your name: ")
lenght_of_the_name = len(name)

print("Number of letters in your name: " + str(lenght_of_the_name))x


print(3 * 3 / 3 + 3 - 3)

bmi = 84 / 1.65 ** 2

print(int(bmi))

print(int(bmi))

print(round(bmi, 2)) '''

score = 0

#User scores a point

score += 1

print(score)




print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill: $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
persons = int(input("How many people to split the bill? "))

tip_porcentage = tip / 100 
tip = tip_porcentage
total_bill = bill_amount * tip + bill_amount
each_person = total_bill / persons

print(f"Each person should pay: ${round(each_person,3)} ")


