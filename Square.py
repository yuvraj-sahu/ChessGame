#This is a class that will be used for each square of the board
class Square:
    def __init__(self, color, piece):
        self.color = color
        self.piece = piece
        
    def print_data(self):
        print(self.color + self.piece, end="")
        
    def set_color(self, color):
        self.color = color
        
    def set_piece(self, piece):
        self.piece = piece

    def get_color(self):
        return self.color

    def get_piece(self):
        return self.piece

    def isEmpty(self):
        return self.color == '-' and self.piece == '-'
