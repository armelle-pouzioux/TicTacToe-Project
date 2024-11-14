def TRY_coor(player):
    #try si l'input de coordonnée correspond à une case vide, au quel cas le
    # tour se termine en remplaçant dans la liste board l'élément à la
    # coordonnée choisie par le symbole du joueur 1 ou 2 ([0:1])
    from lists import board, players
    while True:
        coordinates = input(f"{players[player]}  Quelle case souhaitez-vous jouer ? (1 à 9)\n  ")
        try:
            coordinates = int(coordinates)
        except ValueError:
            print("Inscrivez le nombre entier correspondant à la case : ")
            continue

        if coordinates < 0 or coordinates > 10:
            print("Inscrivez une valeur entre 1 et 9 : ")
            continue

        elif board[coordinates-1] != ' ':
            print("Cette case est déjà occupée ! ")
            continue

        elif (coordinates-1) in range(0, 9) and board[coordinates-1] == ' ':
            board[coordinates-1] = players[player]
            return True
        
        else :
            print("Erreur inconnue, réessayer : ")
            continue
        

def TRY_win(player):
    #vérifier si le dernier placement de symbole permet de compléter une
    # combinaison victorieuse pour le joueur
    from lists import board, players
    
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

def launch_match():
    #cette fonction constitue la boucle de jeu enchaînant les tours des deux
    # joueurs jusqu'à atteindre soit une victoire soit un match nul
    from functions_board import reset_board, display_board
    from lists import players, MATCH, SCORES
    TURN = 0
      #cette variable compte le nombre de tours écoulés depuis le début de la
      # manche, permettant d'arrêter celle-ci lorsque les 9 tours sont écoulés

    reset_board()
    while TURN <=9 :
        TURN +=1
        print(f"           MATCH {MATCH[0]}, Tour {TURN}")
        display_board()

        if TURN %2!= 0:
            TRY_coor(0)
            if TRY_win(0) == True:
                Display_board
                SCORES[0] +=1
                MATCH[0] +=1
                if TURN <=7:
                    return f"\n{players[0]} Joueur 1 gagne !! Félicitations !!! {players[0]}"
                else : return f"\n{players[0]} Joueur 1 gagne ! {players[0]}"
            
        else :
            TRY_coor(1)
            if TRY_win(1) == True:
                Display_board
                SCORES[1] +=1
                MATCH[0] +=1
                if TURN <=7:
                    return f"\n{players[1]} Joueur 2 gagne !! Félicitations !!! {players[1]}"
                else: return f"\n{players[1]} Joueur 2 gagne !! {players[1]}"
    MATCH[0] +=1
    return f"Dommage, il faudra rejouer pour trouver un vainqueur !"
