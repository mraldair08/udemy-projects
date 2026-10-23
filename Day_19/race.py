from turtle import Turtle, Screen
import random


#tim = Turtle()
screen = Screen()
screen.setup(500, 400)
turtles = []
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race?")
colours = ["red", "orange", "yellow", "green", "blue", "purple", ]

#tim.shape("turtle")
#tim.penup()
#tim.goto(-230, -100)
x = -230
y = -100

for turtle in range(6):
    new_turtle = Turtle()
    turtles.append(new_turtle)

for index,turtle in enumerate(turtles):
    turtle.shape("turtle")
    turtle.penup()
    turtle.color(colours[index])
    turtle.goto(x, y)
    y +=50
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles: 
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
            
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()