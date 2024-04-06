from Piece_types.Bishop import Bishop
from Piece_types.King import King
from Piece_types.Pawn import Pawn
from Piece_types.Queen import Queen
from Piece_types.Rook import Rook
from Piece_types.Knight import Knight
from Color import Color


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

