
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
        print("Chaque joueur choisi son symbole pour la partie.\
              A tour de rôle les joueurs vont placer leur symbole dans la grille de jeu.\
              Le premier à aligner ses trois symboles, horizontalement, verticalement, ou diagonalement, gagne la partie.\
              Si aucun joueur n'aligne ses symboles, c'est match nul et nous t'invitons à rejouer !")
        print()
        return
    else :
        print("Bonne chance !")
        return