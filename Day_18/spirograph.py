import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()


t.colormode(255)
tim.width(1)
tim.speed("fastest")
tim.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color
'''
def create_circles():
    tim.color(random_color())
    tim.circle(80)
    tim.right(5)
    
for _ in range(200):
    create_circles()
'''

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(10)




screen = t.Screen()
screen.exitonclick()
screen.setup(width=800, height=600)