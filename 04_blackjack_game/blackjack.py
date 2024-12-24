import random 
import re
#region - Creating & shuffling the deck
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
#endregion   
#region - Creating class for game participants
# Create a class GameParticipants with the attributes hand (=cards in hand), status (=active if the participant can continue the game)
# Using custom constructor (__init__) to set up default values for all instances
class GameParticipants:
    def __init__(self, hand={}, status='Active'):
        self.hand=hand
        self.status=status

    def add_card_to_hand(self, deck):
        keys=list(self.hand.keys())
        values=list(self.hand.values())
        card_key,card_value,updated_deck=hit(deck)
        keys.append(card_key)
        values.append(card_value)
        self.hand=dict(zip(keys,values))
        deck=updated_deck 
        return(self.hand,deck)   
    
    def blackjack_check(self, hand, status):
        hand_values=list(hand.values())
        if sum(hand_values)==21 and len(hand_values)==2:
            self.status='Blackjack'
        return(self.status)
#endregion
#region - Creating a subclass players
# Create a subclass Player with an additional attributes id, bet, chips_value
# Adding an extra instance variable player_id and use super() to call attributes and method of the parent class
class Player(GameParticipants):
    def __init__(self, id, bet, chips_value):
        self.id=id
        self.bet=bet
        self.chips_value=chips_value
        super().__init__()
    
    def hand_analyser(self,hand,status):
        hand_keys=list(self.hand.keys())
        hand_values=list(self.hand.values())
        if sum(hand_values)==21:
            status='Winner'
        if sum(hand_values)<21:
            pass
        else:
            num_aces= len(re.findall('Ace' in ''.join(hand.keys())))
            if num_aces==0:
                status='Lost'
            else:
                hand_sum=sum(hand_values)
                for i in range(0,num_aces):
                    hand_sum-=10
                    if hand_sum==21:
                        status='Winner'
                    if hand_sum<21:
                        pass
                        break
                    else:
                        continue
        return(status)
#endregion
#region - Creating a subclass dealer
# Create a subclass Dealer which will have only one instance 
# Doesn't have any extra attributes compared to the parent class
class Dealer (GameParticipants):
    pass
#endregion
#region - Functions for generating the list of players and removing players who won/lost from it
# Get the number of players and generate a list with their ids
def generate_player_ids():
    n=int(input('Please enter a number of players: '))
    player_ids = ["player" + str(i+1) for i in range(n)]
    # print(player_ids)
    return(player_ids)

# Create a list of players 
def create_players_list():
    players_list=[]
    for id in generate_player_ids():
        player=Player(id, chips_value=100, bet=20) #need to change this to reflect various bets and number of chips
        players_list.append(player)
    return(players_list)   

#Remove players who have won or lost from the list of players
def players_list_update(players):
    num_of_players=len(players.copy())
    players=[player for player in players if player.status=='Active']
    num_of_players_updated=len(players)
    if num_of_players!=num_of_players_updated:
        print('This is an updated list of players: ')
        for player in players:
            print(player.id)
    else:
        print('All players continue the game')
    return(players)
#endregion
#region - Functions for processing a blackjack

def dealer_blackjack_results (player, dealer):
    if player.status == 'Blackjack': 
        print(f'Both {player.id} and the dealer have a blackjack. {player.id} keeps their bet')
    else:
        player.bet=0
        print(f'{player.id} lost his bet')    

def player_blackjack_results(player):
    if player.status=='Blackjack':
        player.chips_value+=1.5*player.bet
        print(f'Player {player.id} has a blackjack. He has won {1.5*player.bet} and ended the game.')
#endregion




# Take the top card from the deck (and remove it from the deck) 
def hit(d):
    keys=list(d.keys())
    card_key=keys.pop()
    card_value=d[card_key]
    # Removing the card from the deck
    d.pop(card_key) 
    return(card_key,card_value,d)

    


dealer=Dealer()
players=create_players_list()
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

#Print statement to display initial hands for players and  upcard of the dealer
for player in players:
    print(f'This is the hand of the {player.id}: {player.hand}')
print(f'This is the dealer\'s upper card: {list(dealer.hand.items())[1]}')    
 
#Blackjack analysing
for player in players:
    player.status=player.blackjack_check(player.hand, player.status)
dealer.status=dealer.blackjack_check(dealer.hand, dealer.status)

if dealer.status=='Blackjack':
    print(f'The dealer has checked his second card, and he has a blackjack. Dealer hand is {dealer.hand} ')
    for player in players:
        dealer_blackjack_results(player,dealer)
    print('The game has ended')
else:
    for player in players:
        player_blackjack_results(player)
    players_list_update(players)    


        




#region
# Blackjack check
# for player in players:
#     player.is_blackjack=blackjack_check(player.hand)
# dealer.is_blackjack=blackjack_check(dealer.hand)
#endregion

