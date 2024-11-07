
def Reset_board():
    #réinitialise la grille de jeu afin de permettre à une nouvelle mange de
    # prendre place
    from Lists_Board_Players_MATCH import board
    board[0:9] = [' ' for coordinates in range(1,10)]

def Display_board():
    #imprimer un board de jeu où sont inscrites les coordonnées de jeu qui
    # seront remplacées par les symboles joués
    from Lists_Board_Players_MATCH import board
    print(f"| {board[0]} | {board[1]} | {board[2]} |" )
    print("-"*13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |" )
    print("-"*13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |" )
