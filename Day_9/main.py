import random
should_continue = True
bidders = {}
max_value = 0
items = [
    "Guitar",
    "Laptop",
    "Watch",
    "Painting",
    "Camera",
    "Headphones",
    "Bicycle"
]
random_item = random.choice(items)
print("Welcome to the secret auction program.")
print(f"We are auctioning: {random_item}")

def find_highest_bidder(bidding_dictionary):
    winner = "" 
    max_value = 0    
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > max_value:
            max_value = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${max_value}")
    
while should_continue:
    name = input("What is your name? \n")
    bid = float(input("What's your bid: $"))
    
    bidders[name] = bid
    
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no. \n").lower()
    
    if more_bidders == "no":
        should_continue = False
        find_highest_bidder(bidders)
    elif more_bidders == 'yes':
        print('\n' * 100)
