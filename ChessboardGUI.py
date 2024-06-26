import tkinter as tk
from tkinter import messagebox


class ChessboardGUI:
    def __init__(self, master):
        self.master = master
        self.board_canvas = tk.Canvas(master, width=655, height=655)
        self.board_canvas.pack(side=tk.LEFT)
        self.draw_board()
        self.place_pieces()
        self.selected_piece = None  # To store the selected piece
        self.drag_data = {"x": 0, "y": 0}  # To store drag data
        self.board_canvas.bind("<Button-1>", self.on_piece_click)
        self.board_canvas.bind("<B1-Motion>", self.on_piece_drag)
        self.board_canvas.bind("<ButtonRelease-1>", self.on_piece_release)

        # Create row and column labels
        self.create_labels()

    def draw_board(self):
        """Draw the chessboard with alternating colors"""
        colors = ["#E8DCC2", "#B18D76"]  # Light beige and wood brown colors
        square_size = 600 // 8
        for row in range(8):
            for col in range(8):
                color_index = (row + col) % 2
                color = colors[color_index]
                x0, y0 = col * square_size, row * square_size
                x1, y1 = x0 + square_size, y0 + square_size
                self.board_canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def place_pieces(self):
        """Place chess pieces on the board"""
        pieces = {
            "R": "\u2656", "N": "\u2658", "B": "\u2657", "Q": "\u2655",
            "K": "\u2654", "P": "\u2659", "r": "\u265C", "n": "\u265E",
            "b": "\u265D", "q": "\u265B", "k": "\u265A", "p": "\u265F"
        }
        self.piece_objects = {}  # To store piece objects for dragging
        square_size = 600 // 8
        for col, piece in enumerate("RNBQKBNR"):
            self.place_piece(0, col, pieces[piece], square_size)
            self.place_piece(7, col, pieces[piece.lower()], square_size)

        for col in range(8):
            self.place_piece(1, col, pieces["P"], square_size)  # Place white pawns
            self.place_piece(6, col, pieces["p"], square_size)  # Place black pawns

    def place_piece(self, row, col, piece, square_size):
        """Place a chess piece on the board at given position"""
        x, y = col * square_size + square_size // 2, row * square_size + square_size // 2
        piece_obj = self.board_canvas.create_text(x, y, text=piece, font=("Arial", square_size // 2), fill='black')
        self.piece_objects[piece_obj] = (row, col)  # Store piece object with its position

    def create_labels(self):
        """Create row and column labels for the board"""
        for row in range(8):
            y = row * (600 // 8) + (600 // 16)  # Adjust position
            label = tk.Label(self.master, text=str(8 - row), font=("Arial", 12))
            label.place(x=610, y=y)

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for col in range(8):
            x = col * (600 // 8) + (600 // 16)  # Adjust position
            label = tk.Label(self.master, text=letters[col], font=("Arial", 12))
            label.place(x=x, y=610)

    def on_piece_click(self, event):
        """Handle piece click event"""
        piece = self.board_canvas.find_closest(event.x, event.y)
        if piece:
            self.selected_piece = piece[0]
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

    def on_piece_drag(self, event):
        """Handle piece drag event"""
        if self.selected_piece:
            delta_x = event.x - self.drag_data["x"]
            delta_y = event.y - self.drag_data["y"]
            self.board_canvas.move(self.selected_piece, delta_x, delta_y)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

    def on_piece_release(self, event):
        """Handle piece release event"""
        if self.selected_piece:
            row = event.y // (600 // 8)
            col = event.x // (600 // 8)
            self.board_canvas.coords(self.selected_piece,
                                     col * (600 // 8) + (600 // 16),
                                     row * (600 // 8) + (600 // 16))
            self.piece_objects[self.selected_piece] = (row, col)
            messagebox.showinfo("Move Information", f"Piece moved to ({8 - row}, {chr(col + 97)})")
        self.selected_piece = None


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chessboard. All right reserved. Power by: Shira Hazan ©")
    ChessboardGUI(root)
    root.mainloop()
