from Piece import Piece
from Enums.PieceType import PieceType


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, PieceType.ROOK)
        self.has_moved = False  # Flag to track if the rook has moved

    def check_move(self, start_pos, end_pos, board):
        """Code to check if a move is valid for a rook"""
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Rook can move horizontally or vertically in straight lines
        if self.check_is_col(start_row, end_row, start_col, end_col, board):
            self.move(start_pos, end_pos, board)
            return True
        elif self.check_is_row(start_row, end_row, start_col, end_col, board):
            self.move(start_pos, end_pos, board)
            return True
        return False

    @staticmethod
    def check_is_col(start_row, end_row, start_col, end_col, board):
        if start_row == end_row and start_col != end_col:
            step = 1 if end_col > start_col else -1
            if Rook.is_clear_path('col', start_col, end_col, step, board):
                return True
        return False

    @staticmethod
    def check_is_row(start_row, end_row, start_col, end_col, board):
        if start_col == end_col and start_row != end_row:
            step = 1 if end_row > start_row else -1
            if Rook.is_clear_path('row', start_row, end_row, step, board):
                return True

    @staticmethod
    def is_clear_path(fixed_pos, start_pos, end_pos, step, board):
        """check if the path is clear horizontally or vertically"""
        for pos in range(start_pos + step, end_pos, step):
            if fixed_pos == 'row' and board[start_pos][pos] != ' ':
                return False
            elif fixed_pos == 'col' and board[pos][start_pos] != ' ':
                return False
        return True
