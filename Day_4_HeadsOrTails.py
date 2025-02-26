import random
def coinToss():
    toss = random.randint(0,1)
    if toss == 0:
        print('Heads')
    else:
        print('Tails')
    user = input('Toss again? y/n  ')
    if user == 'y':
        coinToss()

coinToss()