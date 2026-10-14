class User:   #Clase
    
    def __init__(self, user_id, username): #constructor
        self.id = user_id
        self.username = username
        self.followers = 0 #podemos asignar un valor por default
        self.following = 0
        
    def follow(self, user): #Metodo
        user.followers += 1
        self.following += 1
        
    
'''
user_1 = User("001")  #Objeto  
user_1.id = "001" #atributo
user_1.username = "Luis" #atributo
'''
user_1 = User("001", "Luis")# creando el objeto con el constructor
user_2 = User("002", "angela")  # creando el objeto con el constructor

user_1.follow(user_2)   #user1 siguio a user2


print(user_1.followers)   #Para llamar un atributo en especifico ponemos objeto.atributo
print(user_1.following)
print(user_2.followers)   
print(user_2.following)