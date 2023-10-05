from replit import clear
from art import logo

print(logo)

bidding_record = []


def add_bidder_to_auction(name, price):
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["price"] = price
    bidding_record.append(new_bidder)


def find_winner(all_bidders):
    final_price = 0
    winner = ""

    for bidder in all_bidders:
        if (bidder["price"] > final_price):
            final_price = bidder["price"]
            winner = bidder["name"]

    print(f"The winner is {winner} with a bid of ${final_price}")


is_auction_done = False

while (is_auction_done is not True):
    user_name = input("What is your name?: ")
    user_price = float(input("What's your bid? $"))

    add_bidder_to_auction(user_name, user_price)

    new_user = input("Are there any other bidders?: y/n ").lower()

    if (new_user == "n"):
        is_auction_done = True
#Clearing console provides to make blind the auction
    clear()
'''
In a blind bid, if two people give the same price, the winner is usually the person who placed the bid first 1. 
This is because the earlier bid is considered to have priority over the later one.
If two bidders place the same bid, the leader will be the first one to have placed this bid.
'''

find_winner(bidding_record)
