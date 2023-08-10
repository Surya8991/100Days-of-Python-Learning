from replit import clear
from art import logo
# HINT: You can call clear() to clear the output in the console.
print(logo)
bids_collector = {}


def auction_house(customer_name, bidder_amount):
    new_bid = {"name": customer_name, "bid_amount": bidder_amount}
    bids_collector[customer_name] = bidder_amount


auction_over = False
while not auction_over:
    name = input("Enter Your Name \n")
    bid = int(input("Enter your bid amount \n"))
    auction_house(name, bid)
    another_bid = input(
        "Do u like to enter another bid type 'yes' or 'no' \n ")
    if another_bid == "yes":
        clear()
    elif another_bid == "no":
        auction_over = True

highest_bid = 0
highest_bidder = ""

for name, bid_amount in bids_collector.items():
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = name

print(f"The Highest bidder is {name} and their bid is {highest_bid}")
