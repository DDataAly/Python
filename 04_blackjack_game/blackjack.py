import random 
import re

# Create a list of cards and their values. The default initial value of Ace is 11
def cards_generation():
    basic_keys=['Ace', '2', '3', '4', '5', '6', '7', '8','9', '10', 'King', 'Queen', 'Jack']
    suit_values=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    suits=['Hearts', 'Clubs', 'Spikes', 'Diamonds']
    full_keys=[]
    for suit in suits:
        for basic_key in basic_keys:
            full_keys.append(suit+' '+basic_key)
    full_values=suit_values*4
    return(full_keys, full_values)

def deck_generation(keys, values):
    d={}
    for i in range (0, len(keys)):
        d.update({keys[i]:values[i]})
    return(d)

def cards_shuffle(d):
    keys=list(d.keys())
    random.shuffle(keys) 
    values=[]
    for key in keys:
        value=d[key]
        values.append(value)
    return(keys, values)

    
# Take the top card from the deck (and remove it from the deck) 
def hit(d):
    keys=list(d.keys())
    card_key=keys.pop()
    card_value=d[card_key]
    # Removing the card from the deck
    d.pop(card_key) 
    return(card_key,card_value,d)

# Check if two initially distributed cards form a blackjack
def blackjack_check(hand):
    is_blackjack=False
    for item in hand.keys():
        if re.search('Ace',item)==None:
            continue
        else:
            #print('There is an Ace in the hand. Checking the second card...')
            #print(f'The sum of two cards is equal {sum(hand.values())}')
            if sum(hand.values())==21:
                is_blackjack=True
                #print('Wohoo! This is a blackjack')
                break
    return(is_blackjack)   

# Check whether a player and/or the dealer have a blackjack
def blackjack_winners(pbj, dbj):
    if dbj==False:
        if pbj==False:
            pass
        else:
            player.player_status="Blackjack winner"
    if dbj==True:
            if pbj==True:
                player.player_status="Tie"
            else:
                player.player_status="Looser" 
    return(player.player_status)
      

# Get the number of players and generate a list with their ids
def generate_player_ids():
    n=int(input('Please enter a number of players: '))
    player_ids = ["player" + str(i+1) for i in range(n)]
    # print(player_ids)
    return(player_ids)

# Create a class GameParticipants with the attributes participant_hand,participant_is_blackjack
# Using custom constructor (__init__) to set up default values for all instances
class GameParticipants:
    def __init__(self, hand={}, is_blackjack=False):
        self.hand=hand
        self.is_blackjack=is_blackjack

    def add_card_to_hand(self, deck):
        keys=list(self.hand.keys())
        values=list(self.hand.values())
        card_key,card_value,updated_deck=hit(deck)
        keys.append(card_key)
        values.append(card_value)
        self.hand=dict(zip(keys,values))
        deck=updated_deck 
        return(self.hand,deck)   



# Create a subclass Player with an additional attribute player_id
# Adding an extra instance variable player_id and use super() to call attributes and method of the parent class
class Player(GameParticipants):
    def __init__(self, player_id, player_bet, player_chips_value, player_status='Still playing'):
        self.player_id=player_id
        self.player_bet=player_bet
        self.player_chips_value=player_chips_value
        self.player_status=player_status
        super().__init__()


# Create a subclass Dealer which will have only one instance 
# Doesn't have any extra attributes compared to the parent class
class Dealer (GameParticipants):
    pass

def initial_round_results(player):
    #print(player.player_id, player.player_status)
    if player.player_status == 'Blackjack winner':
        print(f'{player.player_id} has won {1.5*player.player_bet} and finished the game')
        player.player_chips_value+=1.5*player.player_bet
        print(f'{player.player_id} has {player.player_chips_value} of chips now')
    elif player.player_status == 'Tie':
        print(f'{player.player_id} keeps his bet')
    elif player.player_status=='Looser':
        print(f'{player.player_id} lost his bet')    
        player.player_chips_value-=player.player_bet
        print(f'{player.player_id} has {player.player_chips_value} of chips now')
    return(player)

def players_list_update(players):
    num_of_players=len(players.copy())
    players=[player for player in players if player.player_status=='Still playing']
    num_of_players_updated=len(players)
    if num_of_players!=num_of_players_updated:
        print('This is an updated list of players: ')
        for player in players:
            print(player.player_id)
    else:
        print('All players continue the game')
    return(players)

# Create a list of players 
def players_list():
    players_list=[]
    for player_id in generate_player_ids():
        player=Player(player_id, player_chips_value=100, player_bet=20) #need to change this to reflect various bets and number of chips
        players_list.append(player)
    return(players_list)   


dealer=Dealer()
players=players_list()
# Game set up (cards are shuffled only once in the beginning of the game)
deck=deck_generation(cards_generation()[0], cards_generation()[1])
# Since we use random.shuffle in card_shuffle we need to make sure that we call cards_shuffle function only once and return both keys and values
# If we do shuffled_deck=deck_generation(cards_shuffle(deck)[0], cards_shuffle(deck)[1]) we call the function twice
# This means that re-shuffling takes place twice, with keys returned at fist iteration and values after the second re-shuffling
# Naturally keys and card values wouldn't match 
shuffled_keys, shuffled_values=cards_shuffle(deck)
deck=deck_generation(shuffled_keys, shuffled_values)
# print(f'This is the shuffled deck of 52 cards: \n {deck}')


                                                                                                                                                                                                                                                                                                

# First card distribution
num_initial_rounds=2
for round in (1, num_initial_rounds+1):
    for player in players:
        player.add_card_to_hand(deck)
    dealer.add_card_to_hand(deck)

# Blackjack check
for player in players:
    player.is_blackjack=blackjack_check(player.hand)
dealer.is_blackjack=blackjack_check(dealer.hand)

for player in players:
    print(f'This is {player.player_id} hand: {player.hand} {"Wohoo, it\'s a blackjack!" if player.is_blackjack==True else ""}')
# print(f'This is dealer hand: {dealer.hand}')
print(f'This is the dealer\'s upper card: {list(dealer.hand.items())[1]}')
if dealer.is_blackjack==True:
    print(f'The dealer has checked and he has a blackjack. This is the dealer\'s hand: {dealer.hand}')
    print('The game is over for all players. These are the game results: ')
# print(f'These are the cards still in the deck: {deck}')
# print(f'There are {len(deck)} cards left in the deck')

for player in players:
    player.player_status=blackjack_winners(player.is_blackjack,dealer.is_blackjack) 
    initial_round_results(player)

if dealer.is_blackjack==False:
    players=players_list_update(players)

print('''This is the list of available actions:
    Stand - do nothing, pass the turn to the next player
    Hit - take a card
    Double - increase your bet up to 2X
    Split - available only if the player has two cards of the same value
    Surrender - end the game immediately and keep half of the bet''')

for player in players:    
    bust=False
    while not bust:
        next_move=input('Please enter h if you\'d like to hit or s if you prefer to stand: ')
        if next_move=='h':
            player.hand, deck=player.add_card_to_hand(deck)
            print(player.hand)
            bust=True
            print(bust)


    


 

# def bust_checker(hand):
#     hand_keys=list(hand.keys())
#     hand_values=hand.values()
#     print(f'The sum of hand is {sum(hand_values)}')
#     if sum(hand_values)<=21:
#         pass
# all_keys=''+join(list(hand.keys()))
# if len(re.findall)



