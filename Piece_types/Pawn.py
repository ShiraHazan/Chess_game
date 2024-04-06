from Piece import Piece
from Enums.PieceType import PieceType
from Enums.Color import Color


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, PieceType.PAWN)
        self.has_moved = False  # Flag to track if the pawn has moved

    def check_move(self, start_pos, end_pos, board_department):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        direction = 1 if self.color == Color.WHITE else -1  # Pawn movement direction based on color

        # Pawn can move forward by one square
        if start_col == end_col and end_row == start_row + direction:
            # Check if the target square is empty
            if board_department[end_row][end_col] == ' ':
                self.move(start_pos, end_pos, board_department)
                self.has_moved = True
                return True

        # Pawn can move forward by two squares on its first move
        if not self.has_moved and start_col == end_col and end_row == start_row + 2 * direction:
            # Check if both squares are empty
            if board_department[end_row][end_col] == ' ' and board_department[start_row + direction][end_col] == ' ':
                self.move(start_pos, end_pos, board_department)
                self.has_moved = True
                return True

        # Pawn can capture diagonally
        if abs(end_col - start_col) == 1 and end_row == start_row + direction:
            target_piece = board_department[end_row][end_col]
            # Check if there's an opponent's piece to capture
            if isinstance(target_piece, Piece) and target_piece.color != self.color:
                self.move(start_pos, end_pos, board_department)
                self.has_moved = True
                return True

        return False

