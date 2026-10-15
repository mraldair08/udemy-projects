import turtle as t
import random
import colorgram

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

colors = colorgram.extract("image.jpg",30)

first_color = colors[0]
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    
    rgb_tuple = (r, g, b)
    rgb_colors.append(rgb_tuple)

print(rgb_colors)

t.fd(50)
t.dot(20, "blue") 
t.fd(50)
screen = t.Screen()
screen.exitonclick()