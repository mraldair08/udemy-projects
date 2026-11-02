from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        
    def up(self):
        new_y = self.ycor() + 6
        self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - 6
        self.goto(self.xcor(), new_y)
        
    def restart_player(self):
            self.goto(0,-280)
