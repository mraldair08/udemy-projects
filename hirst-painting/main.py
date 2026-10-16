import turtle as t
import random
import colorgram

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.shape("turtle")

colors = colorgram.extract("image.jpg",40)

first_color = colors[0]
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    
    rgb_tuple = (r, g, b)
    rgb_colors.append(rgb_tuple)

def random_colors():
    color = random.choice(rgb_colors)
    return color


t.dot(20, random_colors())
t.penup()
t.fd(50)
t.dot(20, random_colors())
#t.pendown()
#t.dot(20, random_colors()) 
#t.penup()
#t.fd(50)
#t.dot(20, random_colors()) 
#t.right(90)
#t.forward(50)

#t.bgcolor(random_colors())
    
def print_dots(n_dots):
    for _ in range(n_dots):
        t.penup()
        t.dot(20,random_colors())
        t.forward(50)
    new_line(n_dots +1)
    t.dot(20,random_colors())

def new_line(n_dots):
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(n_dots * 50)
    t.setheading(0)
    print(t.position())

for _ in range(5):
    print_dots(9)
    
print(t.position())
print(t.heading())
    


screen = t.Screen()
screen.exitonclick()

#10 x 10 rows dots 20 space 50