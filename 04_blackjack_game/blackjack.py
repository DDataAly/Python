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
    is_blackjack='False'
    for item in hand.keys():
        if re.search('Ace',item)==None:
            continue
        else:
            print('There is an Ace in the hand. Checking the second card...')
            print(f'The sum of two cards is equal {sum(hand.values())}')
            if sum(hand.values())==21:
                is_blackjack=True
                print('Wohoo! This is a blackjack')
                break
    return(is_blackjack)           

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

# Create a subclass Player with an additional attribute player_id
# Adding an extra instance variable player_id and use super() to call attributes and method of the parent class
class Player(GameParticipants):
    def __init__(self, player_id):
        self.player_id=player_id
        super().__init__()


# Create a subclass Dealer which will have only one instance 
# Doesn't have any extra attributes compared to the parent class
class Dealer (GameParticipants):
    pass

# Create a list of players 
def players_list():
    players_list=[]
    for player_id in generate_player_ids():
        player=Player(player_id)
        players_list.append(player)
    return(players_list)   


# Game set up (cards are shuffled only once in the beginning of the game)
deck=deck_generation(cards_generation()[0], cards_generation()[1])
print (f'This is the deck of 52 cards:\n {deck}')
print('Let\'s re-shuffle it')
# Since we use random.shuffle in card_shuffle we need to make sure that we call cards_shuffle function only once and return both keys and values
# If we do shuffled_deck=deck_generation(cards_shuffle(deck)[0], cards_shuffle(deck)[1]) we call the function twice
# This means that re-shuffling takes place twice, with keys returned at fist iteration and values after the second re-shuffling
# Naturally keys and card values wouldn't match 
shuffled_keys, shuffled_values=cards_shuffle(deck)
deck=deck_generation(shuffled_keys, shuffled_values)
print(f'This is the shuffled deck of 52 cards: \n {deck}')


dealer=Dealer()
players=players_list()

# First card distribution
num_initial_rounds=2
for round in (1, num_initial_rounds+1):
    for player in players:
        player.add_card_to_hand(deck)
    dealer.add_card_to_hand(deck)
      

for player in players:
    print(f'This is {player.player_id} hand: {player.hand}')
print(f'This is dealer hand: {dealer.hand}')
print(f'These are the cards still in the deck: {deck}')
print(f'There are {len(deck)} cards left in the deck')



   


# hand={}
# hand_keys=list(hand.keys())
# hand_values=list(hand.values())
# while sum(hand_values)<21:
#     print("I took a new card")
#     top_up_key, top_up_value=hit()
#     print(top_up_key, top_up_value)
#     hand_keys.append(top_up_key)
#     hand_values.append(top_up_value)
#     print(f'The current total on hand is {sum(hand_values)}.')
#     hand_total(hand_keys, hand_values)
# print(hand_keys)
# print(hand_values)



# def hand_top_up(hand,hit):
#     card=hit()
#     hand.update(card)
#     print(hand)
#     return(hand)   

# def bust_checker(hand):
#     hand_keys=hand.keys()
#     hand_values=hand.values()
#     print(f'The sum of hand is {sum(hand_values)}')
#     while sum(hand_values)<=21:
#         print('cats')
#         hand_top_up

