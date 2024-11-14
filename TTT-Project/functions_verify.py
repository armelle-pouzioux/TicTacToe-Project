def verify_coordinate(current):
    # tries the players' inputs until it stands as an integer, making it
    # comparable with the board's coordinate (from 1 to 9)
    from settings import board, players
    while True:
        coordinate = input(f"Joueur {players[current]},\
 quelle case souhaitez-vous jouer ? (1 à 9)\n  ")
        try: coordinate = int(coordinate)
        except ValueError: print("Inscrivez le nombre entier\
 correspondant à la case : "); continue
        if coordinate < 0 or coordinate > 10:
            print("Inscrivez une valeur entre 1 et 9 : "); continue
        elif board[coordinate-1] != ' ':
            print("Cette case est déjà occupée ! "); continue
        elif (coordinate-1) in range(0, 9) and board[coordinate-1] == ' ':
            board[coordinate-1] = players[current]; return True
        # fail-safe when all conditions are false, which shouldn't happen
        else: print("Erreur inconnue, réessayer : "); continue
        

def verify_win(current):
    # verifies if the board list has any combination of 3 coordinates
    # corresponding to the current's symbol to return true
    from settings import board, players
    # columns combinations
    if all(players[current] in board[coordinate] for coordinate in (0,3,6))\
     or all(players[current] in board[coordinate] for coordinate in (1,4,7))\
     or all(players[current] in board[coordinate] for coordinate in (2,5,8)):
        return True
    # rows combinations
    elif all(players[current] in board[coordinate] for coordinate in (0,1,2))\
     or all(players[current] in board[coordinate] for coordinate in (3,4,5))\
     or all(players[current] in board[coordinate] for coordinate in (6,7,8)):
        return True
    # diagonal combinations
    elif all(players[current] in board[coordinate] for coordinate in (2,4,6))\
     or all(players[current] in board[coordinate] for coordinate in (0,4,8)):
        return True