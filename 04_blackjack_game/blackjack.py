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
       
    def blackjack_check(self, hand):
        hand_values=list(hand.values())
        if sum(hand_values)==21: #and len(hand_values)==2:
            self.status='Blackjack'  
        return(self.status)
    
    def hand_sum_with_ace_check(self, hand):
        hand_sum=sum(list(self.hand.values()))
        num_aces= len(re.findall('Ace',''.join(hand.keys())))
        if num_aces==0:
                #print('Since there are no aces, it\'s a bust')
            self.status='Lost'
        else:
            print(f'There is(are) {num_aces} ace(s) in this hand')
            for i in range(0,num_aces):
                hand_sum-=10
                if hand_sum==21:
                    self.status='21 Winner'
                    print('The sum is 21, you\'re a winner!')
                    break
                if hand_sum<21:
                    break
                else:
                    continue
            if hand_sum>21:
                self.status='Lost'
            print(f'This is the ace-adjusted sum of the hand {hand_sum}')
        return(self.status, hand_sum)
    
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
    
    def player_main_game(self,id,hand,status,deck):
        print(f'Player {self.id} is playing')
        print(f'Player hand: {self.hand}')
        while self.status=='Active':
            player_move=input('Please choose your action, hit or stand: ')
            if player_move.strip() =='stand':
                self.status='Standing'
            else:
                self.add_card_to_hand(deck)
                print(self.hand)
                self.status, hand_sum=self.player_hand_analyser(self.hand)
                if self.status=='Lost':
                    print(f'The hand sum is {hand_sum}')
                    print(f'The {self.id} has bust')
        return(self.status)

    def player_hand_analyser(self,hand):
        #hand_values=list(self.hand.values())
        hand_sum=sum(list(self.hand.values()))
        #print(f'The hand sum is {hand_sum}')
        if hand_sum==21:
            print('The sum is 21, you\'re a winner!')
            self.status='21 Winner'
        elif hand_sum<21:
            #print('The sum is less than 21')
            pass
        else:
            self.status, hand_sum=self.hand_sum_with_ace_check(hand)
        return(self.status, hand_sum)
#endregion
#region - Creating a subclass dealer
# Create a subclass Dealer which will have only one instance 
# Doesn't have any extra attributes compared to the parent class
class Dealer (GameParticipants):

    def dealer_hand_analyser(self,hand):
        dhand_sum=sum(list(self.hand.values()))
        print(f'The dealer hand has sum of {dhand_sum}')
        if dhand_sum<17:
            #print("Less than 17 condition")
            pass
        elif dhand_sum<21:
            #print('Less than 21 condition')
            self.status='Standing'
        elif dhand_sum==21:
            #print('21 winner condition')
            self.status='21 Winner'
        else:
            self.status, dhand_sum=self.hand_sum_with_ace_check(hand)
        return(self.status, dhand_sum)
    
    def dealer_hole_check (self, hand):
        if sum(list(hand.values()))!=21 and list(dealer.hand.items())[1][1] in [10,11]:
            #self.status='No blackjack'
            print('The dealer has checked and he doesn\'t have a blackjack')
        #else:
            #print('Passing here')
            #pass         
        #return(self.status)

    def dealer_main_game(self,hand,status,deck):
        print('The dealer is playing')
        print(f'This is the dealer hand: {self.hand}')
        if sum(list(self.hand.values()))>=17:
            self.status='Standing'
            dhand_sum=sum(list(self.hand.values()))
            print('I\'m standing still as I already have 17 in my hand')
        else:
            print('The dealer has to take cards from the deck until he hits 17 or more')
            while self.status=='Active':
                self.add_card_to_hand(deck)
                print(f'The dealer took a card. His updated hand is {self.hand}')
                self.status,dhand_sum=self.dealer_hand_analyser(self.hand)
            #print(self.status)
        return(self.status, dhand_sum)
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
def players_list_update(players, game_over):
    num_of_players=len(players.copy())
    # print(f'Initial number of players is {num_of_players}')
    players=[player for player in players if player.status in ['Active','Standing','21 Winner']]
    num_of_players_updated=len(players)
    # print(f'Current number of players is {num_of_players_updated}')
    if num_of_players_updated==0:
        print('The game is over for all participants')
        game_over=True
    elif num_of_players!=num_of_players_updated:
        print('This is the list of players who continue the game: ')
        for player in players:
            print(player.id, end= ' ')
        print('\n')    
    # else:
        # print('All players continue the game')  
    return(game_over,players)
