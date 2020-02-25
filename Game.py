from Board import Board

class Game:

    def __init__(self):
        self.board = Board()
        
    def start(self):
        #Variable initialization
        game_status = '-'
        self.board.print_board()
        current_player = 'W'
        white_prompt = "White, enter your move: "
        black_prompt = "Black, enter your move: "
        prompt = white_prompt
        
        while game_status == '-':
            #Gets response
            response = input(prompt)

            #Checks if they want to quit the game
            if response.lower() == "quit":
                print("Exiting game")
                return

            #Splits the response by space-separated elements
            response = response.split(" ")
            
            #Makes sure that there are 4 elements
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

            #Prevent them from moving a piece that is not theirs
            if not self.board.get_square_color(old_row, old_col) == current_player:
                print("Invalid move n")
                continue

            #Checks if the move is valid    
            result = self.board.move(old_row, old_col, new_row, new_col)
            if result == False:
                print("Invalid move")
                continue

            #Switches players
            if current_player == 'W':
                current_player = 'B'
                prompt = black_prompt
            else:
                current_player = 'W'
                prompt = white_prompt

            #Prints board
            self.board.print_board()
            #Updates the status of the game
            game_status = self.board.get_game_status()
            print()

        #Prints the final result
        if game_status == 'W':
            print("White wins!")
        elif game_status == 'B':
            print("Black wins!")
        else:
            print("Stalemate!")
            

game = Game()
game.start()
