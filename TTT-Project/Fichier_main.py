board = [coordinates for coordinates in range(1,10)]
    #cette liste à répéter à chaque début de manche définit / réinitialise la
    # grille, générant 9 "coordinates" vierges

TURN = 0
    #cette variable compte le nombre de tours écoulés depuis le début de la
    # manche, permettant d'arrêter celle-ci lorsque les 9 tours sont écoulés

SYMBOL_J1 = ''
SYMBOL_J2 = ''
SCORE_J1 = ''
SCORE_J2 = ''

from Function_Display_rules import Display_rules
    # CODE MAIN
    #compile et initie l'intégralité des algorythmes composant le jeu,
    # permettant la délimitation de manches
Display_rules(input("Bienvenue au tic-tac-toe ! Voulez-vous visualiser les\
 règles avant de commencer ? (affichage de la grille coordonnée) o/n "))
print("Le premier joueur choisit le symbole qui le représentera pendant la\
 manche,")
print("Ce symbole doit être désigné à partir de la liste qui suit :")

from Function_Choose_symbol import Choose_symbol

Choose_symbol(0)
print("Le deuxième joueur choisit également son symbole conformément à la\
 liste")
Choose_symbol(1)
from Function_Choose_symbol import players
print("Le joueur 1 jouera donc avec le symbole :", players[0],\
 "et le joueur 2 :", players[1])
SYMBOL_J1 = players[0]
SYMBOL_J2 = players[1]
print(SYMBOL_J1)
print(SYMBOL_J2)

#from Fonctions_Rounds import Launch_turn, TRY_coor, Check_win
#from Fonctions_Display import Reset_board, Display_board
#Launch_turn()



    
