from turtle import Turtle
import random
class Food(Turtle):   #heredmos de clase turtle
    
    def __init__(self):
        super().__init__()  #Inicializa la herencia y ya se pueden llamar los methodos de Turtle
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("green")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)