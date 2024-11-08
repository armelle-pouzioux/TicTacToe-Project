
def Launch_turn(player):
    from Fichier_Lists import SCORES, MATCH
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
    from Fichier_Lists import players, MATCH, TURN
    import time

    Reset_board()
    TURN[0] = 1
    while TURN[0] <=9 :
        time.sleep(1)
        print(f"{' '*10} MATCH {MATCH[0]}, Tour {TURN[0]}")
        TURN[0] +=1
        Display_board()
        time.sleep(0.5)
        if TURN[0] %2!= 0:
            if Launch_turn(0) == True:
                time.sleep(1)
                return f"{players[0]} Joueur 1 gagne !! Félicitations !!!\
 {players[0]}\n"
            
        else :
            if Launch_turn(1) == True:
                time.sleep(1)
                return f"{players[1]} Joueur 1 gagne !! Félicitations !!!\
 {players[1]}\n"
    
    # lorsque les tours sont écoulés, la boucle devient obsolète et la
    # fonction return sans ajouter de score
    Display_board()
    MATCH[0] +=1
    return f"\nDommage, il faudra rejouer pour trouver un vainqueur !\n"
