from turtle import Screen
from paddle import  r_paddle, l_paddle
from ball import Ball
import time

screen = Screen()
ball = Ball()

screen.setup(800, 600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
    
screen.listen()    
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.tracer(0)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    #Dectec collision with right paddel
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        print("contact")    


screen.exitonclick()