from turtle import Screen
from paddle import  r_paddle, l_paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

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
    time.sleep(ball.move_speed)
    screen.tracer(0)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        
    #Dectec collision with right paddel
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    
    #Detect if right paddle misses       
    if ball.xcor() > 380:
        ball.restart_ball()
        scoreboard.increase_score_left()
    
    #Detect if left paddle misses
    if  ball.xcor() < -380:
        ball.restart_ball()
        scoreboard.increase_score_right()

screen.exitonclick()