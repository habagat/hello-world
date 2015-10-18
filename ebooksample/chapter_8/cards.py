import random 
 
# function to test if all cards in a list have the same suit
def same_suit(hand): 
    first_card = hand[0] 
    first_card_suit = first_card[1] 
    for card in hand: 
        if card[1] != first_card_suit: 
            return False 
    return True 
 
# construct the deck by matching each value with each suit
values = [1,2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K'] 
suits = ['H', 'D', 'S', 'C'] 
deck = [] 
for value in values: 
    for suit in suits: 
        card = str(value) + suit 
        deck.append(card) 

same_suit_hands = 0
for i in range(1000):
    random.shuffle(deck)
    hand = deck[0:5]
    if same_suit(hand):
        same_suit_hands = same_suit_hands + 1
print(same_suit_hands)
