def reset_board():
    # reset the board list to spaces not to create conflict between matches
    from settings import board
    board[0:9] = [' ' for coordinates in range(1,10)]


def display_board():
    # print said gameboard with updated board list to keep settings.players aware of
    # their in-game moves
    from settings import board
    print(f"\n| {board[0]} | {board[1]} | {board[2]} |          | 1 | 2 | 3 |")
    print(("+" + "-"*3)*3 + "+" + " "*10 + ("+" + "-"*3)*3 + "+")
    print(f"| {board[3]} | {board[4]} | {board[5]} |          | 4 | 5 | 6 |")
    print(("+" + "-"*3)*3 + "+" + " "*10 + ("+" + "-"*3)*3 + "+")
    print(f"| {board[6]} | {board[7]} | {board[8]} |          | 7 | 8 | 9 |\n")


def display_scores():
    # returns a formated text displaying basic informations for the players
    import settings ; return f"MATCH {settings.match} : {settings.scores[0]} \
 {settings.players[0]} - {settings.scores[1]} {settings.players[1]}"


def display_rules():
    # receive and reads the player's input about weither printing the rules
    # of the game or jump right into it
    import time
    response = input("\nBienvenue au tic-tac-toe ! Voulez-vous visualiser les\
 règles avant de commencer ?\n  (affichage de la grille des coordonnées)\
 o/n :\n   ")

    if response in ('o', 'oui', 'O', 'Oui', 'y', 'yes', 'Y', 'Yes'):
        print("\nChaque joueur choisit son symbole pour la partie.\n")
        time.sleep(2.5)
        print("\nA tour de rôle les joueurs vont placer leur symbole dans la \
grille de jeu.\nLe premier à aligner ses trois symboles horizontalement, \
verticalement,\nou diagonalement, gagne la partie. Si aucun joueur n'aligne \
ses symboles,\nc'est match nul et nous t'invitons à rejouer !\n")
        time.sleep(7) ; display_board()
        print("\nVoici la grille de jeu et ses 9 cases.\n") ; time.sleep(3)
    else :
        print("\nBonne chance !\n") ; time.sleep(1.5)