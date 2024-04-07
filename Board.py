from Piece import Piece
from Piece_types.Bishop import Bishop
from Piece_types.King import King
from Piece_types.Pawn import Pawn
from Piece_types.Queen import Queen
from Piece_types.Rook import Rook
from Piece_types.Knight import Knight
from Enums.Color import Color


class Board:
    def __init__(self):
        # The game board consists of an 8/8 matrix
        self.board = [[' ' for _ in range(8)] for _ in range(8)]

    def initialize_board(self):
        """Code to set up initial positions of pieces"""
        # White pieces
        self.board[0] = [
            Rook(Color.WHITE), Knight(Color.WHITE), Bishop(Color.WHITE), Queen(Color.WHITE),
            King(Color.WHITE), Bishop(Color.WHITE), Knight(Color.WHITE), Rook(Color.WHITE)
        ]
        self.board[1] = [Pawn(Color.WHITE) for _ in range(8)]

        # Black pieces
        self.board[7] = [
            Rook(Color.BLACK), Knight(Color.BLACK), Bishop(Color.BLACK), Queen(Color.BLACK),
            King(Color.BLACK), Bishop(Color.BLACK), Knight(Color.BLACK), Rook(Color.BLACK)
        ]
        self.board[6] = [Pawn(Color.BLACK) for _ in range(8)]

    def is_place_empty(self, i, j):
        if self.board[i][j] == ' ':
            return True
        return False

    def are_opponents(self, piece1_row, piece1_col, piece2_row, piece2_col):
        """Checking if 2 pieces are opponents"""
        if (isinstance(self.board[piece1_row][piece1_col], Piece)
                and isinstance(self.board[piece2_row][piece2_col], Piece) and
                self.board[piece2_row][piece2_col].color != self.board[piece1_row]
                [piece1_col].color):
            return True
        return False
