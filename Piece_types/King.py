from Piece import Piece
from Enums.PieceType import PieceType


class King(Piece):
    def __init__(self, color):
        super().__init__(color, PieceType.KING)

    def check_move(self, start_pos, end_pos, board):
        """Check if a move is valid for a king"""
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Check if the destination is within one square of the king
        if abs(end_row - start_row) <= 1 and abs(end_col - start_col) <= 1:
            # Check if the destination is not occupied by own piece
            if not board.is_same_color_piece(end_row, end_col, self.color):
                return True

        return False