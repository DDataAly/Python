import game_rules as rules

print('Welcome to the blackjack table!')
input('Please press Enter to start the game ')
current_game=rules.game_start()
current_game.initial_card_distribution()
current_game.blackjack_check()


# import random 
# import re
# #region - Creating & shuffling the deck
# # Create a list of cards and their values. The default initial value of Ace is 11
# def cards_generation():
#     basic_keys=['Ace', '2', '3', '4', '5', '6', '7', '8','9', '10', 'King', 'Queen', 'Jack']
#     suit_values=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#     suits=['Hearts', 'Clubs', 'Spades', 'Diamonds']
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

# # Take the top card from the deck (and remove it from the deck) 
# def hit(d):
#     keys=list(d.keys())
#     card_key=keys.pop()
#     card_value=d[card_key] 
#     # Removing the card from the deck
#     d.pop(card_key) 
#     return(card_key,card_value,d)

# #endregion   
# #region - Creating class for game participants
# # Create a class GameParticipants with the attributes hand (=cards in hand), status (=active if the participant can continue the game)
# # Using custom constructor (__init__) to set up default values for all instances
# class GameParticipants:
#     def __init__(self, hand={}, status='Active', final_hand_sum=0):
#         self.hand=hand
#         self.status=status
#         self.final_hand_sum=final_hand_sum

#     def add_card_to_hand(self, deck):
#         keys=list(self.hand.keys())
#         values=list(self.hand.values())
#         card_key,card_value,updated_deck=hit(deck)
#         keys.append(card_key)
#         values.append(card_value)
#         self.hand=dict(zip(keys,values))
#         self.final_hand_sum=sum(values)
#         deck=updated_deck 
#         return(self.hand,deck) 
       
#     def blackjack_check(self):
#         hand_values=list(self.hand.values())
#         if sum(hand_values)==21: 
#             self.status='Blackjack'
#         return(self.status)

#     def hand_sum_with_ace_check(self):
#         num_aces= len(re.findall('Ace',''.join(self.hand.keys())))
#         if num_aces:
#             print(f'There is(are) {num_aces} ace(s) in this hand')
#             for i in range(0,num_aces):
#                 self.final_hand_sum-=10
#                 if self.final_hand_sum<=21:
#                     break
#                 else:
#                     continue  
#         return(self.final_hand_sum)
    
# #endregion
# #region - Creating a subclass players
# # Create a subclass Player with an additional attributes and methods
# # Adding an extra instance variables e.g. player_id and use super() to call attributes and method of the parent class
# class Player(GameParticipants):
#     def __init__(self, id, bet, chips_value):
#         self.id=id
#         self.bet=bet
#         self.chips_value=chips_value
#         super().__init__()

#     # Adding extra options (splitting, doubling down and surrendering) available at the first move 
#     # def player_first_move(self):
#     #     options=['hit', 'stand', 'double down', 'surrender']
#     #     if list(player.hand.values())[0]==list(player.hand.values())[1]:
#     #         options.append('split')
#     #     valid_input=False    
#     #     while valid_input==False:    
#     #     player_first_move=input(f'Please choose one of the following options {options}:  ')
#     #     if player_first_move in options:
#     #         valid_input=True
#     #     if player_first_move in ['hit','stand']:
#     #         player_main_game(self,deck) 
#     #     if player_first_move=='double down':
#     #         player_double_down (self)
#     #     if player first_move=='surrender':
#     #         player_surrender(self)
#     #     if player_first_move=='split':
#     #         player_split(self)
#     #     else:
#     #         print("Please enter a valid command")    
           

