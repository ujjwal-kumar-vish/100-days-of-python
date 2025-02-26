import random


def draw(remaining_deck, hand):
    '''it takes the remaining deck 
    and the hand served to give a random carc'''
    rand_draw = random.randint(0,len(remaining_deck)-1)
    hand.append(remaining_deck[rand_draw])
    remaining_deck.pop(rand_draw)


def blackJackGame():

    deck = ['ace',2,3,4,5,6,7,8,9,10,10,10,10,'ace',2,3,4,5,6,7,8,9,10,10,10,10,'ace',2,3,4,5,6,7,8,9,10,10,10,10,'ace',2,3,4,5,6,7,8,9,10,10,10,10,]

    dealers_hand = []

    players_hand = []


    print('''
        welcome to the 
          black jack 
            game 
        ''')

    # making the Player's hand 
    first_round = True
    game_on = True
    while game_on == True:
        while first_round == True:
            draw(deck, dealers_hand)
            draw(deck, dealers_hand)

            draw(deck, players_hand)
            first_round = False
        else:
            draw(deck, players_hand)

        print(dealers_hand[0], 'is the first card of dealer')
        print(players_hand)
        #print(dealers_hand)
        #print(deck)

        sum = 0
        for card in players_hand:
            if card == 'ace':
                if sum > 10:
                    sum += 1
                else:
                    sum += 11
            else:
                sum += card

        if sum > 21 :
            print("you loose, its a bust, the sum of the deck is over 21!")
            break

        if input('draw another card ? (y/n) :\n') == 'n':
            game_on = False

    # desiding the dealer's hand
    dealer_sum = 0 
    while dealer_sum <17:
        dealer_sum = 0
        for card in dealers_hand:
            if card == 'ace':
                dealer_sum += 11
            else:
                dealer_sum += card
        if dealer_sum > 16:
            break
        draw(deck, dealers_hand)
        #print(dealer_sum,'   it is the debug')

    if dealer_sum>21 :
        print('you win! The dealer\'s deck is bust ')
    elif dealer_sum<sum and sum < 21:
        print ("you win the round ! ;)")
    elif dealer_sum>sum:
        print("the dealer win ")
        #print(dealers_hand)
    elif dealer_sum == sum:
        print("its a draw / stale mate ")

    print(dealers_hand,f" dealer's sum is {dealer_sum} ")
    
    if input("want to play another round? (y/n)  :\n ") == 'y':
        blackJackGame()


blackJackGame()