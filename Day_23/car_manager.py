from turtle import Turtle
from scoreboard import Scoreboard
import random

COLOURS = ["red", "blue", "yellow", "purple", "orange"]
ALL_CARS = []
scoreboard = Scoreboard()

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLOURS))
        self.shapesize(stretch_wid=1,stretch_len= 3)
        self.penup()
        self.goto(300, random.randint(-297, 297))
        self.x_move = 20
        
    def move(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor()
        self.goto(new_x, new_y)
        
    def create_cars(self):
        cars = Cars()
        ALL_CARS.append(cars)
        
    def move_cars(self):
        for car in ALL_CARS:
            car.move()
            
    def check_collision(self, player):
        for car in ALL_CARS:
            if player.distance(car) < 15:
                scoreboard.game_over()