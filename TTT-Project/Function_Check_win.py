from Function_Display_rules import board
def Check_win(Symbole):
    #vérifier si le dernier placement de symbole permet de compléter une
    # combinaison victorieuse pour le joueur
    if all(Symbole in board[x] for x in (0,3,6)) or all(Symbole in board[x]\
     for x in (1,4,7)) or all(Symbole in board[x] for x in (2,5,8)):
        return True
    
    elif all(Symbole in board[x] for x in (0,1,2)) or all(Symbole in board[x]\
     for x in (3,4,5)) or all(Symbole in board[x] for x in (6,7,8)):
        return True
    
    elif all(Symbole in board[x] for x in (2,4,6)) or all(Symbole in board[x]\
     for x in (0,4,8)):
        return True
    else:
        return False