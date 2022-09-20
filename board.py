from constants import *

class Board():
    def __init__(self):
        # set up properties
        self.turn = 0
        self.white_move = True

        self.state = 'RNBQKBNR' + 'P' * 8 + '.' * 32 + 'p' * 8 + 'rnbqkbnr'

        # Keep track of king moves and rook moves for castling
        self.K_moved = self.k_moved = self.Ra_moved = self.Rh_moved = self.ra_moved = self.rh_moved = False
        self.white_check = self.black_check = False

    def __repr__(self):
        result = '\n'
        for i in range(8):
            result += ' '.join(self.state[i * 8: i * 8 + 8]) + '\n' 
        result += 'Moves: ' + ' '.join(self.generate_moves())
        return result
    
    # TODO generate legal moves
    def generate_moves(self):
        moves = ["e4"]
        return moves

    # -1 for black victory, 0 for stalemate, 1 for white victory, 2 if continue playing
    def game_over(self):
        moves = self.generate_moves()
        if len(moves) == 0:
            if self.white_move:
                return -1 if self.white_check else 0
            else:
                return 1 if self.black_check else 0
        return 2
    
    def evaluate_board(self):
        piece_values = 0
        for each in self.state:
            piece_values += VALUES[each]
        return piece_values