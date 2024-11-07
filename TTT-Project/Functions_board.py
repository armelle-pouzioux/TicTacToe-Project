board = [coordinates for coordinates in range(1,10)]
    #cette liste à répéter à chaque début de manche définit / réinitialise la
    # grille, générant 9 "coordinates" vierges

def Reset_board():
    board[0:9] = [' ' for coordinates in range(1,10)]

def Display_board():
    #imprimer un board de jeu où sont inscrites les coordonnées de jeu qui
    # seront remplacées par les symboles joués
    print(f"| {board[0]} | {board[1]} | {board[2]} |" )
    print("-"*13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |" )
    print("-"*13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |" )