#endregion
#region - Functions for processing a blackjack

# def dealer_blackjack_results (player, dealer):
#     if player.status == 'Blackjack': 
#         print(f'Both {player.id} and the dealer have a blackjack. {player.id} keeps their bet')
#     else:
#         player.bet=0
#         print(f'{player.id} lost his bet')    

# def player_blackjack_results(player):
#     if player.status=='Blackjack':
#         player.chips_value+=1.5*player.bet
#         print(f'Player {player.id} has a blackjack. He has won {1.5*player.bet} and ended the game.')
#endregion




# Take the top card from the deck (and remove it from the deck) 
def hit(d):
    keys=list(d.keys())
    card_key=keys.pop()
    card_value=d[card_key] 
    # Removing the card from the deck
    d.pop(card_key) 
    return(card_key,card_value,d)

Calculate the game results
def game_results(dealer, players,dhand_sum): 
    print('\nThe game results are: ')
    for player in players:
        player.status, sum_hand = player.player_hand_analyser(player.hand)
        if player.status=='Blackjack' and dealer.status!='Blackjack':
            print(f'{player.id} is a blackjack winner and is paid 3:2 on his bet')
        elif player.status=='Blackjack' and dealer.status=='Blackjack':
            print(f'{player.id} an the dealer both have blackjacks, so {player.id} keeps his bet')
        elif player.status!='Blackjack' and dealer.status=='Blackjack':
            print(f'The dealer has a blackjack and {player.id} doesn\'t. {player.id} lost his bet ')

        #For both players and dealers I need to get the sum_hand returned, not only the status. 

        elif sum_hand<sum(list(dealer.hand.values())):
                player.status='Lost'
                print(f'{player.id} has lost the game')
            elif sum_hand>sum(list(dealer.hand.values())):
                player.status='21 Winner'
                print(f'{player.id} has won the game')
            else:
                print(f'{player.id} has a tie with the dealer')


dealer=Dealer()
players=create_players_list()
game_over=False
# Game set up (cards are shuffled only once in the beginning of the game)
deck=deck_generation(cards_generation()[0], cards_generation()[1])
# Since we use random.shuffle in cards_shuffle we need to make sure that we call cards_shuffle function only once 
# If we do shuffled_deck=deck_generation(cards_shuffle(deck)[0], cards_shuffle(deck)[1]) we call the function twice
# This means that re-shuffling takes place twice, with keys returned at fist iteration and values after the second re-shuffling
shuffled_keys, shuffled_values=cards_shuffle(deck)
deck=deck_generation(shuffled_keys, shuffled_values)
                                                                                                                                                                                                                                                                                               
# First card distribution
num_initial_rounds=2
for round in (1, num_initial_rounds+1):
    for player in players:
        player.add_card_to_hand(deck)
    dealer.add_card_to_hand(deck)

#Print statement to display initial hands for players and the upcard of the dealer
for player in players:
    print(f'This is the hand of the {player.id}: {player.hand}')
print(f'This is the dealer\'s upper card: {list(dealer.hand.items())[1]}')  
# print('\n')  
 
#Blackjack analysing
for player in players:
    player.status=player.blackjack_check(player.hand)
    if player.status=='Blackjack':
        print(f'Player {player.id} has a blackjack and has ended the game. He will be paid at the end of the game')

dealer.status=dealer.blackjack_check(dealer.hand)
dealer.dealer_hole_check(dealer.hand)
if dealer.status=='Blackjack':
    game_over=True 
    print(f'The dealer has checked his second card, and he has a blackjack. Dealer\'s hand is {dealer.hand} ')
    print('The game has ended for all participants')

game_over,players=players_list_update(players,game_over)  

