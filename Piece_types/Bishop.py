from Piece import Piece
from Enums.PieceType import PieceType


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, PieceType.BISHOP)

    def check_move(self, start_pos, end_pos, board):
        """Code to check if a move is valid for a bishop"""
        # Check if the move is along a diagonal
        if self.check_is_diagonal(start_pos, end_pos, board):
            self.move(start_pos, end_pos, board)
            return True
        return False

    @staticmethod
    def check_is_diagonal(start_pos, end_pos, board):
        """Checking if it is diagonal"""
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if abs(end_row - start_row) == abs(end_col - start_col):
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            if Bishop.is_clear_diagonal(start_row, start_col, end_row, end_col, row_step, col_step, board):
                return True

        return False

    @staticmethod
    def is_clear_diagonal(start_row, start_col, end_row, end_col, row_step, col_step, board):
        """Checking if the path is clear diagonally"""
        row, col = start_row + row_step, start_col + col_step
        while row != end_row and col != end_col:
            if board.is_place_empty(row, col):
                return False
            row += row_step
            col += col_step
        return True
