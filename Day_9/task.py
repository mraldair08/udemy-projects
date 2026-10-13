capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nest list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stutgart", "Berlin"]
}

#print(travel_log["France"][1])

nested_list = ["a", "b", ["c", "d"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "num_times_vsited": 8
        },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart" ],
        "num_times_vsited": 5        
        }
}
print(travel_log["Germany"]["cities_visited"][2]) 


should_continue = True 
bidders = {} 
max_value = 0 
print("Welcome to the secret auction program.")

# while should_continue: 
#     name = input("What is your name? \n") 
#     bid = float(input("What's your bid: $")) 
#     bidders[name] = bid 
    
#     more_bidders = input("Are there any other bidders? Type 'yes' or 'no. \n").lower() 
#     print('\n' * 100) 
#     if more_bidders == "no": 
#         should_continue = False 
#     for name, bid in bidders.items(): 
#         if bid > max_value: 
#             max_value = bid 
#             winner = name 
# print(f"The winner is {winner} with a bid of ${max_value}")