#Main game - goes ahead if the dealer doesn't have a blackjack and there are some participants who don't have a blackjack
if game_over==False:
    print('\nThe main game is starting\n')
    for player in players:
        player.status=player.player_main_game(player.id,player.hand,player.status,deck)
        print('\n')
    game_over,players=players_list_update(players,game_over)  

# If there is at least one player who didn't bust the dealer plays
    if len(players)!=0:
        dealer.status, dhand_sum=dealer.dealer_main_game(dealer.hand,dealer.status,deck)

# Game results calculation
    game_results(dealer, players)




# import random 
# import re
# #region - Creating & shuffling the deck
# # Create a list of cards and their values. The default initial value of Ace is 11
# def cards_generation():
#     basic_keys=['Ace', '2', '3', '4', '5', '6', '7', '8','9', '10', 'King', 'Queen', 'Jack']
#     suit_values=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#     suits=['Hearts', 'Clubs', 'Spikes', 'Diamonds']
#     full_keys=[]
#     for suit in suits:
#         for basic_key in basic_keys:
#             full_keys.append(suit+' '+basic_key)
#     full_values=suit_values*4
#     return(full_keys, full_values)

# def deck_generation(keys, values):
#     d={}
#     for i in range (0, len(keys)):
#         d.update({keys[i]:values[i]})
#     return(d)

# def cards_shuffle(d):
#     keys=list(d.keys())
#     random.shuffle(keys) 
#     values=[]
#     for key in keys:
#         value=d[key]
#         values.append(value)
#     return(keys, values)
# #endregion   
# #region - Creating class for game participants
# # Create a class GameParticipants with the attributes hand (=cards in hand), status (=active if the participant can continue the game)
# # Using custom constructor (__init__) to set up default values for all instances
# class GameParticipants:
#     def __init__(self, hand={}, status='Active'):
#         self.hand=hand
#         self.status=status

#     def add_card_to_hand(self, deck):
#         keys=list(self.hand.keys())
#         values=list(self.hand.values())
#         card_key,card_value,updated_deck=hit(deck)
#         keys.append(card_key)
#         values.append(card_value)
#         self.hand=dict(zip(keys,values))
#         deck=updated_deck 
#         return(self.hand,deck) 
       
#     def blackjack_check(self, hand):
#         hand_values=list(hand.values())
#         if sum(hand_values)==21: #and len(hand_values)==2:
#             self.status='Blackjack'  
#         return(self.status)
    
#     def hand_sum_with_ace_check(self, hand):
#         hand_sum=sum(list(self.hand.values()))
#         num_aces= len(re.findall('Ace',''.join(hand.keys())))
#         if num_aces==0:
#                 #print('Since there are no aces, it\'s a bust')
#             self.status='Lost'
#         else:
#             print(f'There is(are) {num_aces} ace(s) in this hand')
#             for i in range(0,num_aces):
#                 hand_sum-=10
#                 if hand_sum==21:
#                     self.status='21 Winner'
#                     print('The sum is 21, you\'re a winner!')
#                     break
#                 if hand_sum<21:
#                     break
#                 else:
#                     continue
#             if hand_sum>21:
#                 self.status='Lost'
#             print(f'This is the ace-adjusted sum of the hand {hand_sum}')
#         return(self.status, hand_sum)
    
# #endregion
# #region - Creating a subclass players
# # Create a subclass Player with an additional attributes id, bet, chips_value
# # Adding an extra instance variable player_id and use super() to call attributes and method of the parent class
# class Player(GameParticipants):
#     def __init__(self, id, bet, chips_value):
#         self.id=id
#         self.bet=bet
#         self.chips_value=chips_value
#         super().__init__()
    
#     def player_main_game(self,id,hand,status,deck):
#         print(f'Player {self.id} is playing')
#         print(f'Player hand: {self.hand}')
#         while self.status=='Active':
#             player_move=input('Please choose your action, hit or stand: ')
#             if player_move.strip() =='stand':
#                 self.status='Standing'
#             else:
#                 self.add_card_to_hand(deck)
#                 print(self.hand)
#                 self.status, hand_sum=self.player_hand_analyser(self.hand)
#                 if self.status=='Lost':
#                     print(f'The hand sum is {hand_sum}')
#                     print(f'The {self.id} has bust')
#         return(self.status)

