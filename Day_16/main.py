from turtle import Turtle, Screen

timmy = Turtle()
'''
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()'''

timmy.speed(0)
timmy.bgcolor("black")
timmy.color("aqua")
for i in range(170):
    timmy.circle(i-5)
    timmy.left(5)
    
timmy.done()
