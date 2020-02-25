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

    #Prints the board
    def print_board(self):
        for r in range(0, 8):
            for c in range(0, 8):
                self.print_square(r, c)
                print(" ", end="")
            print()

    #Prints the information for one square
    def print_square(self, row, col):
        self.board[row][col].print_data()

    #Doesn't need self because all board dimensions are the same
    def is_valid_board_position(row, col):
        return row >= 0 and col >= 0 and row < 8 and col < 8

    def is_valid_move(self, old_row, old_col, new_row, new_col):

        #Must make a move
        if old_row == new_row and old_col == new_col:
            return False
        
        old_square = self.board[old_row][old_col]

        #Must have a piece on that square
        if old_square.is_empty():
            return False
        
        piece = old_square.get_piece()
        color = old_square.get_color()

        #Checks if the piece is moved to a square with the same colored piece
        if self.board[new_row][new_col].get_color() == color:
            return False

        #If this is a pawn
        if piece == 'P':            
            if color == 'W':
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

        elif piece == 'B':
            #Checks if it was a diagonal move
            if abs(new_row - old_row) == abs(new_col - old_col):
                col_direction = 1
                if new_col < old_col:
                    col_direction = -1

                row_direction = 1
                if new_row < old_row:
                    row_direction = -1

                #Checks for any pieces in the bishop's path
                for i in range(1, abs(new_row - old_row)):
                    if not self.board[old_row + i * row_direction][old_col + i * col_direction].is_empty():
                        return False

                return True

            return False

        elif piece == 'R':
            #Checks if it moved horizontally
            if new_row == old_row:
                #Checks for any pieces in the rook's path
                for col in range(min(new_col, old_col) + 1, max(new_col, old_col)):
                    if not self.board[new_row][col].is_empty():
                        return False

                return True

            #Checks if it moved vertically
            elif new_col == old_col:
                #Checks for any pieces in the rook's path
                for row in range(min(new_row, old_row) + 1, max(new_row, old_row)):
                    if not self.board[row][new_col].is_empty():
                        return False

                return True

            else:
                return False

        elif piece == 'K':
            #Checks if king has moved only one square in any direction
            #Also checks that the king is not moving into a spot where it can be taken
            if abs(new_row - old_row) <= 1 and abs(new_col - old_col) <= 1:
                return not self.is_threatened_square(new_row, new_col, self.board[new_row][new_col].get_color())
            return False

        elif piece == 'Q':

            #This uses the checks for both the rook and the bishop
            
            if new_row == old_row:
                for col in range(min(new_col, old_col) + 1, max(new_col, old_col)):
                    if not self.board[new_row][col].is_empty():
                        return False

                return True

            elif new_col == old_col:
                for row in range(min(new_row, old_row) + 1, max(new_row, old_row)):
                    if not self.board[row][new_col].is_empty():
                        return False

                return True

            elif abs(new_row - old_row) == abs(new_col - old_col):
                col_direction = 1
                if new_col < old_col:
                    col_direction = -1

                row_direction = 1
                if new_row < old_row:
                    row_direction = -1

                for i in range(1, abs(new_row - old_row)):
                    if not self.board[old_row + i * row_direction][old_col + i * col_direction].is_empty():
                        return False

                return True

            return False

        #Should never reach this spot
        return False
            

    #Checks if a current square is threatened
    #Only checks if it is threatened by a piece
    #That is not of the player_color
    def is_threatened_square(self, row, col, player_color):
        for r in range(0, 8):
            for c in range(0, 8):
                square = self.board[r][c]
                
                if square.get_color() == player_color or square.is_empty():
                    continue
                
                if square.get_piece() == 'K':
                    return abs(row - r) <= 1 and abs(col - c) <= 1
                elif self.is_valid_move(r, c, row, col):
                    return True

        return False


    #Checks if a player has won
    #'B' = black won, 'W' = white won, '-' = no winner (continue play), 'S' = stalemate
    def get_game_status(self):
        for row in range(0, 8):
            for col in range(0, 8):
                if self.board[row][col].get_piece() == 'K':
                    try:
                        for r in range(row - 1, row + 2):
                            for c in range(col - 1, col + 2):
                                if r == row and c == col:
                                    continue
                                if not self.is_threatened_square(r, c, self.board[r][c].get_color()):
                                    #This is an error thrown to break out of multiple loops
                                    #Also used to check if there is a winner
                                    raise RuntimeError()
                                
                    except RuntimeError:
                        continue #This means that the king had a place to move

                    #The king did not have a place to move
                    #This means that it is either a checkmate or a stalemate
                    player_color = self.board[row][col].get_color()
                    if self.is_threatened_square(row, col, player_color):
                        #This is a checkmate
                        if player_color == 'B':
                            #White wins
                            return 'W'
                        else:
                            #Black wins
                            return 'B'
                    else:
                        #This is a stalemate
                        return 'S'

        #There is no winner
        return '-'


    #Moves a piece if valid
    #Returns true if the piece was moved and false if the move was invalid
    def move(self, old_row, old_col, new_row, new_col):
        if self.is_valid_move(old_row, old_col, new_row, new_col):
            old_square = self.board[old_row][old_col]
            new_square = self.board[new_row][new_col]
            new_square.set_color(old_square.get_color())
            new_square.set_piece(old_square.get_piece())
            old_square.set_to_empty()

            return True

        return False


    #Some helpful methods
    def get_square_color(self, row, col):
        return self.board[row][col].get_color()

    def get_square_piece(self, row, col):
        return self.board[row][col].get_piece()

