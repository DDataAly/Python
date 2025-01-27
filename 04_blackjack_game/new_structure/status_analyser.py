import re 

def add_card_to_hand(player, deck):
    card_key,card_value,deck=player.draw_card(deck)
    player.hand[card_key]=card_value
    player.current_hand_sum=sum(player.hand.values())
    return(player.hand,deck) 

def dealer_hole_check(dealer):
    if sum(list(dealer.hand.values()))!=21 and list(dealer.hand.items())[1][1] in [10,11]:
        print('The dealer has checked and he doesn\'t have a blackjack')    

def blackjack_check(player):
    hand_values=list(player.hand.values())
    if sum(hand_values)==21: 
        player.status='Blackjack'
    return(player.status)

def calculate_hand_sum(player):
    total_sum=sum(list(player.hand.values()))
    if total_sum>21:
        num_aces= len(re.findall('Ace',''.join(player.hand.keys())))
        if num_aces:
            print(f'There is(are) {num_aces} ace(s) in this hand')
            for i in range(0,num_aces):
                total_sum-=10
                if total_sum<=21:
                    break
                else:
                    continue  
    player.current_hand_sum =total_sum
    #return(total_sum)


def calculate_player_status(player):
    if player.current_hand_sum>21:
        player.status='Bust'
    elif player.current_hand_sum==21:
        player.status='21 winner'
    else:
        pass    

def hit(player,deck):
    add_card_to_hand(player,deck)
    print(player.hand)
    calculate_hand_sum(player)   
    calculate_player_status(player)
    print(f'New sum of the hand is {player.current_hand_sum}')
    # if player.status=='Bust':
    #     print(f'The sum of cards at hand is {player.current_hand_sum} which is more than 22. It\'s a bust')
    # if player.status=='21 winner':
    #     print(f'{player.id} is a 21 winner!')    

def stand(player):
    calculate_hand_sum(player)
    player.status='Standing' 
    #print(f'{player.id} chose to stand')  

def announce_player_status(player):
    if player.status=='Standing':
        print(f'{player.id} chose to stand') 
    elif player.status=='Bust':
        print(f'The sum of cards at hand is {player.current_hand_sum} which is more than 22. It\'s a bust')
    elif player.status=='21 winner':
        print(f'{player.id} is a 21 winner!')
    else:
        pass     

def calculate_dealer_status(dealer):
    if dealer.current_hand_sum>=17:
        dealer.status='Standing'
    else:
        pass    

if __name__ == "__main__": 
    import game_setup
    deck,players,dealer=game_setup.setup_game()
    for player in players:
        player.hand={'Clubs 8': 8, 'Spades 8': 6}
        print(player.hand)
        calculate_hand_sum(player)
        calculate_player_status(player)
        print(player.current_hand_sum)
        stand(player)
