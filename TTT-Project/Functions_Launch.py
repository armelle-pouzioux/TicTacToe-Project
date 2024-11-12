
def launch_turn(player):
    # launches the verifying of current player's coordinate of choice
    # to update the board list accurately then launches the verifying of
    # all winning combinations
    from lists_established import scores, match
    from functions_display import display_board
    from functions_verify import verify_coordinate, verify_win_cases

    verify_coordinate(player)
    if verify_win_cases(player) == True:
        display_board()
        scores[player] +=1
        match[0] +=1
        return True

def launch_match():
    # regroup all match-related functions to create a functionning round
    # with inputs and formatted prints 
    from functions_display import reset_board, display_board
    from lists_established import players, match, turn
    import time

    reset_board()
    turn[0] = 1
    while turn[0] <=9 :
        time.sleep(1)
        print(f"{' '*10} MATCH {match[0]}, Tour {turn[0]}")
        turn[0] +=1
        display_board()
        time.sleep(0.5)
        if turn[0] %2== 0:
            if launch_turn(0) == True:
                time.sleep(1)
                return f"{players[0]} Joueur 1 gagne !! Félicitations !!!\
 {players[0]}\n"
            
        else :
            if launch_turn(1) == True:
                time.sleep(1)
                return f"{players[1]} Joueur 1 gagne !! Félicitations !!!\
 {players[1]}\n"
    
    # when 9 turns have ecluded, the while loop become obsolete and the
    # function returns without changing scores
    display_board()
    match[0] +=1
    return f"\nDommage, il faudra rejouer pour trouver un vainqueur !\n"
