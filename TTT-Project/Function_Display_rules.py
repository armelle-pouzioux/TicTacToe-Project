
def Display_rules(y_n):
    #affiche ou non les règles du jeu, l'assignation des symboles et le
    # système de manches
    if y_n in ('o', 'oui', 'O', 'Oui', 'y', 'yes', 'Y', 'Yes'):
        print()
        print(f"| 1 | 2 | 3 |" )
        print("-"*13)
        print(f"| 4 | 5 | 6 |" )
        print("-"*13)
        print(f"| 7 | 8 | 9 |" )
        print()
        print("Voici les règles")
        print()
        return
    else :
        print()
        return
