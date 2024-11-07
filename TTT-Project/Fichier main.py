
board = [coordinates for coordinates in range(1,10)]
    #cette liste à répéter à chaque début de manche définit / réinitialise la
    # grille, générant 9 "coordinates" vierges

symbol = ['x','o','&','#','★','♥']
    #cette liste établit les différents symboles pouvant être utilisés pour
    # représenter le jeu de chaque joueur

players = [' ', ' ']
    #cette liste énumère et désigne le ou les deux joueurs participants aux
    # différentes manches

TURN = 0
    #cette variable compte le nombre de tours écoulés depuis le début de la
    # manche, permettant d'arrêter celle-ci lorsque les 9 tours sont écoulés

SYMBOL_J1 = ''
SYMBOL_J2 = ''
SCORE_J1 = ''
SCORE_J2 = ''









    #compile et initie l'intégralité des algorythmes composant le jeu,
    # permettant la délimitation de manches
Display_rules(input("Bienvenue au tic-tac-toe ! Voulez-vous visualiser les\
 règles avant de commencer ? (affichage de la grille coordonnée) o/n "))
print("Le premier joueur choisit le symbole qui le représentera pendant la\
 manche,")
print("Ce symbole doit être désigné à partir de la liste qui suit :")
Choose_symbol(0)
print("Le deuxième joueur choisit également son symbole conformément à la\
 liste")
Choose_symbol(1)
print("Le joueur 1 jouera donc avec le symbole :", players[0],\
 "et le joueur 2 :", players[1])
SYMBOL_J1 = players[0]
SYMBOL_J2 = players[1]
Launch_round()



    
