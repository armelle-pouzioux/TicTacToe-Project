
#
# FICHIER_MAIN : compile et initie l'intégralité des algorythmes composant le jeu,
#                permettant la délimitation de manches, du compte du score, etc.


# Préambule 1 : import de la fonction permettant l'affichage des règles au
#               choix du joueur
from Functions_Display import Display_rules
Display_rules(input("\nBienvenue au tic-tac-toe ! Voulez-vous visualiser les\
 règles avant de commencer ?\n   (affichage de la grille des coordonnées)\
 o/n :\n   "))

# Préambule 2 : import de la fonction faisant choisir aux joueurs les symboles
#               avec lesquels ils souhaitent jouer
from Functions_Display import Choose_symbol
print(f"Le premier joueur choisit le symbole qui le représentera pendant la\
 manche,\nce symbole doit être désigné à partir de la liste qui suit : \n")
Choose_symbol(0)
print("\nLe deuxième joueur choisit également son symbole conformément à la\
 liste\n")
Choose_symbol(1)

# Préambule 3 : import de la liste players['0','1'] recençant les symboles
#               choisis afin de les placer sur la grille de jeu
from Lists_Board_Players_MATCH import players
print("\nLe joueur 1 jouera donc avec le symbole :", players[0],\
 "et le joueur 2 :", players[1])


# Début des manches ! : import de la fonction des matchs dans une boucle
#      infinie permettant de relancer la fonction en gardant un compte des
#      scores pour chaque joueur, et sans répéter le préambule
from Functions_Launch import Launch_match
from Functions_Display import Display_scores
while True:
    print(f"\n  Début du {Display_scores()}\n")
    print(Launch_match())

    # Interstice 1 : condition permettant de réinitialiser la boucle et donc
    #              une nouvelle partie grâce à la commande continue
    replay = input("Souhaitez-vous rejouer ? o/n :\n   ")
    if replay in ("o","O","oui","Oui","y","Y","yes","Yes"):
        continue

    # Interstice 2 : en cas de fin de partie, la commande break brise la
    #              boucle et met fin au code, affichant les scores finaux
    else:
        print(f"\nMerci d'avoir joué, à bientôt !\
\n\nScores finaux, {Display_scores()}\n")
        break