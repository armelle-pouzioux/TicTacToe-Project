from Fonctions_Display import Reset_board, Display_board
from Fichier_main import board


def TRY_coor(input):
    #try si l'input de coordonnée correspond à une case vide, au quel cas le
    # tour se termine
    pass


def Check_win(Symbole):
    #vérifier si le dernier placement de symbole permet de compléter une
    # combinaison victorieuse pour le joueur
    if all(Symbole in board[x] for x in (0,3,6)) or all(Symbole in board[x]\
     for x in (1,4,7)) or all(Symbole in board[x] for x in (2,5,8)):
        return True
    
    elif all(Symbole in board[x] for x in (0,1,2)) or all(Symbole in board[x]\
     for x in (3,4,5)) or all(Symbole in board[x] for x in (6,7,8)):
        return True
    
    elif all(Symbole in board[x] for x in (2,4,6)) or all(Symbole in board[x]\
     for x in (0,4,8)):
        return True
    else:
        return False

def Launch_round():
    TURN +=1
    Reset_board()
    Display_board()
    TRY_coor(input("Quelle case souhaitez-vous jouer ? (1 à 9) "))
    pass