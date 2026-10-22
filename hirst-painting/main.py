import turtle as t
import random
import colorgram


screen = t.Screen()
t.colormode(255) #Permite usar colores rgb
t.shape("turtle")
t.penup()
#t.goto(-225, -225) #indica la coordenada donde debe iniciar a pintar
t.speed(5)

colors = colorgram.extract("image.jpg",40)  #extrae los colores de la imagen 40 es el numero de colores que esperamos obtener

first_color = colors[0]
rgb_colors = []

for color in colors:  #recorre la variable colors para obtener todos los colores 
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    
    rgb_tuple = (r, g, b)  #recibe los valores de rgb como una tupla 
    rgb_colors.append(rgb_tuple) #los agrega a una lista

def random_colors():  #Funcion que recorre la lista de colores para obtener un color al azar
    color = random.choice(rgb_colors)
    return color


#t.dot(20, random_colors())
#t.penup()
#t.fd(50)
#t.dot(20, random_colors())

    
def print_dots(n_dots, pixels):
    
    for _ in range(n_dots):
        t.penup()
        t.dot(20,random_colors())
        t.forward(pixels)
    new_line(n_dots, pixels)


def new_line(n_dots, pixels):
    t.setheading(90)
    t.forward(pixels)
    t.setheading(180)
    t.forward(n_dots * pixels)
    t.setheading(0)
    print(t.position())

def center_grid(n_dots, pixels):
    start_position =  (n_dots -1) * pixels / 2 * -1
    t.goto(start_position, start_position)

def grid_size(n_dots, pixels):
    center_grid(n_dots, pixels)
    for _ in range(n_dots):
        print_dots(n_dots, pixels)

grid_size(5, 10)
     

screen = t.Screen()
screen.exitonclick()

#10 x 10 rows dots 20 space 50