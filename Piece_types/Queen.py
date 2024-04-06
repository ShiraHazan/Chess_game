from Piece import Piece


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Queen"

    def check_move(self, start_pos, end_pos):
        """Code to check if a move is valid for a queen"""
        pass