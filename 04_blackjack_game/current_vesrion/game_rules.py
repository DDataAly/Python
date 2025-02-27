import game_setup as setup
import status_analyser as analyser

class Game:
    def __init__(self, players, dealer, deck, game_over = False):
        self.players = players 
        self.dealer = dealer
        self.game_over = game_over 
        self.deck = deck

    
    def initial_card_distribution(self):
        print('The dealer gives two cards to all players and himself\n')
        num_initial_rounds = 2
        for round in (1, num_initial_rounds + 1):
            for player in self.players:
                analyser.add_card_to_hand(player,self.deck)
            analyser.add_card_to_hand(self.dealer,self.deck)
        for player in self.players:    
            player.show_hand()    
            
        self.dealer.show_upper_card()   
        #For testing - replace the last line with the below
        #self.dealer.show_hand() 
        
    def blackjack_check(self):
        analyser.dealer_hole_card_check (self.dealer)

        for player in self.players:
            analyser.blackjack_check(player)
            if player.status == 'Blackjack':
                print(f'The {player.id} has a blackjack and won the game')
  
        analyser.blackjack_check(self.dealer)
        if self.dealer.status == 'Blackjack':
            self.game_over = True
            print(f'The dealer has a blackjack {self.dealer.hand}. This is the end of the game for all players')

    def check_players_proceed_main_game(self):
        active_players = [player for player in self.players if player.status == 'Still playing']
        if not active_players:
            self.game_over = True
            print('\nThere are no players to proceed to the main game.')
        return(active_players)

    def check_players_not_bust(self):
        active_players = [player for player in self.players if player.status != 'Bust']
        if not active_players:
            self.game_over = True
            print('\nAll players bust. This is the end of the game.')     

    def game_results_blackjack(self):
        print ('\nGame results: \n')
        if self.dealer.status == 'Blackjack':
            for player in self.players:
                if player.status == 'Blackjack':
                    print(f'{player.id} keeps their bet')
                else:
                    print(f'{player.id} lost their bet')
        else:
            for player in self.players:
                print(f'{player.id} is paid 3:2 on their bet')   

    def players_to_play(self):
        active_players = self.check_players_proceed_main_game()
        for player in active_players:
            player.player_main_game(self.deck)
        self.check_players_not_bust()


    def dealer_to_play(self):
        self.dealer.dealer_main_game(self.deck)


    def main_game_results(self):
        print ('\nGame results: \n')
        dealer_status = self.dealer.status
        dealer_hand_sum = self.dealer.current_hand_sum

        for player in self.players:
            player_status = player.status
            player_hand_sum = player.current_hand_sum

            if player_status=='Blackjack':
                print(f'{player.id} is a blackjack winner and is paid 3:2 on his bet')

            elif player_status =='Bust':
                print(f'{player.id} bust. He lost the game and his bet')    

            elif dealer_status =='Bust':
                print(f'The dealer bust and {player.id} didn\'t. {player.id} is a winner and' 
                      'is paid 1:1 on his bet')   
            
            elif player_hand_sum > dealer_hand_sum:
                print(f'{player.id} has more points ({player_hand_sum}) than the dealer({dealer_hand_sum}).'
                      f'{player.id} won the game and is paid 1:1 of his bet')
                
            elif player_hand_sum == dealer_hand_sum:
                print(f'The dealer and the {player.id} has the same points ({player_hand_sum}),'
                      f'so {player.id} keeps his bet ')   
                
            else:
                print(f'{player.id} has fewer points ({player_hand_sum}) than the dealer ({dealer_hand_sum}).'
                     f'{player.id} lost the game and his bet')
             

def game_start():
    current_game = Game([],{},{})
    current_game.deck,current_game.players,current_game.dealer = setup.setup_game()
    print(f'All players are ready to start playing\n ')
    return(current_game)
   
if __name__ == "__main__": 
    current_game = Game([],{},{})
    deck,current_game.players,current_game.dealer = current_game.game_start()
    game_over = current_game.game_over_check()
    print(game_over)
    current_game.initial_card_distribution()
    for player in current_game.players:
        print(player.hand)


