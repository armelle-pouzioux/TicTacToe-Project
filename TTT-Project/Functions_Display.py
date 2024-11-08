
def Choose_symbol(player):
    # définit avec un input le choix de symbole réalisé par le joueur puis
    # supprime celui-ci de la liste disponible
    from Lists_Board_Players_MATCH import symbol, players

    print(symbol)
    for x in range(1, symbol.index(symbol[-1])+2):
        print("   ", end='')
        print(x, ",", sep='', end='')

    while True:
        choice = input("\n\nFaites votre choix avec le numéro correspondant : ")
        try:
            choice = int(choice)
        except ValueError:
            print("Insérez un nombre entier désignant le symbole choisi : ")
            continue
        if 0 <= choice-1 <= symbol.index(symbol[-1]):
            players[player] = symbol.pop(choice-1)
            return
        else: 
            print("Insérez un nombre compris dans la sélection : ")
            continue

def Reset_board():
    # réinitialise la grille de jeu afin de permettre à une nouvelle manche de
    # prendre place
    from Lists_Board_Players_MATCH import board
    board[0:9] = [' ' for coordinates in range(1,10)]

def Display_board():
    # imprimer un board de jeu où sont inscrites les coordonnées de jeu qui
    # seront remplacées par les symboles joués
    from Lists_Board_Players_MATCH import board
    print(f"\n| {board[0]} | {board[1]} | {board[2]} |          | 1 | 2 | 3 |")
    print("-"*13 + " "*10 + "-"*13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |          | 4 | 5 | 6 |")
    print("-"*13 + " "*10 + "-"*13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |          | 7 | 8 | 9 |\n\n")

def Display_rules(y_n):
    # affiche ou non les règles du jeu, l'assignation des symboles et le
    # système de manches
    if y_n in ('o', 'oui', 'O', 'Oui', 'y', 'yes', 'Y', 'Yes'):
        print("\nChaque joueur choisi son symbole pour la partie.\
 A tour de rôle les joueurs vont placer leur symbole dans la grille de jeu.\n\
 Le premier à aligner ses trois symboles, horizontalement, verticalement, ou\
 diagonalement, gagne la partie.\n Si aucun joueur n'aligne ses symboles, c'est\
 match nul et nous t'invitons à rejouer !")
        print()
        Display_board()
        print()
        return
    else :
        print("Bonne chance !")
        return

def Display_scores():
    from Lists_Board_Players_MATCH import SCORES, MATCH, players
    return f"MATCH {MATCH[0]} : \
{SCORES[0]} {players[0]} - {SCORES[1]} {players[1]}"