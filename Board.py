from Square import Square

# This is a class that will contain an 8x8 grid of Squares
# It will also check validity of movements and move pieces
class Board:

    #Stores the characters of each of the front row pieces
    frontRowPieces = tuple('P') * 8 #Represents 8 pawns

    #Stores the characters of each of the back row pieces
    backRowPieces = ('R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R')

    def __init__(self):
        #Creates an empty array to be filled by the following code
        self.board = [None] * 8

        for r in range(0, 8):
            self.board[r] = [None] * 8

        for c in range(0, 8):
            self.board[0][c] = Square('B', Board.backRowPieces[c])

        for c in range(0, 8):
            self.board[1][c] = Square('B', Board.frontRowPieces[c])

        for r in range(2, 6):
            for c in range(0, 8):
                self.board[r][c] = Square('-', '-')

        for c in range(0, 8):
            self.board[6][c] = Square('W', Board.frontRowPieces[c])

        for c in range(0, 8):
            self.board[7][c] = Square('W', Board.backRowPieces[c])

    def print_board(self):
        for r in range(0, 8):
            for c in range(0, 8):
                self.print_square(r, c)
                print(" ", end="")
            print()
            

    def print_square(self, row, col):
        self.board[row][col].print_data()

    #Doesn't need self because all board dimensions are the same
    def is_valid_board_position(row, col):
        return row >= 0 and col >= 0 and row < 8 and col < 8

    def is_valid_move(self, old_row, old_col, new_row, new_col):
        old_square = self.board[old_row][old_col]
        piece = old_square.get_piece()

        #If this is a pawn
        if piece == 'P':
            player = old_square.get_color()
            
            if player == 'W':
                #First move for a pawn allows for 2-space movement
                if old_row == 6 and old_row - 2 == new_row and old_col == new_col:
                    return (self.board[old_row - 1][old_col].is_empty()
                    and self.board[new_row][new_col].is_empty())
                #Checks for the normal 1-space-forward move
                if old_row - 1 == new_row and old_col == new_col:
                    return self.board[new_row][new_col].is_empty()
                #Checks for a diagonal capture
                if (old_row - 1 == new_row and
                (old_col - 1 == new_col or old_col + 1 == new_col)):
                    return not self.board[new_row][new_col].is_empty()
                #Otherwise, not valid pawn move
                return False

            else:
                #First move for a pawn allows for 2-space movement
                if old_row == 1 and old_row + 2 == new_row and old_col == new_col:
                    return (self.board[old_row + 1][old_col].is_empty()
                    and self.board[new_row][new_col].is_empty())
                #Checks for the normal 1-space-forward move
                if old_row + 1 == new_row and old_col == new_col:
                    return self.board[new_row][new_col].is_empty()
                #Checks for a diagonal capture
                if (old_row + 1 == new_row and
                (old_col - 1 == new_col or old_col + 1 == new_col)):
                    return not self.board[new_row][new_col].is_empty()
                #Otherwise, not valid pawn move
                return False

        elif piece == 'N':
            #Checks if moved 3 spaces without going in only 1 direction
            #Guarantees that it moved only like a knight
            return (abs(new_row - old_row) + abs(new_col - old_col) == 3
                    and old_row != new_row and old_col != new_col)

                



#MAIN CODE
#This is just for testing purposes
#These will eventually be moved to a new file

board = Board()
board.print_board()
        
        
print(board.is_valid_move(1, 0, 3, 0))



