# An abstract class that expresses a piece on the game board
class Piece:
    def __init__(self, color, piece_type):
        self.color = color
        self.type = piece_type.value

    def check_move(self):
        """Code to determine valid move for a piece"""
        pass
