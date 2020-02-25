#This is a class that will be used for each square of the board
class Square:

    #These do not include blank squares (dashes)
    #because one will not be allowed to set a piece/color to a dash
    #Instead, they will have to make sure that they use set_to_empty
    #to make sure that users do not set a square
    #to a blank color and valid piece or vice versa

    valid_colors = ('B', 'W')
    valid_pieces = ('P', 'R', 'N', 'B', 'Q', 'K')
    
    def __init__(self, color, piece):
        if color == '-' and piece == '-':
            self.set_to_empty()
        else:
            self.set_color(color)
            self.set_piece(piece)

    #Some helpful methods to be used by other classes
    
    def print_data(self):
        print(self.color + self.piece, end="")
        
    def set_color(self, color):
        if color in Square.valid_colors:
            self.color = color
        else:
            raise ValueError("Not a valid color: " + color)
        
    def set_piece(self, piece):
        if piece in Square.valid_pieces:
            self.piece = piece
        else:
            raise ValueError("Not a valid piece: " + piece)

    def get_color(self):
        return self.color

    def get_piece(self):
        return self.piece

    def is_empty(self):
        return self.color == '-' and self.piece == '-'

    def set_to_empty(self):
        self.color = '-'
        self.piece = '-'
