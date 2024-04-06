# An abstract class that expresses a piece on the game board
class Piece:
    def __init__(self, color, piece_type):
        self.color = color
        self.type = piece_type.value

    def check_move(self, start_pos, end_pos, board_department):
        """Code to determine valid move for a piece"""
        pass

    def move(self, start_pos, end_pos, board_department):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        board_department[end_row][end_col] = board_department[start_row][start_col]
        board_department[start_row][start_col] = ' '

