import tkinter as tk


class ChessboardGUI:
    def __init__(self, master):
        self.master = master
        self.board_canvas = tk.Canvas(master, width=400, height=400)
        self.board_canvas.pack()
        self.draw_board()

    def draw_board(self):
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                color_index = (row + col) % 2
                color = colors[color_index]
                x0, y0 = col * 50, row * 50
                x1, y1 = x0 + 50, y0 + 50
                self.board_canvas.create_rectangle(x0, y0, x1, y1, fill=color)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chessboard")
    ChessboardGUI(root)
    root.mainloop()
