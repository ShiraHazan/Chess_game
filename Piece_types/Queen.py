from Piece import Piece
from Rook import Rook
from Enums.PieceType import PieceType


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, PieceType.QUEEN)

    def check_move(self, start_pos, end_pos, board):
        """Code to check if a move is valid for a queen"""
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # צריך להשתמש בפונקציות בצריח ורץ
        # Check if the move is valid for a rook (horizontal or vertical movement)
        if start_row == end_row and start_col != end_col:
            step = 1 if end_col > start_col else -1
            if self.is_clear_path('col', start_col, end_col, step, board):
                self.move(start_pos, end_pos, board)
                return True
        elif start_col == end_col and start_row != end_row:
            step = 1 if end_row > start_row else -1
            if self.is_clear_path('row', start_row, end_row, step, board):
                self.move(start_pos, end_pos, board)
                return True

        # Check if the move is valid for a bishop (diagonal movement)
        if abs(end_row - start_row) == abs(end_col - start_col):
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            if self.is_clear_diagonal(start_row, start_col, end_row, end_col, row_step, col_step, board):
                self.move(start_pos, end_pos, board)
                return True

        return False

    def is_clear_path(self, fixed_pos, start_pos, end_pos, step, board):
        return Rook.is_clear_path(fixed_pos, start_pos, end_pos, step, board)

    def is_clear_diagonal(self, start_row, start_col, end_row, end_col, row_step, col_step, board):
        row, col = start_row + row_step, start_col + col_step
        while row != end_row and col != end_col:
            if board[row][col] != ' ':
                return False
            row += row_step
            col += col_step
        return True