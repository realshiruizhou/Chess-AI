from board import Board
from constants import *

class Minimax:
    def __init__(self):
        pass
    
    def evaluate_board(self, board):
        piece_values = 0
        for each in board.state:
            piece_values += VALUES[each]
        return piece_values