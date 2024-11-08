def TRY_coor(player):
    # try l'input du joueur jusqu'à qu'iel inscrive un nombre entier,
    # contenu entre 1 et 10 et dont l'équivalent dans la grille est libre
    from Lists_Board_Players_MATCH import board, players
    while True:
        coordinates = input(f"{players[player]}\
 Quelle case souhaitez-vous jouer ? (1 à 9)\n  ")

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
    # vérifier si le dernier placement de symbole permet de compléter une
    # combinaison victorieuse pour le joueur
    from Lists_Board_Players_MATCH import board, players
    
    # combinaisons horizontales
    if all(players[player] in board[x] for x in (0,3,6)) or\
     all(players[player] in board[x] for x in (1,4,7)) or\
     all(players[player] in board[x] for x in (2,5,8)):
        return True
    
    # combinaisons verticales
    elif all(players[player] in board[x] for x in (0,1,2)) or\
     all(players[player] in board[x] for x in (3,4,5)) or\
     all(players[player] in board[x] for x in (6,7,8)):
        return True
    
    # combinaisons en diagonale
    elif all(players[player] in board[x] for x in (2,4,6)) or\
     all(players[player] in board[x] for x in (0,4,8)):
        return True
    else:
        return False
