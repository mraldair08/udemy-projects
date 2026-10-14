from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")


contador = 0

#while contador <= 4:
 #   timmy.forward(150)
  #  timmy.right(90)
   # contador +=1



while contador < 100:
    if contador % 2 == 0:
        timmy.penup()
        timmy.forward(50)
        timmy.right(45)
        
    else:
        timmy.pendown()
        timmy.forward(50)
        timmy.right(45)
        timmy.color("red")










screen = Screen()
screen.exitonclick()