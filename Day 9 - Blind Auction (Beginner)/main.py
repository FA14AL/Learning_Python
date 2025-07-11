import art
print(art.logo)

bids = {}
continue_bidding = True
while continue_bidding:

    name = input("What is your name? ")
    price = int(input("What is your bid?: $"))

    bids[name] = price

    more_bid = input("Are there any another bidders? Type 'yes' or 'no'. \n").lower()
    if more_bid == "yes":
        print("\n" * 1000)

    else:
        continue_bidding = False

def find_highest_bidder(bidding_dictionary):
    winner = ''
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

find_highest_bidder(bidding_dictionary=bids)