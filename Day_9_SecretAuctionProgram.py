from replit import clear

Bids = {}
people_want_to_bid = True

while people_want_to_bid:
    name = input("what is your name? : ")
    bidAmount = int(input("what's your bid?: $"))
    Bids[name] = bidAmount
    x = input("is there anyone else who want to bid? \n (yes/no) ")
    if x == 'no':
        people_want_to_bid = False
    else: #if there are more people
        clear()

maxBid = 0
maxBider = ''

for bider in Bids:
    if Bids[bider]> maxBid:
        maxBid = Bids[bider]
        maxBider = bider
        
clear()
print(f" {maxBider} is the winner with amount {maxBid} ")