
def choose_symbol(player):
    # prints symbol list with a set of numbers dedicated to receive the
    # player's input, therefore modifying their space in the players list
    # according to their choice, before erasing it from the symbol list
    # to avoid same choice scenarios
    from lists_established import symbol, players
    import time
    print(symbol)
    for x in range(1, symbol.index(symbol[-1])+2):
        print("   ", end='')
        print(x, ",", sep='', end='')

    while True:
        choice = input(f"\n\nJoueur {player+1}, faites votre choix avec\
 le numéro correspondant : ")
        try:
            choice = int(choice)
        except ValueError:
            print("Insérez un nombre entier désignant le symbole choisi : ")
            continue
        if 0 <= choice-1 <= symbol.index(symbol[-1]):
            players[player] = symbol.pop(choice-1)
            print(f"\nJoueur {player+1}, votre symbole sera {players[player]}")
            time.sleep(1.5)
            return
        else: 
            print("Insérez un nombre compris dans la sélection : ")
            continue

def reset_board():
    # reset the board list to spaces not to create conflict between matches
    from lists_established import board
    board[0:9] = [' ' for coordinates in range(1,10)]

def display_board():
    # print said gameboard with updated board list to keep players aware of
    # their in-game moves
    from lists_established import board
    print(f"\n| {board[0]} | {board[1]} | {board[2]} |          | 1 | 2 | 3 |")
    print(("+" + "-"*3)*3 + "+" + " "*10 + ("+" + "-"*3)*3 + "+")
    print(f"| {board[3]} | {board[4]} | {board[5]} |          | 4 | 5 | 6 |")
    print(("+" + "-"*3)*3 + "+" + " "*10 + ("+" + "-"*3)*3 + "+")
    print(f"| {board[6]} | {board[7]} | {board[8]} |          | 7 | 8 | 9 |\n")

def display_rules(y_n):
    # receive and reads the player's input about weither printing the rules
    # of the game or jump right into it
    import time
    if y_n in ('o', 'oui', 'O', 'Oui', 'y', 'yes', 'Y', 'Yes'):
        print("\nChaque joueur choisi son symbole pour la partie.\n")
        time.sleep(3)
        print("\nA tour de rôle les joueurs vont placer leur symbole dans la \
grille de jeu.\nLe premier à aligner ses trois symboles horizontalement, \
verticalement,\nou diagonalement, gagne la partie. Si aucun joueur n'aligne \
ses symboles,\nc'est match nul et nous t'invitons à rejouer !\n")
        time.sleep(7)
        display_board()
        print("\nVoici la grille de jeu et sa décomposition.\n")
        time.sleep(3)
        return
    else :
        print("\nBonne chance !\n")
        time.sleep(1.5)
        return

def display_scores():
    from lists_established import scores, match, players
    return f"MATCH {match[0]} : \
{scores[0]} {players[0]} - {scores[1]} {players[1]}"