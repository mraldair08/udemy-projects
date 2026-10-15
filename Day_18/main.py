#from turtle import Turtle, Screen
import turtle as t
import random

colors = ['red', 'pink', 'yellow', 'purple', 'grey', 'black', 'coral', 'green', "#FF1493",  # Rosa intenso"#FF4500",  # Naranja rojizo
    "#FFFF00",  # Amarillo eléctrico
    "#00FF00",  # Verde neón
    "#00FFFF",  # Cian eléctrico
    "#0000FF",  # Azul intenso
    "#8A2BE2",  # Violeta
    "#FF00FF",  # Magenta
    "#FF6347",  # Coral
    "#FFA500",  # Naranja
    "#7FFF00",  # Verde chartreuse
    "#FF69B4",  # Rosa chicle
    "#40E0D0",  # Turquesa
    "#9400D3",  # Violeta oscuro
    "#FFFFFF",  # Blanco
    "#000000"]  # Negro

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("coral")
contador = 0

#while contador <= 4:
 #   timmy.forward(150)
  #  timmy.right(90)
   # contador +=1
'''
for i in range(4):
    for i in range(40):
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.forward(50)
        timmy.right(45)

    timmy.penup()
    timmy.left(45)
    timmy.forward(100)

    for i in range(40):
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.forward(50)
        timmy.left(45)

colors = ['red', 'pink', 'yellow', 'purple', 'grey', 'black', 'coral', 'green']
selection = 0
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)
        
for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
    timmy.color(random.choice(colors))
    selection +=1



pixels = random.randrange(20,50)

def forward():
    timmy.forward(pixels)

def right():
    timmy.right(90)

def left():
    timmy.left(90)

def backwards():
    timmy.backward(pixels)

action = [forward, right, left, backwards]
   
    
def random_walk():
    timmy.width(10)
    random.choice(action)()
    timmy.color(random.choice(colors))

is_on = True

while is_on:
    random_walk()''' 
     
# Solucion del curso
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

    
directions = [0, 90, 180, 270]
timmy.width(15)
timmy.speed("fastest")

for _ in range(200):
    timmy.forward(30)
    timmy.color(random_color())
    timmy.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
screen.setup(width=800, height=600)