#     def player_hand_analyser(self,hand):
#         #hand_values=list(self.hand.values())
#         hand_sum=sum(list(self.hand.values()))
#         #print(f'The hand sum is {hand_sum}')
#         if hand_sum==21:
#             print('The sum is 21, you\'re a winner!')
#             self.status='21 Winner'
#         elif hand_sum<21:
#             #print('The sum is less than 21')
#             pass
#         else:
#             self.status, hand_sum=self.hand_sum_with_ace_check(hand)
#         return(self.status, hand_sum)
# #endregion
# #region - Creating a subclass dealer
# # Create a subclass Dealer which will have only one instance 
# # Doesn't have any extra attributes compared to the parent class
# class Dealer (GameParticipants):

#     def dealer_hand_analyser(self,hand):
#         hand_sum=sum(list(self.hand.values()))
#         print(f'The dealer hand has sum of {hand_sum}')
#         if hand_sum<17:
#             #print("Less than 17 condition")
#             pass
#         elif hand_sum<21:
#             #print('Less than 21 condition')
#             self.status='Standing'
#         elif hand_sum==21:
#             #print('21 winner condition')
#             self.status='21 Winner'
#         else:
#             self.status, hand_sum=self.hand_sum_with_ace_check(hand)
#         return(self.status)
    
#     def dealer_hole_check (self, hand):
#         #print('Hello from the hole function')
#         #print(f'Sum of dealer\'s hand is {sum(list(hand.values()))}')
#         #print(f'And his uppder card value is {list(dealer.hand.items())[1][1]}')
#         if sum(list(hand.values()))!=21 and list(dealer.hand.items())[1][1] in [10,11]:
#             self.status='No blackjack'
#             print('The dealer has checked and he doesn\'t have a blackjack')
#         else:
#             #print('Passing here')
#             pass         
#         return(self.status)

#     def dealer_main_game(self,hand,status,deck):
#         print('The dealer is playing')
#         print(f'This is the dealer hand: {self.hand}')
#         if sum(list(self.hand.values()))>=17:
#             self.status='Standing'
#             print('I\'m standing still as I already have 17 in my hand')
#         else:
#             print('The dealer has to take cards from the deck until he hits 17 or more')
#             while self.status=='Active':
#                 self.add_card_to_hand(deck)
#                 print(f'The dealer took a card. His updated hand is {self.hand}')
#                 self.status=self.dealer_hand_analyser(self.hand)
#             #print(self.status)
#         return(self.status)
# #endregion
# #region - Functions for generating the list of players and removing players who won/lost from it
# # Get the number of players and generate a list with their ids
# def generate_player_ids():
#     n=int(input('Please enter a number of players: '))
#     player_ids = ["player" + str(i+1) for i in range(n)]
#     # print(player_ids)
#     return(player_ids)

# # Create a list of players 
# def create_players_list():
#     players_list=[]
#     for id in generate_player_ids():
#         player=Player(id, chips_value=100, bet=20) #need to change this to reflect various bets and number of chips
#         players_list.append(player)
#     return(players_list)   

# #Remove players who have won or lost from the list of players
# def players_list_update(players, game_over):
#     num_of_players=len(players.copy())
#     # print(f'Initial number of players is {num_of_players}')
#     players=[player for player in players if player.status in ['Active','Standing','21 Winner']]
#     num_of_players_updated=len(players)
#     # print(f'Current number of players is {num_of_players_updated}')
#     if num_of_players_updated==0:
#         print('The game is over for all participants')
#         game_over=True
#     elif num_of_players!=num_of_players_updated:
#         print('This is the list of players who continue the game: ')
#         for player in players:
#             print(player.id, end= ' ')
#     else:
#         print('All players continue the game')
#     print('\n')    
#     return(players)
# #endregion
# #region - Functions for processing a blackjack

