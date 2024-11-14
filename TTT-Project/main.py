#
# MAIN.PY : compiles every functions and lists to create a functional
#           game of TicTacToe

# Pre-match 1 : importing of the first function to display the rules of the
#               game based on the players' choice
import functions_display, functions_launch; import time
time.sleep(1) ; functions_display.display_rules()

# Pre-match 2 : importing of the function letting players choose which symbol
#               they wish to play with
print(f"Les joueurs choisissent d'abord les symboles qui les représenteront\
 pendant la partie,\nces symboles sont résumés dans cette liste :\n")
functions_launch.launch_choice(0)
print("\nLe deuxième joueur choisit également son symbole :\n")
time.sleep(1.5); functions_launch.launch_choice(1)

# Matches start ! : importing the function returning a playable match loop
#                   which lets players choose weither they want to play again
while True:
    print(f"\n  Début du {functions_display.display_scores()}\n")
    print(functions_launch.launch_match())

    # Half-time 1 : condition with an input to ask players weither to play
    #               again or not, followed with message responses
    time.sleep(2) ; replay = input("Souhaitez-vous rejouer ? o/n :\n   ")
    if replay in ("o","O","oui","Oui","y","Y","yes","Yes"): continue

    # Half-time 2 : if the players don't play again, a message showing the
    #               final scores is printed along with the break command
    else: print(f"\nMerci d'avoir joué, à bientôt !\n\nScores finaux,\
 {functions_display.display_scores()}\n"); time.sleep(3); break