import game_rules as rules

print('\nWelcome to the blackjack table!')
input('Please press Enter to start the game ')
current_game = rules.game_start()
current_game.initial_card_distribution()
current_game.blackjack_check()
if current_game.game_over == True:
    current_game.game_results_blackjack()
else:
    current_game.players_to_play()
    if current_game.game_over != True:
        current_game.dealer_to_play()
    current_game.main_game_results()    






