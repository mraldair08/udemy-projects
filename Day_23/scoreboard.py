from turtle import Turtle
ALIGMENT = 'left'
FONT = ("Courier", 15, "normal")
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-250,265)
        self.color("black")
        self.hideturtle()        
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGMENT, font=FONT)
        
    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align="center", font=FONT)
            
        