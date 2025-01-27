import random 
import class_player

#region - Creating & shuffling the deck
# The default initial value of Ace is 11
def cards_generation():
    basic_keys=['Ace', '2', '3', '4', '5', '6', '7', '8','9', '10', 'King', 'Queen', 'Jack']
    suit_values=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    suits=['Hearts', 'Clubs', 'Spades', 'Diamonds']
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

#region - Creating list of players

def generate_player_ids():
    n=int(input('\nPlease enter a number of players: '))
    player_ids = ["player" + str(i+1) for i in range(n)]
    return(player_ids)

# Create a list of players 
def create_players_list():
    players_list=[]
    for id in generate_player_ids():
        player=class_player.Player(id, chips_value=100, bet=20) #need to change this to reflect various bets and number of chips
        players_list.append(player)
    return(players_list)  

#endregion

#region - Bringing all together
def setup_game():
    deck=deck_generation(cards_generation()[0], cards_generation()[1])
    shuffled_keys, shuffled_values=cards_shuffle(deck)
    deck=deck_generation(shuffled_keys, shuffled_values)
    players=create_players_list()
    dealer=class_player.Dealer()
    return (deck,players,dealer)

if __name__ == "__main__": 
    deck,players,dealer=setup_game()
    print(deck)
    for player in players:
        print (f'This is {player.id}')
    if dealer:
        print('Dealer is here')




