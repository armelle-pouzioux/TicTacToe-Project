from Functions_board import board, Display_board
def Display_rules(y_n):
    #affiche ou non les règles du jeu, l'assignation des symboles et le
    # système de manches
    if y_n in ('o', 'oui', 'O', 'Oui', 'y', 'yes', 'Y', 'Yes'):
        print("Chaque joueur choisi son symbole pour la partie.\
 A tour de rôle les joueurs vont placer leur symbole dans la grille de jeu.\
 Le premier à aligner ses trois symboles, horizontalement, verticalement, ou diagonalement, gagne la partie.\
 Si aucun joueur n'aligne ses symboles, c'est match nul et nous t'invitons à rejouer !")
        print()
        Display_board()
        print()
        return
    else :
        print("Bonne chance !")
        return