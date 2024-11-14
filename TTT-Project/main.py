#   compile et initie l'intégralité des algorythmes composant le jeu,
#    permettant la délimitation de manches

from function_display_rules import display_rules
display_rules(input("Bienvenue au tic-tac-toe ! Voulez-vous visualiser les\
 règles avant de commencer ?\n   (affichage de la grille des coordonnées) o/n :\n   "))

from function_choose_symbol import choose_symbol
print(f"Le premier joueur choisit le symbole qui le représentera pendant la\
 manche,\nce symbole doit être désigné à partir de la liste qui suit : \n")
choose_symbol(0)
print("\nLe deuxième joueur choisit également son symbole conformément à la\
 liste\n")
choose_symbol(1)

from lists import players
print("Le joueur 1 jouera donc avec le symbole :", players[0],\
 "et le joueur 2 :", players[1])

from functions_rounds import launch_match
while True:
    from lists import MATCH, SCORES
    print(f"\n Début du match {MATCH[0]} ! \n     Score : {SCORES[0]} {players[0]} - {SCORES[1]} {players[1]}\n")
    print(launch_match())
    replay = input("Souhaitez-vous rejouer ? o/n :\n   ")
    if replay in ("o","O","oui","Oui","y","Y","yes","Yes"):
        continue
    else:
        from lists import SCORES
        print(f"\nMerci d'avoir joué, à bientôt !\n Scores finaux : {SCORES[0]} {players[0]} - {SCORES[1]} {players[1]}\n")
        break
