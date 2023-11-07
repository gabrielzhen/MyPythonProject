from cards import card ##import the model

deck=[]
for suit in range(1,5):
    for rank in range(1,14):
        deck.append(card(suit,rank))
hand=[]
for i in range(0,5):
    a=random.choice(deck)
    hand.append(a)
    deck.remove(a)
