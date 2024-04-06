from Piece import Piece
from Enums.PieceType import PieceType


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, PieceType.QUEEN)

    def check_move(self, start_pos, end_pos):
        """Code to check if a move is valid for a queen"""
        pass