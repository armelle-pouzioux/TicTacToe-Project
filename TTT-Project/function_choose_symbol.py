symbol = ['x','o','&','#','★','♥']
    #cette liste établit les différents symboles pouvant être utilisés pour
    # représenter le jeu de chaque joueur

def choose_symbol(player):
    #définit avec un input le choix de symbole réalisé par le joueur puis
    # supprime celui-ci de la liste disponible
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
            from lists import players
            players[player] = symbol.pop(choice-1)
            return
        else: 
            print("Insérez un nombre compris dans la sélection : ")
            continue