# def dealer_blackjack_results (player, dealer):
#     if player.status == 'Blackjack': 
#         print(f'Both {player.id} and the dealer have a blackjack. {player.id} keeps their bet')
#     else:
#         player.bet=0
#         print(f'{player.id} lost his bet')    

# def player_blackjack_results(player):
#     if player.status=='Blackjack':
#         player.chips_value+=1.5*player.bet
#         print(f'Player {player.id} has a blackjack. He has won {1.5*player.bet} and ended the game.')
# #endregion




# # Take the top card from the deck (and remove it from the deck) 
# def hit(d):
#     keys=list(d.keys())
#     card_key=keys.pop()
#     card_value=d[card_key] 
#     # Removing the card from the deck
#     d.pop(card_key) 
#     return(card_key,card_value,d)

# # Calculate the game results
# def game_results(dealer, players): 
#     if dealer.status=='Lost':
#         print(f'Since dealer has bust, the following participants won the game: ')
#         for player in players:
#             print(player.id)
#     else:
#         print(f'Calculating the game results for remaining players')    
#         for player in players:
#             player.status, sum_hand = player.player_hand_analyser(player.hand)
#             if sum_hand<sum(list(dealer.hand.values())):
#                 player.status='Lost'
#                 print(f'{player.id} has lost the game')
#             elif sum_hand>sum(list(dealer.hand.values())):
#                 player.status='21 Winner'
#                 print(f'{player.id} has won the game')
#             else:
#                 print(f'{player.id} has a tie with the dealer')


# dealer=Dealer()
# players=create_players_list()
# game_over=False
# # Game set up (cards are shuffled only once in the beginning of the game)
# deck=deck_generation(cards_generation()[0], cards_generation()[1])
# # Since we use random.shuffle in cards_shuffle we need to make sure that we call cards_shuffle function only once 
# # If we do shuffled_deck=deck_generation(cards_shuffle(deck)[0], cards_shuffle(deck)[1]) we call the function twice
# # This means that re-shuffling takes place twice, with keys returned at fist iteration and values after the second re-shuffling
# shuffled_keys, shuffled_values=cards_shuffle(deck)
# deck=deck_generation(shuffled_keys, shuffled_values)
                                                                                                                                                                                                                                                                                               
# # First card distribution
# num_initial_rounds=2
# for round in (1, num_initial_rounds+1):
#     for player in players:
#         player.add_card_to_hand(deck)
#     dealer.add_card_to_hand(deck)

# #Print statement to display initial hands for players and the upcard of the dealer
# for player in players:
#     print(f'This is the hand of the {player.id}: {player.hand}')
# print(f'This is the dealer\'s upper card: {list(dealer.hand.items())[1]}')    
 
# #Blackjack analysing
# for player in players:
#     player.status=player.blackjack_check(player.hand)
# dealer.status=dealer.blackjack_check(dealer.hand)
# #print(f'Initial dealer status is {dealer.status}')
# dealer.status=dealer.dealer_hole_check(dealer.hand)
# #print(f'Dealer status after holing is {dealer.status}')

# if dealer.status=='Blackjack':
#     print(f'The dealer has checked his second card, and he has a blackjack. Dealer\'s hand is {dealer.hand} ')
#     for player in players:
#         dealer_blackjack_results(player,dealer)
#     game_over=True    
#     print('The game has ended')
# else: 
#     #if dealer.status=='No blackjack':
#         #print('The dealer has checked and he doesn\'t have a blackjack')    
#     for player in players:
#         player_blackjack_results(player)
#     players=players_list_update(players)    

# #Main game - goes ahead if the dealer doesn't have a blackjack
# if dealer.status!='Blackjack':
#     print('The main game is starting\n')
#     for player in players:
#         player.status=player.player_main_game(player.id,player.hand,player.status,deck)
#         print('\n')
#     players=players_list_update(players)  

# # If there is at least one player who didn't bust the dealer plays
#     if len(players)!=0:
#         dealer.status=dealer.dealer_main_game(dealer.hand,dealer.status,deck)

# # Game results calculation
#     game_results(dealer, players)