#     def player_main_game(self,deck):
#         print(f'Player {self.id} is playing')
#         self.status, self.final_hand_sum =self.player_hand_analyser()
#         while self.status=='Active':
#             player_move=input('Please choose your action, hit or stand: ')
#             if player_move.strip().lower() =='stand':
#                 self.final_hand_sum=self.player_hand_analyser()[1]
#                 self.status='Standing'
#                 print(f'The hand sum is {self.final_hand_sum}')
#             elif player_move.strip().lower()=='hit':
#                 self.add_card_to_hand(deck)
#                 self.status, self.final_hand_sum =self.player_hand_analyser()
#             else:
#                 print('Unknown command. Please choose between hit and stand')    
#         return(self.status, self.final_hand_sum)
    
#         def player_first_move(self):
#         options=['hit', 'stand', 'double down', 'surrender']
#         if list(player.hand.values())[0]==list(player.hand.values())[1]:
#             options.append('split')
#         player_first_move=input(f'Please choose one of the following options {options}:  ')
#         if player_first_move in ['hit','stand']:
#             player_main_game(self,deck)    

#     def player_hand_analyser(self):
#         if self.final_hand_sum<21 and self.status!='Standing':
#             print(f'{self.hand}. The hand sum is {self.final_hand_sum}')
#             pass
#         elif self.final_hand_sum==21:
#             print(f'{self.hand}. The sum is 21, you\'re a winner!')
#             self.status='21 Winner'
#         else:
#             self.final_hand_sum=self.hand_sum_with_ace_check()
#             if self.final_hand_sum<21:
#                 print(f'{self.hand}. The hand sum is {self.final_hand_sum}')
#                 pass
#             elif self.final_hand_sum==21:
#                 print(f'{self.hand}. The sum is 21, you\'re a winner!')
#                 self.status='21 Winner'
#             else:
#                 print(f'{self.hand} The sum is {self.final_hand_sum}, which is over 21. It\'s a bust!')
#                 self.status='Lost'
#         return(self.status, self.final_hand_sum)
    
# #endregion
# #region - Creating a subclass dealer
# # Create a subclass Dealer which will have only one instance 
# # Doesn't have any extra attributes compared to the parent class, but has it's own methods
# class Dealer (GameParticipants):

#     def dealer_hole_check (self):
#         if sum(list(self.hand.values()))!=21 and list(self.hand.items())[1][1] in [10,11]:
#             print('The dealer has checked and he doesn\'t have a blackjack')

#     def dealer_hand_analyser(self):
#         if self.final_hand_sum<17:
#             print(f'The dealer took a card. His updated hand is {self.hand}. The hand sum is {self.final_hand_sum}')
#             pass
#         elif self.final_hand_sum<=21:
#             self.status='Standing'
#             print(f'The dealer took a card. His updated hand is {self.hand}. \nThe dealer\'s hand sum is {self.final_hand_sum} which is equal or over 17. The dealer finished the game. ')
#         else:
#             print(f'The dealer took a card. His updated hand is {self.hand}.')
#             self.final_hand_sum=self.hand_sum_with_ace_check()
#             print(f'The hand sum is {self.final_hand_sum}.')
#             if self.final_hand_sum<17:
#                 pass
#             elif self.final_hand_sum<=21:
#                 self.status='Standing'
#                 print(f'The dealer will stand and calculate the game results.')
#             else:
#                 self.status='Lost'
#                 print(f'The dealer bust.')
#         return(self.status, self.final_hand_sum)
    
#     def dealer_main_game(self,deck):
#         print('\nThe dealer is playing')
#         print(f'This is the dealer hand: {self.hand}. The hand sum is {self.final_hand_sum}')
#         print('The dealer has to take cards from the deck until he hits 17 or more')
#         if self.final_hand_sum>=17:
#             self.status='Standing'
#             print(f'The dealer is standing still as he has the required sum in his hand already')
#         else:
#             while self.status=='Active':
#                 self.add_card_to_hand(deck)
#                 self.status,self.final_hand_sum=self.dealer_hand_analyser()
#         return(self.status, self.final_hand_sum)
# #endregion
# #region - Functions for generating the list of players and removing players who won/lost from it
# # Get the number of players and generate a list with their ids
# def generate_player_ids():
#     n=int(input('Please enter a number of players: '))
#     player_ids = ["player" + str(i+1) for i in range(n)]
#     return(player_ids)

