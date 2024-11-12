symbols = ['x','o','&','#','★','♥']
    # this list states all available symbols that can be used by players
    # during the games

board = [' ' for coordinate in range(1,10)]
    # this list simply generates 9 blank spaces destined to be switched to
    # what players play during matches

players = [' ',' ']
    # this list shows 2 blank spaces that will be switched to what symbol
    # each player choose to play with

scores = [0,0]
match = [1]
turn = [1]
# these lists made to be counts makes it possible to keep track of basic
# informations between matches