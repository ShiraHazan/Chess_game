import tkinter as tk


class ChessboardGUI:
    def __init__(self, master):
        self.master = master
        self.board_canvas = tk.Canvas(master, width=400, height=400)
        self.board_canvas.pack()
        self.draw_board()
        self.place_pieces()

    def draw_board(self):
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                color_index = (row + col) % 2
                color = colors[color_index]
                x0, y0 = col * 50, row * 50
                x1, y1 = x0 + 50, y0 + 50
                self.board_canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def place_pieces(self):
        pieces = {
            "R": "♜", "N": "♞", "B": "♝", "Q": "♛",
            "K": "♚", "P": "♟", "r": "♖", "n": "♘",
            "b": "♗", "q": "♕", "k": "♔", "p": "♙"
        }
        for col in range(8):
            self.place_piece(1, col, pieces["P"])
            self.place_piece(6, col, pieces["p"])

        for col, piece in enumerate("RNBQKBNR"):
            self.place_piece(0, col, pieces[piece])
            self.place_piece(7, col, pieces[piece.lower()])

    def place_piece(self, row, col, piece):
        x, y = col * 50 + 25, row * 50 + 25
        self.board_canvas.create_text(x, y, text=piece, font=("Arial", 32))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chessboard")
    ChessboardGUI(root)
    root.mainloop()
