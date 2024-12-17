import random 
import re

# Create a deck with 52 cards. The default initial value of Ace is 11
def full_deck():
    basic_keys=['Ace', '2', '3', '4', '5', '6', '7', '8','9', '10', 'King', 'Queen', 'Jack']
    suit_values=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    suits=['Hearts', 'Clubs', 'Spikes', 'Dimonds']
    full_keys=[]
    for suit in suits:
        for basic_key in basic_keys:
            full_keys.append(suit+' '+basic_key)
    full_values=suit_values*4

    d={}
    for i in range (0, len(full_keys)):
        d.update({full_keys[i]:full_values[i]})
    # print(f'This is a full deck {d}.')
    return(d)

# Take a card from the deck (and remove it from the deck)
def hit(d):
    i=random.randrange(0, len(d))
    card_key=list(d.keys())[i]
    card_value=d[card_key]
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
def player_ids():
    n=int(input('Please enter a number of players: '))
    player_ids = ["player" + str(i+1) for i in range(n)]
    print(player_ids)
    return(player_ids)

# Create a class Player with the attributes player_id,player_hand,player_blackjack
class Player:
    def __init__(self, player_id):
        self.player_id=player_id
        self.player_hand={}
        self.player_is_blackjack=False

# Create a list of players 
def players_list():
    player_ids=player_ids()
    players_list=[]
    for player_id in player_ids:
        player=Player(player_id)
        players_list.append(player)
    print(players_list)    


# d=full_deck()
# for player in players_list:
#     card_key, card_value, d= hit(d)
#     player.player_hand 
# print(d)
# card_key2, card_value2, d= hit(d)
# print(d)
# hand ={card_key1:card_value1, card_key2:card_value2}
# print(hand)
# blackjack=blackjack_check(hand)
# print(blackjack)


# d=full_deck()
# for player in players_list:
#     card_key, card_value, d= hit(d)
# print(d)
# card_key2, card_value2, d= hit(d)
# print(d)
# hand ={card_key1:card_value1, card_key2:card_value2}
# print(hand)
# blackjack=blackjack_check(hand)
# print(blackjack)




# d=full_deck()
# for i in range(0,3):
#     card_key, card_value,d=hit(d)
#     print(card_key, card_value)
#     print(f"Updated deck: {d}")









    


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

