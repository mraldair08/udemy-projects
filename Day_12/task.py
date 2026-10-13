'''Modificar variable fuera de una funcion'''
# enemies = 1 

# def increase_enemies(enemy):
#     print(f"enemies inside function: {enemies}")
#     return enemy + 1
    
# enemies = increase_enemies(enemies)
# print(f"enemies outside function: {enemies}")


#Local Scope
#def drink_potion():
#    posion_strength = 2
#    print(posion_strength)
    
#drink_potion()
#print(posion_strength)

#Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         posion_strength = 2
#         print(player_health)
    
#     drink_potion()
    

# print(player_health)
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# def create_enemy():
#     new_enemy = ""
#     if game_level < 5:
#         new_enemy = enemies[0]
    
    
#     print(new_enemy)

PI = 3.14159

def my_func():
    print(PI)
    
my_func()