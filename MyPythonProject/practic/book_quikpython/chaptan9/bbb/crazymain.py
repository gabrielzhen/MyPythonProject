game_done is false
while not game_done:
    blocked==0
    player_trun()
    if len(p_hand)==0:
        game_done=True
        print('player win')
    if not game_done:
        computer_trun()
    if len(c_hand)==0:
        game_done=True
        print('computer win')
    if blocked==2:
        game_done=True
        print('both have blocks game over')