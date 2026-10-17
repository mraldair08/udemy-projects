print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
turn = input("You're at a cross road. Where do you want to go? (Type Left or Right) ").lower()

if turn == "right":
    print(turn)
    print("Game over")
elif turn == "left":
    print(turn)
    
    lake = input("You've come to a lake. There is an island in the middle  of the lake. Type  wait. To wait for the boat. Type swim to swim across ").lower()
    if lake == "swim":
        print(lake)
        print("Game Over")
    elif lake == "wait":
        print(lake)
        door = input("You arrive to the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Wich color do you choose? ").lower()
        if door =="red" or door == "blue":
            print(door)
            print("Game Over")
        else:
            print(door)
            print("You win!")