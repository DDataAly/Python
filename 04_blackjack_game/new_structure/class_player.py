import re
import status_analyser as analyser

class Player:
    def __init__(self, id, bet, chips_value, hand=None, status='Still playing', current_hand_sum=0):
        self.id=id
        self.bet=bet
        self.chips_value=chips_value
        self.hand=hand if hand is not None else {}
        self.status=status
        self.current_hand_sum=current_hand_sum

    # # Take the top card from the deck (and remove it from the deck) 
    def draw_card(self,d):
        keys=list(d.keys())
        card_key=keys.pop()
        card_value=d[card_key] 
        # Removing the card from the deck
        d.pop(card_key) 
        return(card_key,card_value,d)    
    
    #Testing mode - use it to choose the cards for each player
    # def draw_card(self,d):
    #     keys=list(d.keys())
    #     print(keys)
    #     card_key=keys[int(input ('Please enter the number of the key you want to use: '))-1]
    #     card_value=d[card_key] 
    #     # Removing the card from the deck
    #     d.pop(card_key) 
    #     return(card_key,card_value,d)   

    def show_hand(self):
        print(f'{self.id}\'s cards: {self.hand}')

    def player_choose_first_move(self,deck):
        print(f'\n{self.id} is playing')
        options=['hit', 'stand', 'double down', 'surrender']
        if list(self.hand.values())[0]==list(self.hand.values())[1]:
            options.append('split')
        valid_input = False
        while valid_input==False:    
            player_move=input(f'Please choose one of the following options {options}:  ')
            if player_move.strip().lower() in options:
                valid_input=True
            else:
                print('Unknown command. Please choose one of the available options')
        return(player_move)

    def player_choose_next_move(self,deck):
        options=['hit', 'stand']
        valid_input = False
        while valid_input==False:    
            player_move=input(f'Please choose one of the following options {options}:  ')
            if player_move.strip().lower() in options:
                valid_input=True
            else:
                print('Unknown command. Please choose one of the available options')
        return(player_move)

    def process_the_move(self, player_move,deck):
        if player_move=='hit':
            analyser.hit(self, deck)
            analyser.announce_player_status(self)
        if player_move =='stand':
            analyser.stand(self)
            analyser.announce_player_status(self)
        if player_move=='split':
            pass
        if player_move=='double down':
            pass
        if player_move=='surrender':
            pass
            
    def player_main_game(self,deck):
        player_move=self.player_choose_first_move(deck)
        self.process_the_move(player_move,deck)
        while self.status=='Still playing':
            player_move=self.player_choose_next_move(deck)
            self.process_the_move(player_move,deck)


    
   
#endregion
#region - Creating a subclass dealer
# Doesn't have any extra attributes compared to the parent class, but has it's own methods
class Dealer (Player):
    def __init__(self):
        super().__init__(id=None, bet=None, chips_value=None)

    def player_first_move(self):
        raise AttributeError ('Selected method doesn\'t apply to the dealer')
    
    def player_main_game(self,deck):
        raise AttributeError ('Selected method doesn\'t apply to the dealer')
    
    def player_choose_first_move(self,deck):
        raise AttributeError ('Selected method doesn\'t apply to the dealer')
    
    def player_choose_next_move(self,deck):
        raise AttributeError ('Selected method doesn\'t apply to the dealer')
    
    def player_main_game(self,deck):
        raise AttributeError ('Selected method doesn\'t apply to the dealer')
       
    def show_upper_card(self):
        print(f'\nThis is the dealer\'s upper card: {list(self.hand.items())[1]}\n')  

    def show_hand(self):
        print(f'Dealer\'s cards: {self.hand}')    
    
    def dealer_hole_check (self):
        if sum(list(self.hand.values()))!=21 and list(self.hand.items())[1][1] in [10,11]:
            print('The dealer has checked and he doesn\'t have a blackjack')

    def dealer_main_game(self,deck):
        analyser.calculate_hand_sum(self)
        print(self.current_hand_sum)        
        analyser.calculate_dealer_status(self)
        print(self.status)
        while self.status=='Still playing':
            analyser.hit(self,deck)






    # def dealer_hand_analyser(self):
    #     if self.final_hand_sum<17:
    #         print(f'The dealer took a card. His updated hand is {self.hand}. The hand sum is {self.final_hand_sum}')
    #         pass
    #     elif self.final_hand_sum<=21:
    #         self.status='Standing'
    #         print(f'The dealer took a card. His updated hand is {self.hand}. \nThe dealer\'s hand sum is {self.final_hand_sum} which is equal or over 17. The dealer finished the game. ')
    #     else:
    #         print(f'The dealer took a card. His updated hand is {self.hand}.')
    #         self.final_hand_sum=self.hand_sum_with_ace_check()
    #         print(f'The hand sum is {self.final_hand_sum}.')
    #         if self.final_hand_sum<17:
    #             pass
    #         elif self.final_hand_sum<=21:
    #             self.status='Standing'
    #             print(f'The dealer will stand and calculate the game results.')
    #         else:
    #             self.status='Lost'
    #             print(f'The dealer bust.')
    #     return(self.status, self.final_hand_sum)
    
    # def dealer_main_game(self,deck):
    #     print('\nThe dealer is playing')
    #     print(f'This is the dealer hand: {self.hand}. The hand sum is {self.final_hand_sum}')
    #     print('The dealer has to take cards from the deck until he hits 17 or more')
    #     if self.final_hand_sum>=17:
    #         self.status='Standing'
    #         print(f'The dealer is standing still as he has the required sum in his hand already')
    #     else:
    #         while self.status=='Still playing':
    #             self.add_card_to_hand(deck)
    #             self.status,self.final_hand_sum=self.dealer_hand_analyser()
    #     return(self.status, self.final_hand_sum)


# Body of the program
                                                                                                                                                                                                                                    
# First card distribution
# num_initial_rounds=2
# for round in (1, num_initial_rounds+1):
#     for player in players:
#         player.add_card_to_hand(deck)
#     dealer.add_card_to_hand(deck)

# #Print statement to display initial hands for players and the upcard of the dealer
# for player in players:
#     print(f'This is the hand of the {player.id}: {player.hand}')
# print(f'This is the dealer\'s upper card: {list(dealer.hand.items())[1]}')  
 
