print('what would you like to do')
print('player手牌'变量)
response=raw_input('Type a card to play')
while not valid_play:
    selected_card=None
    while selected_card==None:
        if response.lower()=='draw':
            valid_play=True
            if len(deck)>0:
                card=random.choice(deck)
                p_hand.append(card)
                deck.remove(card)
                print('your drew is',card.short_name)
            else:
                print('no cards can be drew')
                blocked+=1
            return
        else:
            for card in p_hand:
                if response.upper()==card.short_name:
                    selected_card=card
            if selected_card==None:
                response=raw_input('you card is wrong, Type a card to play')
    
    if selected_card.rank=='8':
        valid_play=True
    elif selected_card.suit==active_suit:
        valid_play=True
    elif selected_card.rank==active_rank:
        valid_play=True

    if not valid_play:
        