import random 

basic_keys=['Ace', '2', '3', '4', '5', '6', '7', '8','9', '10', 'King', 'Queen', 'Jack']
suit_values=[1,2,3,4,5,6,7,8,9,10,10,10,10]
suits=['Hearts', 'Clubs', 'Spikes', 'Dimonds']
full_keys=[]
for suit in suits:
    for basic_key in basic_keys:
        full_keys.append(suit+' '+basic_key)
full_values=suit_values*4

d={}
for i in range (0, len(full_keys)):
    d.update({full_keys[i]:full_values[i]})
  

class player():
    pass

def hit():
    i=random.randrange(0, len(d))
    card_key=full_keys[i]
    card_value=d[card_key]
    return(card_key,card_value)

hand={}
hand_keys=list(hand.keys())
hand_values=list(hand.values())
while sum(hand_values)<21:
    top_up_key, top_up_value=hit()
    print(top_up_key, top_up_value)
    hand_keys.append(top_up_key)
    hand_values.append(top_up_value)
print(hand_keys)
print(hand_values)



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

