from player import player
from board import board

def main():
    b = board(9)
    p= player('white', b)
    p2= player('black', b)
    b.setPieces(b.dimension)

    
    print(b.board1)
    print(b.nbrPawns)
if __name__ == '__main__':
    main()
