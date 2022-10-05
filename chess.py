from board import Board

class Main:
    def play_chess(self):
        # set up board
        board = Board()

        # True for white, false for black
        player_color = False if input("What color do you want to play? W or B ") == "B" else True
        delay = int(input("How long would you like the engine to think (seconds)? "))

        while board.game_over() == 2:
            print(board)
            if board.white_move == player_color:
                player_move = input("What move are you going to play? ")
            

        outcome = board.game_over()
        if outcome == -1:
            print('Black Wins!')
        elif outcome == 1:
            print('White Wins!')
        else:
            print('Stalemate!')    

if __name__ == "__main__":
    main = Main()
    main.play_chess()