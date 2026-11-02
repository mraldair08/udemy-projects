import time
from turtle import Screen, Turtle
from player import Player
from car_manager import Cars
from scoreboard import Scoreboard

screen = Screen()
player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.setup(600, 600)
screen.title("The Turtle Crossing")
screen.tracer(0)

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
counter = 0

while game_is_on:
    time.sleep(0.3)
    screen.update()
    cars.move_cars()
    counter +=1
    if counter == 5:
        cars.create_cars()
        counter = 0
    if player.ycor() > 290:
        player.restart_player()
        scoreboard.increase_score()
    
    cars.check_collision(player)

    
    
    
    
screen.exitonclick()