from Piece import Piece


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Rook"

    def check_move(self, start_pos, end_pos):
        """Code to check if a move is valid for a rook"""
        pass
