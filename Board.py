from Square import Square

# This is a class that will contain an 8x8 grid of Squares
# It will also check validity of movements and move pieces
class Board:

    #Stores the characters of each of the front row pieces
    frontRowPieces = ['P'] * 8 #Represents 8 pawns

    #Stores the characters of each of the back row pieces
    backRowPieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

    def __init__(self):
        #Creates an empty array to be filled by the following code
        self.board = [None] * 8

        for r in range(0, 8):
            self.board[r] = [None] * 8

        for c in range(0, 8):
            self.board[0][c] = Square('W', Board.backRowPieces[c])

        for c in range(0, 8):
            self.board[1][c] = Square('W', Board.frontRowPieces[c])

        for r in range(2, 6):
            for c in range(0, 8):
                self.board[r][c] = Square('-', '-')

        for c in range(0, 8):
            self.board[6][c] = Square('B', Board.frontRowPieces[c])

        for c in range(0, 8):
            self.board[7][c] = Square('B', Board.backRowPieces[c])

    def print_board(self):
        for r in range(0, 8):
            for c in range(0, 8):
                self.print_square(r, c)
                print(" ", end="")
            print()
            

    def print_square(self, row, col):
        self.board[row][col].print_data()


board = Board()
board.print_board()
        
        
    



