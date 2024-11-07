TURN = 1
    #cette variable compte le nombre de tours écoulés depuis le début de la
    # manche, permettant d'arrêter celle-ci lorsque les 9 tours sont écoulés
MATCH = 1

def TRY_coor(input):
    #try si l'input de coordonnée correspond à une case vide, au quel cas le
    # tour se termine
    print(input)
    pass

from Fichier_main import board
from Functions_board import Reset_board, Display_board
def Launch_match():
    Reset_board()
    while ' ' in board:
        print(f"MANCHE {MATCH}, Tour {TURN}")
        TURN +=1
        MATCH +=1
        Display_board()
        TRY_coor(input("Quelle case souhaitez-vous jouer ? (1 à 9) "))
    pass

