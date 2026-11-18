# Si se agrega *args (o cualquier otra palabra) se asigna un numero infinito de variables args dentro de la funcion
def add (*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(8, 9 ,8 , 6))

# Si se agregan dos * ahora nos permite declarar un numero infinito de variables y estas se imprimen como diccionario
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #imprime el valor asignado
    #print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs['multiply']
    print(n )
    
calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        #Si agregamos .get hace que sea opcional llenar los dos campos y devuelve none en el vacio
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        
my_car = Car(make = "Nissan", color="Red")
print(my_car.model)