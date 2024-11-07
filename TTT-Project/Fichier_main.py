
#   compile et initie l'intégralité des algorythmes composant le jeu,
#    permettant la délimitation de manches

from Function_Display_rules import Display_rules
Display_rules(input("Bienvenue au tic-tac-toe ! Voulez-vous visualiser les\
 règles avant de commencer ? (affichage de la grille coordonnée) o/n "))

from Function_Choose_symbol import Choose_symbol
print(f"Le premier joueur choisit le symbole qui le représentera pendant la\
 manche,\nce symbole doit être désigné à partir de la liste qui suit : ")
Choose_symbol(0)
print("\nLe deuxième joueur choisit également son symbole conformément à la\
 liste")
Choose_symbol(1)

from Lists_Board_Players_MATCH import players
print("Le joueur 1 jouera donc avec le symbole :", players[0],\
 "et le joueur 2 :", players[1])

from Functions_Rounds import Launch_match
while True:
    from Lists_Board_Players_MATCH import MATCH, SCORE_J1, SCORE_J2
    print(f"   Début du match {MATCH} ! \nScore : {SCORE_J1} - {SCORE_J2}")
    if Launch_match() == True:
        pass


    


#from Fonctions_Rounds import Launch_turn, TRY_coor, Check_win
#from Fonctions_Display import Reset_board, Display_board
#Launch_turn()