symbol = ['x','o','&','#','★','♥']
    #cette liste établit les différents symboles pouvant être utilisés pour
    # représenter le jeu de chaque joueur

board = [' ' for coordinates in range(1,10)]
    #cette liste à répéter à chaque début de manche définit / réinitialise la
    # grille, générant 9 "coordinates" vierges

players = ['','']
    #cette liste permet de référer à l'un ou l'autre signe représentant le
    # joueur 1 ou 2 ([O:1])

SCORES = [0,0]
MATCH = [1]
TURN = [0]
# cette variable compte le nombre de tours écoulés depuis le début de la
# manche, permettant d'arrêter celle-ci lorsque les 9 tours sont écoulés