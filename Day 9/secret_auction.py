from art import logo
print(logo)

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

names_and_bids = {}
is_bidding = True

while is_bidding:
    name = input("What is your name?: ")
    while True:
        bid = input("What is your bid?: $")
        try:
            bid_value= float(bid)
            names_and_bids[name] = bid_value
            break
        except ValueError:
            print("Not a valid input. Please type again.")

    new_biders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if new_biders == "no" or new_biders == "n":
        is_bidding = False
        find_highest_bidder(names_and_bids)
    print("\n" * 20)