# for player in players:
#     print(f'This is {player.id} hand: {player.hand}') 
#     if player.status=="Blackjack":
#         print(f'{"Wohoo, it\'s a blackjack!"}')
# print(f'This is dealer hand: {dealer.hand}')
# print(f'This is the dealer\'s upper card: {list(dealer.hand.items())[1]}')
# if dealer.status=='Blackjack':
#     print(f'The dealer has checked and he has a blackjack. This is the dealer\'s hand: {dealer.hand}')
#     print('The game is over for all players. These are the game results: ')
# # print(f'These are the cards still in the deck: {deck}')
# # print(f'There are {len(deck)} cards left in the deck')
# initial_round_results(player.status, dealer.status)

# if dealer.is_blackjack==False:
#     players=players_list_update(players)

# print('''This is the list of available actions:
#     Stand - do nothing, pass the turn to the next player
#     Hit - take a card
#     Double - increase your bet up to 2X
#     Split - available only if the player has two cards of the same value
#     Surrender - end the game immediately and keep half of the bet''')

# for player in players:    
#     bust=False
#     while not bust:
#         next_move=input('Please enter h if you\'d like to hit or s if you prefer to stand: ')
#         if next_move=='h':
#             player.hand, deck=player.add_card_to_hand(deck)
#             print(player.hand)
#             bust=True
#             print(bust)


 

# def bust_checker(hand):
#     hand_keys=list(hand.keys())
#     hand_values=list(hand.values())
#     print(f'The sum of hand is {sum(hand_values)}')
#     if sum(hand_values)<=21:
#         pass
#     all_keys=''.join(hand.keys())
#     re.findall('Ace' in all_keys)




# dealer=Dealer()
# players=players_list()
# # Game set up (cards are shuffled only once in the beginning of the game)
# deck=deck_generation(cards_generation()[0], cards_generation()[1])
# # Since we use random.shuffle in card_shuffle we need to make sure that we call cards_shuffle function only once and return both keys and values
# # If we do shuffled_deck=deck_generation(cards_shuffle(deck)[0], cards_shuffle(deck)[1]) we call the function twice
# # This means that re-shuffling takes place twice, with keys returned at fist iteration and values after the second re-shuffling
# # Naturally keys and card values wouldn't match 
# shuffled_keys, shuffled_values=cards_shuffle(deck)
# deck=deck_generation(shuffled_keys, shuffled_values)
# # print(f'This is the shuffled deck of 52 cards: \n {deck}')


                                                                                                                                                                                                                                                                                                

# # First card distribution
# num_initial_rounds=2
# for round in (1, num_initial_rounds+1):
#     for player in players:
#         player.add_card_to_hand(deck)
#     dealer.add_card_to_hand(deck)

# # Blackjack check
# for player in players:
#     player.is_blackjack=blackjack_check(player.hand)
# dealer.is_blackjack=blackjack_check(dealer.hand)

# for player in players:
#     print(f'This is {player.player_id} hand: {player.hand} {"Wohoo, it\'s a blackjack!" if player.is_blackjack==True else ""}')
# # print(f'This is dealer hand: {dealer.hand}')
# print(f'This is the dealer\'s upper card: {list(dealer.hand.items())[1]}')
# if dealer.is_blackjack==True:
#     print(f'The dealer has checked and he has a blackjack. This is the dealer\'s hand: {dealer.hand}')
#     print('The game is over for all players. These are the game results: ')
# # print(f'These are the cards still in the deck: {deck}')
# # print(f'There are {len(deck)} cards left in the deck')

# for player in players:
#     player.player_status=blackjack_winners(player.is_blackjack,dealer.is_blackjack) 
#     initial_round_results(player)

# if dealer.is_blackjack==False:
#     players=players_list_update(players)

# print('''This is the list of available actions:
#     Stand - do nothing, pass the turn to the next player
#     Hit - take a card
#     Double - increase your bet up to 2X
#     Split - available only if the player has two cards of the same value
#     Surrender - end the game immediately and keep half of the bet''')

# for player in players:    
#     bust=False
#     while not bust:
#         next_move=input('Please enter h if you\'d like to hit or s if you prefer to stand: ')
#         if next_move=='h':
#             player.hand, deck=player.add_card_to_hand(deck)
#             print(player.hand)
#             bust=True
#             print(bust)


    
# def hand_analyser(hand):
#     hand_keys=list(hand.keys())
#     hand_values=list(hand.values())
#     if sum(hand_values)==21 and len(hand_values)==2:
#         status='Blackjack'
#     elif sum(hand_values)==21:
#         status='Winner'
#     if sum(hand_values)<21:
#         status ='Still in the game'
#     else:
#         num_aces= len(re.findall('Ace' in ''.join(hand.keys())))
#         if num_aces==0:
#             status='Lost'
#         else:
#             hand_sum=sum(hand_values)
#             for i in range(0,num_aces):
#                 hand_sum-=10
#                 if hand_sum==21:
#                     status='Winner'
#                 if hand_sum<21:
#                     status='Still in the game'
#                     break
#                 else:
#                     continue
#     return(status)



 

# def bust_checker(hand):
#     hand_keys=list(hand.keys())
#     hand_values=list(hand.values())
#     print(f'The sum of hand is {sum(hand_values)}')
#     if sum(hand_values)<=21:
#         pass
#     all_keys=''.join(hand.keys())
#     re.findall('Ace' in all_keys)


