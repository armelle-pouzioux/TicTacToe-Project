
def Launch_turn(player):
    from Lists_Board_Players_MATCH import SCORES, MATCH
    from Functions_Display import Display_board
    from Functions_TRY import TRY_coor, TRY_win

    TRY_coor(player)
    if TRY_win(player) == True:
        Display_board()
        SCORES[player] +=1
        MATCH[0] +=1
        return True

def Launch_match():
    # cette fonction constitue la boucle de jeu enchaînant les tours des deux
    # joueurs jusqu'à atteindre soit une victoire soit un match nul
    from Functions_Display import Reset_board, Display_board
    from Lists_Board_Players_MATCH import players, MATCH, TURN

    Reset_board()
    while TURN[0] <9 :
        TURN[0] +=1
        print(f"{' '*10} MATCH {MATCH[0]}, Tour {TURN[0]}")
        Display_board()

        if TURN[0] %2!= 0:
            if Launch_turn(0) == True:
                return f"{players[0]} Joueur 1 gagne !! Félicitations !!!\
 {players[0]}\n"
            
        else :
            if Launch_turn(1) == True:
                return f"{players[1]} Joueur 1 gagne !! Félicitations !!!\
 {players[1]}\n"
    
    # lorsque les tours sont écoulés, la boucle devient obsolète et la
    # fonction return sans ajouter de score
    Display_board()
    MATCH[0] +=1
    return f"\nDommage, il faudra rejouer pour trouver un vainqueur !\n"
