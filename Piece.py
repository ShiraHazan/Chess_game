# An abstract class that expresses a piece on the game board
class Piece:
    def __init__(self, color):
        self.color = color

    def check_move(self):
        """Code to determine valid move for a piece"""
        pass
