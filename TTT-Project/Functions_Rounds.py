
def TRY_coor(player):
    #try si l'input de coordonnée correspond à une case vide, au quel cas le
    # tour se termine en remplaçant dans la liste board l'élément à la
    # coordonnée choisie par le symbole du joueur 1 ou 2 ([0:1])
    from Lists_Board_Players_MATCH import board
    while True:
        coordinates = input("Quelle case souhaitez-vous jouer ? (1 à 9) ")
        try:
            coordinates = int(coordinates)
        except ValueError:
            print("Inscrivez le nombre entier correspondant à la case")
            continue

        if (coordinates-1) in range(0, 9) and board[coordinates] != ' ':
            from Lists_Board_Players_MATCH import players
            board[coordinates] = players[player]
            return True
        
        elif board[coordinates] != ' ':
            print("Cette case est déjà occupée ! ")
            continue
        else :
            print("Inscrivez une valeur entre 1 et 9 : ")
            continue

def TRY_win(player):
    #vérifier si le dernier placement de symbole permet de compléter une
    # combinaison victorieuse pour le joueur
    from Lists_Board_Players_MATCH import board, players
    
    if all(players[player] in board[x] for x in (0,3,6)) or all(players[player] in board[x]\
     for x in (1,4,7)) or all(players[player] in board[x] for x in (2,5,8)):
        return True
    
    elif all(players[player] in board[x] for x in (0,1,2)) or all(players[player] in board[x]\
     for x in (3,4,5)) or all(players[player] in board[x] for x in (6,7,8)):
        return True
    
    elif all(players[player] in board[x] for x in (2,4,6)) or all(players[player] in board[x]\
     for x in (0,4,8)):
        return True
    else:
        return False

def Launch_match():
    from Lists_Board_Players_MATCH import board, MATCH, SCORE_J1, SCORE_J2
    from Functions_board import board, Reset_board, Display_board
    TURN = 0
     #cette variable compte le nombre de tours écoulés depuis le début de la
     # manche, permettant d'arrêter celle-ci lorsque les 9 tours sont écoulés

    Reset_board()
    Display_board()

    while TURN <=9 :
        TURN +=1
        print(f"MATCH {MATCH}, Tour {TURN}")
        Display_board()

        if TURN %2!= 0:
            TRY_coor(0)
            if TRY_win(0) == True:
                SCORE_J1 +=1
                MATCH +=1
                return True
            
        else :
            TRY_coor(1)
            if TRY_win(1) == True:
                SCORE_J2 +=1
                MATCH +=1
                return True
    MATCH +=1
    return False
