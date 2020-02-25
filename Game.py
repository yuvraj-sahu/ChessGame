from Board import Board

class Game:

    def __init__(self):
        self.board = Board()
        
    def start(self):
        game_status = '-'
        self.board.print_board()
        current_player = 'W'
        while game_status == '-':
            response = input("Enter your move: ").split(" ")
            if not len(response) == 4:
                print("Invalid input")
                continue

            #Temporary assignment
            old_row = old_col = new_row = new_col = 0
            try:  
                old_row = int(response[0])
                old_col = int(response[1])
                new_row = int(response[2])
                new_col = int(response[3])
            except ValueError:
                print("Invalid input")
                continue
                
            result = self.board.move(old_row, old_col, new_row, new_col)
            if result == False:
                print("Invalid move")
                continue

            self.board.print_board()
            game_status = self.board.get_game_status()

game = Game()
game.start()
