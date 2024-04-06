from Piece import Piece
from Enums.PieceType import PieceType


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, PieceType.KNIGHT)

    def check_move(self, start_pos, end_pos, board):
        """Code to check if a move is valid for a knight"""
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Knights move in an L-shape pattern (2 squares in one direction, 1 square in another)
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Check if the move is in an L-shape pattern (2 squares in one direction, 1 square in another)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            # Check if the target square is empty or has an opponent's piece to capture
            target_piece = board[end_row][end_col]
            if board.is_place_empty(end_row, end_col) or (isinstance(target_piece, Piece) and target_piece.color != self.color):
                self.move(start_pos, end_pos, board)
                return True

        return False
