
def choose_symbol(player):
    # prints symbol list with a set of numbers dedicated to receive the
    # player's input, therefore modifying their space in the players list
    # according to their choice, before erasing it from the symbol list to
    # avoid same choice scenarios
    from lists_established import symbols, players
    import time
    print(symbols)
    for x in range(1, symbols.index(symbols[-1])+2):
        print("   ", end='')
        print(x, ",", sep='', end='')

    while True:
        choice = input(f"\n\nJoueur {player+1}, faites votre choix avec\
 le numéro correspondant : ")
        try:
            choice = int(choice)
        except ValueError:
            print("Insérez un nombre entier désignant le symbole choisi : ")
            continue
        if 0 <= choice-1 <= symbols.index(symbols[-1]):
            players[player] = symbols.pop(choice-1)
            print(f"\nJoueur {player+1}, votre symbole sera {players[player]}")
            time.sleep(1.5)
            return
        else: 
            print("Insérez un nombre compris dans la sélection : ")
            continue
