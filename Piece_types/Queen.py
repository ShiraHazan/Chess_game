from Piece import Piece
from Rook import Rook
from Bishop import Bishop
from Enums.PieceType import PieceType


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, PieceType.QUEEN)

    def check_move(self, start_pos, end_pos, board):
        """Code to check if a move is valid for a queen"""
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Check if the move is valid for a rook (horizontal or vertical movement)
        if Rook.check_is_col(start_row, end_row, start_col, end_col, board):
            self.move(start_pos, end_pos, board)
            return True
        elif Rook.check_is_row(start_row, end_row, start_col, end_col, board):
            self.move(start_pos, end_pos, board)
            return True

        # Check if the move is valid for a bishop (diagonal movement)
        if Bishop.check_is_diagonal(start_pos, end_pos, board):
            self.move(start_pos, end_pos, board)
            return True

        return False

    def is_clear_diagonal(self, start_row, start_col, end_row, end_col, row_step, col_step, board):
        row, col = start_row + row_step, start_col + col_step
        while row != end_row and col != end_col:
            if board[row][col] != ' ':
                return False
            row += row_step
            col += col_step
        return True
