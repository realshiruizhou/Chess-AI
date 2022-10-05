from typing import List

class Board:
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
        for i in range(1, 9):
            result += str(9 - i) + '|' + ' '.join(self.state[i * 10 + 1: i * 10 + 9]) + '\n' 
        result += ' -----------------\n'
        result += '  a b c d e f g h\n\n'
        result += 'Moves: ' + ' '.join(self.generate_moves())
        return result

    def col_to_alph(self, x: int) -> str:
        return chr(x - 1 + ord('a'))

    def coord_to_move(self, x: int, y: int) -> str:
        return self.col_to_alph(x) + str(9 - y)
    
    def can_capture(self, x: int, y: int) -> bool:
        return self.state[y * 10 + x].isupper() if self.white_move else self.state[y * 10 + x].islower()

    def pawn_moves(self, x: int, y: int, moves: List[str]) -> None:
        if self.white_move:
            if self.state[(y - 1) * 10 + x] == '.':
                moves.append(self.coord_to_move(x, y - 1))
                # two moves
                if y == 7 and self.state[(y - 2) * 10 + x] == '.':
                    moves.append(self.coord_to_move(x, y - 2))
            # diagonal capture
            if self.can_capture(x - 1, y - 1):
                moves.append(self.col_to_alph(x) + "x" + self.coord_to_move(x - 1, y - 1))
            if self.can_capture(x + 1, y - 1):
                moves.append(self.col_to_alph(x) + "x" + self.coord_to_move(x + 1, y - 1))
        else:
            if self.state[(y + 1) * 10 + x] == '.':
                moves.append(self.coord_to_move(x, y + 1))
                # two moves
                if y == 2 and self.state[(y + 2) * 10 + x] == '.':
                    moves.append(self.coord_to_move(x, y + 2))
            # diagonal capture
            if self.can_capture(x - 1, y + 1):
                moves.append(self.col_to_alph(x) + "x" + self.coord_to_move(x - 1, y + 1))
            if self.can_capture(x + 1, y + 1):
                moves.append(self.col_to_alph(x) + "x" + self.coord_to_move(x + 1, y + 1))

    def rook_moves(self, x: int, y: int, moves: List[str]) -> None:
        up, down, left, right = y - 1, y + 1, x - 1, x + 1
        # moving up
        while self.state[up * 10 + x] == '.':
            moves.append("R" + self.coord_to_move(x, up))
            up -= 1
        # moving down
        while self.state[down * 10 + x] == '.':
            moves.append("R" + self.coord_to_move(x, down))
            down += 1
        # moving left
        while self.state[y * 10 + left] == '.':
            moves.append("R" + self.coord_to_move(left, y))
            left -= 1
        # moving right
        while self.state[y * 10 + right] == '.':
            moves.append("R" + self.coord_to_move(right, y))
            right += 1
        
        # capture up
        if self.can_capture(x, up):
            moves.append("Rx" + self.coord_to_move(x, up))
        # capture down
        if self.can_capture(x, down):
            moves.append("Rx" + self.coord_to_move(x, down))
        # capture left
        if self.can_capture(left, y):
            moves.append("Rx" + self.coord_to_move(left, y))
        # capture right
        if self.can_capture(right, y):
            moves.append("Rx" + self.coord_to_move(right, y))

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
                        self.pawn_moves(x, y, moves)
                    elif piece == 'r':
                        self.rook_moves(x, y, moves)
                # black piece and black to move        
                elif piece.isupper() and not self.white_move:
                    if piece == 'P':
                        # one move
                        self.pawn_moves(x, y, moves)
                    elif piece == 'R':
                        self.rook_moves(x, y, moves)
                        
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