# # Create a list of players 
# def create_players_list():
#     players_list=[]
#     for id in generate_player_ids():
#         player=Player(id, chips_value=100, bet=20) #need to change this to reflect various bets and number of chips
#         players_list.append(player)
#     return(players_list)   

# def eligible_players(players, game_over):
#     active_players=[player for player in players if player.status in ['Active','Standing','21 Winner']]
#     if not active_players:
#         game_over=True
#         print('There are no players eligible to continue the game')
#     return(game_over)    
# #endregion

# #Calculate the game results
# def game_results(dealer, players): 
#     print('\nThe game results are: ')
#     for player in players:
#         if player.status=='Blackjack' and dealer.status!='Blackjack':
#             print(f'{player.id}: {player.id} is a blackjack winner and is paid 3:2 on his bet')
#         elif player.status=='Blackjack' and dealer.status=='Blackjack':
#             print(f'{player.id}: {player.id} an the dealer both have blackjacks, so {player.id} keeps his bet')
#         elif player.status!='Blackjack' and dealer.status=='Blackjack':
#             print(f'{player.id}: The dealer has a blackjack and {player.id} doesn\'t. {player.id} lost his bet ')
#         elif player.status =='Lost':
#             print(f'{player.id}: {player.id} bust. He lost the game and his bet')    
#         elif player.status!='Lost' and dealer.status=='Lost':
#             print(f'{player.id}: The dealer bust and {player.id} didn\'t. {player.id} is a winner and is paid 1:1 on his bet')   
#         else:
#             if player.final_hand_sum > dealer.final_hand_sum:
#                 print(f'{player.id}: Player {player.id} has more points ({player.final_hand_sum}) than the dealer({dealer.final_hand_sum}). {player.id} won the game and is paid an equivalent of his bet')
#             elif player.final_hand_sum == dealer.final_hand_sum:
#                 print(f'{player.id}: The dealer and the {player.id} has the same points ({player.final_hand_sum}), so {player.id} keeps his bet ')   
#             else:
#                 print(f'{player.id}: Player {player.id} has fewer points ({player.final_hand_sum}) than the dealer ({dealer.final_hand_sum}). {player.id} lost the game and his bet')


# # Body of the program
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
#     player.status=player.blackjack_check()
#     if player.status=='Blackjack':
#         print(f'Player {player.id} has a blackjack and has ended the game. He will be paid at the end of the game')
# # Checking if there are any players who didn't have a blackjack and therefore can continue with the game        
# game_over = eligible_players(players, game_over)

# dealer.status=dealer.blackjack_check()
# dealer.dealer_hole_check()
# if dealer.status=='Blackjack':
#     game_over=True 
#     print(f'The dealer has checked his second card, and he has a blackjack. Dealer\'s hand is {dealer.hand} ')
#     print('The game has ended for all participants')

# #Main game - goes ahead if the dealer doesn't have a blackjack and there are some participants who don't have a blackjack
# if game_over==False:
#     print('\nThe main game is starting')
#     for player in players: 
#         if player.status=='Blackjack':
#             pass
#         else:
#             print('\n')
#             player.status, player.final_hand_sum=player.player_main_game(deck)

# # Status and hand_sum for each player - useful for debugging            
# # print('\n')       
# # for player in players:
# #     print(f'{player.id}: {player.status}, {player. final_hand_sum}')

# #Checking if there are any players who didn't bust
# game_over = eligible_players(players, game_over)

# if game_over==False:
#     input('\nPlease press enter for the dealer to play: ')
#     dealer.status, dealer.final_hand_sum=dealer.dealer_main_game(deck)
    
# game_results(dealer, players)


