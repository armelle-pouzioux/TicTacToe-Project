def reset_board():
    #réinitialise la grille de jeu afin de permettre à une nouvelle mange de
    # prendre place
    from lists import board
    board[0:9] = [' ' for coordinates in range(1,10)]

def display_board():
    #imprimer un board de jeu où sont inscrites les coordonnées de jeu qui
    # seront remplacées par les symboles joués
    from lists import board
    print(f"\n| {board[0]} | {board[1]} | {board[2]} |          | 1 | 2 | 3 |")
    print("-"*13 + " "*10 + "-"*13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |          | 4 | 5 | 6 |")
    print("-"*13 + " "*10 + "-"*13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |          | 7 | 8 | 9 |\n\n")
