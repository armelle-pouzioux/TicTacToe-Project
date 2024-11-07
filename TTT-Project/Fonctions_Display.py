
from Fichier_main import symbol, players, board


def Display_rules(y_n):
    #affiche ou non les règles du jeu, l'assignation des symboles et le
    # système de manches
    if y_n in ('o', 'oui', 'O', 'Oui', 'y', 'yes', 'Y', 'Yes'):
        print()
        Display_board()
        print()
        print("Voici les règles")
        print()
        return
    else :
        print()
        return


def Choose_symbol(player):
    #définit avec un input le choix de symbole réalisé par le joueur puis
    # supprime celui-ci de la liste disponible
    while True:
        print(symbol)
        for x in range(1, symbol.index(symbol[-1])+2):
            print("   ", end='')
            print(x, ",", sep='', end='')
        print()
        choice = input("Faites votre choix avec le numéro correspondant : ")
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
    board[0:9] = [' ' for coordinates in range(1,10)]

def Display_board():
    #imprimer un board de jeu où sont inscrites les coordonnées de jeu qui
    # seront remplacées par les symboles joués
    print(f"| {board[0]} | {board[1]} | {board[2]} |" )
    print("-"*13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |" )
    print("-"*13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |" )