from Piece import Piece
from Enums.PieceType import PieceType


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, PieceType.PAWN)
        self.has_moved = False  # Flag to track if the pawn has moved

    def check_move(self, start_pos, end_pos):
        # Code to check if a move is valid for a pawn
        pass
