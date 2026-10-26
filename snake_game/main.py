from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("My Snake Game")
game_is_on = True
squares = []
x = 0
y = 0


for square in range(3):
    new_square = Turtle()
    squares.append(new_square)

for square in squares:
    square.shape("square")
    square.penup()
    square.color("white")
    square.goto(x,y)
    x += -20
    
while game_is_on:
    for square in squares:
        square.forward(20)

screen.exitonclick()
