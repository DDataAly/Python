
def dealer_hole_check(dealer):
    if sum(list(dealer.hand.values()))!=21 and list(dealer.hand.items())[1][1] in [10,11]:
        print('The dealer has checked and he doesn\'t have a blackjack')    

def blackjack_check(self):
    hand_values=list(self.hand.values())
    if sum(hand_values)==21: 
        self.status='Blackjack'
    return(self.status)
    