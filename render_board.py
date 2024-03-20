import tkinter as tk
from PIL import Image, ImageTk
import cairosvg
from MyChess import MyChess


def convert_svg_to_png(svg_file, png_file):  # Tkinter not working with svg
    with open(svg_file, "rb") as f:
        svg_data = f.read()
    png_data = cairosvg.svg2png(bytestring=svg_data, output_width=300, output_height=300)
    with open(png_file, "wb") as f:
        f.write(png_data)


def render_move_text(moves : str):
    moves_list = moves.split()
    return f"Current move : {moves_list[-1]} \n Previous moves : {moves_list[:-1]}"


class ChessBoard(tk.Tk):
    def __init__(self, state: MyChess):
        super().__init__()
        self.title("Cognitive Chess")
        self.geometry("600x600")

        # convert
        convert_svg_to_png("board.svg", "board.png")
        self.image = Image.open("board.png")
        self.photo = ImageTk.PhotoImage(self.image)

        # grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # display on 0, 1
        self.canvas = tk.Canvas(self, width=self.image.width, height=self.image.height)
        self.canvas.grid(row=0, column=1, sticky="nsew")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Create text box (entry widget) in row 1, column 1
        self.entry = tk.Label(self, text=render_move_text(state.moves))
        self.entry.grid(row=1, column=1, sticky="nsew")


if __name__ == "__main__":
    moves = "d4 Nf6 c4 c5 e3 cxd4 exd4 d5 Nf3"
    app = ChessBoard(MyChess(moves))
    app.mainloop()
