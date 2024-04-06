from Piece import Piece


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "King"

    def check_move(self, start_pos, end_pos):
        """Code to check if a move is valid for a king"""
        pass