def compute_turn():
    global c_hand,deck,up_card,active_suit,active_rank,blocked
    options=[]
    for card in c_hand:
        if card.rank=='8':
            c_hand.remove(card)
            up_card=card
            print('compute played',card.short_name)
            suit_totals=[0,0,0,0]
            for suit in range(1,5):
                for card in c_hand:
                    if card.suit_id==suit:
                        suit_totals[suit-1]+=1
            
            active_suit='Diamonds'
            print('compute change the suit',active_suit)
            return
        else:
            if card.suit==active_suit:
                options.append(card)
            elif card.rank==active_rank:
                opthins.append(card)
    if len(options)>0:
        for card in options:
            if card.value>best_play.value