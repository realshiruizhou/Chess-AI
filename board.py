from typing import List
from constants import *

class Board():
    def __init__(self):
        # set up properties
        self.turn = 0
        self.white_move = True

        self.state = '*' * 10 + '*RNBQKBNR*' + '*' + 'P' * 8 + '*' + ('*' + '.' * 8 + '*') * 4 + '*' + 'p' * 8 + '*' + '*rnbqkbnr*' + '*' * 10

        # Keep track of king moves and rook moves for castling
        self.K_moved = self.k_moved = self.Ra_moved = self.Rh_moved = self.ra_moved = self.rh_moved = False
        self.white_check = self.black_check = False
        self.moves = self.generate_moves()

    def __repr__(self):
        result = '\n'
        for i in range(10):
            result += ' '.join(self.state[i * 10: i * 10 + 10]) + '\n' 
        result += 'Moves: ' + ' '.join(self.generate_moves())
        return result

    def col_to_alph(self, x: int) -> str:
        return chr(x - 1 + ord('a'))

    def coord_to_move(self, x: int, y: int) -> str:
        return self.col_to_alph(x) + str(9 - y)

    # TODO generate legal moves
    def generate_moves(self) -> List[str]:
        moves = []
        for y in range(1, 9):
            for x in range(1, 9):
                piece = self.state[y * 10 + x]
                # white piece and white to move
                if piece.islower() and self.white_move:
                    # white pawn move
                    if piece == 'p':
                        # one move
                        if self.state[(y - 1) * 10 + x] == '.':
                            moves.append(self.coord_to_move(x, y - 1))
                            # two moves
                            if y == 7 and self.state[(y - 2) * 10 + x] == '.':
                                moves.append(self.coord_to_move(x, y - 2))
                        # diagonal capture
                        if self.state[(y - 1) * 10 + x - 1].isupper():
                            moves.append(self.col_to_alph(x) + "x" + self.coord_to_move(x - 1, y - 1))
                        if self.state[(y - 1) * 10 + x + 1].isupper():
                            moves.append(self.col_to_alph(x) + "x" + self.coord_to_move(x + 1, y - 1))
                # black piece and black to move        
                elif piece.isupper() and not self.white_move:
                    if piece == 'P':
                        # one move
                        if self.state[(y + 1) * 10 + x] == '.':
                            moves.append(self.coord_to_move(x, y + 1))
                            # two moves
                            if y == 2 and self.state[(y + 2) * 10 + x] == '.':
                                moves.append(self.coord_to_move(x, y + 2))
                        # diagonal capture
                        if self.state[(y + 1) * 10 + x - 1].islower():
                            moves.append(self.col_to_alph(x) + "x" + self.coord_to_move(x - 1, y + 1))
                        if self.state[(y + 1) * 10 + x + 1].islower():
                            moves.append(self.col_to_alph(x) + "x" + self.coord_to_move(x + 1, y + 1))
                        
        return moves

    # -1 for black victory, 0 for stalemate, 1 for white victory, 2 if continue playing
    def game_over(self):
        moves = self.moves
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