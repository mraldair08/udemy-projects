import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.title("The Turtle Crossing")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()
    
    #Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 10:
            game_is_on = False
            scoreboard.game_over()
            
    #Detect corssing
    if player.restart_player():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()
            
screen.exitonclick()