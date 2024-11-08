# FICHIER_MAIN : compile et initie l'intégralité des algorythmes composant le jeu,
#                permettant la délimitation de manches, du compte du score, etc.

# Préambule 1 : import de la fonction permettant l'affichage des règles au
#               choix du joueur
from Function_Display_rules import Display_rules
Display_rules(input("Bienvenue au tic-tac-toe ! Voulez-vous visualiser les\
 règles avant de commencer ?\n   (affichage de la grille des coordonnées)\
 o/n :\n   "))

# Préambule 2 : import de la fonction faisant choisir aux joueurs les symboles
#               avec lesquels ils souhaitent jouer
from Function_Choose_symbol import Choose_symbol
print(f"Le premier joueur choisit le symbole qui le représentera pendant la\
 manche,\nce symbole doit être désigné à partir de la liste qui suit : \n")
Choose_symbol(0)
print("\nLe deuxième joueur choisit également son symbole conformément à la\
 liste\n")
Choose_symbol(1)

# Préambule 3 : import de la liste players['0','1'] recençant les symboles
#               choisis afin de les placer sur la grille de jeu
from Lists_Board_Players_MATCH import players
print("Le joueur 1 jouera donc avec le symbole :", players[0],\
 "et le joueur 2 :", players[1])


from Functions_Rounds import Launch_match
while True:
    from Lists_Board_Players_MATCH import MATCH, SCORES
    print(f"\n Début du match {MATCH[0]} ! \n     Score :\
 {SCORES[0]} {players[0]} - {SCORES[1]} {players[1]}\n")

    print(Launch_match())

    replay = input("Souhaitez-vous rejouer ? o/n :\n   ")
    if replay in ("o","O","oui","Oui","y","Y","yes","Yes"):
        continue

    else:
        from Lists_Board_Players_MATCH import SCORES
        print(f"\nMerci d'avoir joué, à bientôt !\n Scores finaux :\
 {SCORES[0]} {players[0]} - {SCORES[1]} {players[1]}\n")
        break