
def launch_choice(current):
    # prints symbol list with a set of numbers dedicated to receive the
    # player's input, therefore modifying their space in the players list
    from settings import symbols, players; import time; print(symbols);
    for x in range(1, symbols.index(symbols[-1])+2):
        print("   ", end=''); print(x, ",", sep='', end='')

    while True:
        choice = input(f"\n\nJoueur {current+1}, faites votre choix avec\
 le numéro correspondant : ")
        try: choice = int(choice)
        except ValueError: print("Insérez un nombre entier désignant \
le symbole choisi : "); continue
        if 0 <= choice-1 <= symbols.index(symbols[-1]):
            players[current] = symbols.pop(choice-1)
            print(f"\nJoueur {current+1}, votre symbole sera {players[current]}")
            time.sleep(1); return
        else: print("Insérez un nombre compris dans la sélection : "); continue


def launch_match():
    # regroup all match-related functions to create a functionning round
    # with inputs and formatted prints 
    import functions_display, functions_verify, settings; import time
    functions_display.reset_board()

    for turn in range(0,9):
        time.sleep(1); print(f"{' '*10} MATCH {settings.match}, Tour {turn+1}")
        functions_display.display_board() ; time.sleep(0.5)
        current = turn %2
        functions_verify.verify_coordinate(current)
        if functions_verify.verify_win(current) == True:
                settings.scores[current] +=1 ; settings.match +=1
                time.sleep(1); functions_display.display_board
                return f"{settings.players[current]}\
 Joueur {current+1} gagne !! Félicitations !!! {settings.players[current]}\n"
    
    # when 9 turns have ecluded, the loop becomes obsolete and the function
    # returns without changing scores
    functions_display.display_board(); settings.match +=1
    return f"\nDommage, il faudra rejouer pour trouver un vainqueur !\n"
