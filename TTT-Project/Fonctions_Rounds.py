
def TRY_coor(input):
    #try si l'input de coordonnée correspond à une case vide, au quel cas le
    # tour se termine
    print(input)
    pass

from Fichier_main import board
from Functions_board import Reset_board, Display_board
def Launch_turn():
    TURN +=1
    Reset_board()
    Display_board()
    TRY_coor(input("Quelle case souhaitez-vous jouer ? (1 à 9) "))
    pass
