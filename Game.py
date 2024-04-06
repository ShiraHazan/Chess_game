from Board import Board
from Player import Player
from Color import Color


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", Color.WHITE)
        self.player2 = Player("Player 2", Color.BLACK)
        self.current_player = self.player1

    def start_game(self):
        self.board.initialize_board()
        # Game loop
        # while not self.board.is_checkmate():
        #     # Code to handle player turns and moves
        #     pass
