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


def render_move_text(moves: str):
    moves_list = moves.split()
    side = "White" if len(moves_list) % 2 == 1 else "Black"
    prevs = "\n"
    for i, move in enumerate(moves_list[:-1]):
        prevs += f"{move} "
        if (i + 1) % 2 == 0:
            prevs += "\n"
    return f"Current move : {side, moves_list[-1]} \nPrevious moves : {prevs}"


class ChessBoard(tk.Tk):
    def __init__(self, state: MyChess):
        super().__init__()
        self.title("Cognitive Chess")
        self.geometry("600x630")

        # convert
        convert_svg_to_png("board.svg", "board.png")
        self.image = Image.open("board.png")
        self.photo = ImageTk.PhotoImage(self.image)
        
        # grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # display on 0, 1
        self.canvas = tk.Canvas(self, width=self.image.width, height=self.image.height)
        self.canvas.grid(row=0, column=1, sticky="nw")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # # label
        # self.entry = tk.Label(self, text=render_move_text(state.moves),
        #                       justify="left", wraplength=400, anchor="nw", pady=20, padx = 10)
        # self.entry.grid(row=1, column=1, sticky="nw")
        
        # Frame to contain the label and the text widget for chess moves
        moves_frame = tk.Frame(self)
        moves_frame.grid(row=1, column=1, sticky="nw")
        
        # Label for chess moves inside the moves_frame
        moves_label = tk.Label(moves_frame, text="Chess Moves (Algebraic Form):")
        moves_label.grid(row=0, column=0, sticky="w")
        
        # Text widget for moves with a scrollbar inside the moves_frame
        self.moves_text = tk.Text(moves_frame, wrap="word", width=35, height=15)
        self.moves_text.grid(row=1, column=0, sticky="nw")
        
        # Scrollbar for the text widget
        self.scrollbar = tk.Scrollbar(moves_frame, orient="vertical", command=self.moves_text.yview)
        self.scrollbar.grid(row=1, column=1, sticky="ns")
        
        # Configure text widget to use scrollbar
        self.moves_text.config(yscrollcommand=self.scrollbar.set)
        
        # Insert moves text into the text widget
        self.moves_text.insert(tk.END, render_move_text(state.moves))


        # # text box (entry widget) in row 1, column 0
        # self.user_label = tk.Label(self, text="User:")
        # self.user_label.grid(row=1, column=0, sticky="nw")
        # self.entry = tk.Text(self, width=50, height=13, pady=20)
        # self.entry.grid(row=1, column=0, sticky="sw")
        
        # Frame to contain the label and the text widget
        user_frame = tk.Frame(self)
        user_frame.grid(row=1, column=0, sticky="nw")
        
        # Label for user inside the user_frame
        self.user_label = tk.Label(user_frame, text="User:")
        self.user_label.grid(row=0, column=0, sticky="w")
        
        # Text box (entry widget) inside the user_frame
        self.entry = tk.Text(user_frame, wrap="word", width=35, height=13, pady=20)
        self.entry.grid(row=1, column=0, sticky="nw")
        
        # Buttons
        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, sticky="ew")

        self.next_move_button = tk.Button(self, text="Next Move", command=self.play_next_move)
        self.next_move_button.grid(row=2, column=1, sticky="ew")

        self.prompt_button = tk.Button(self, text="Generate Prompt", command=self.generate_prompt)
        self.prompt_button.grid(row=3, column=0, sticky="ew")

        self.explanation_button = tk.Button(self, text="Get Explanation", command=self.get_explanation)
        self.explanation_button.grid(row=3, column=1, sticky="ew")
        
    def start_game(self):
        # Start the game logic here
        pass

    def play_next_move(self):
        # Play the next move logic here
        pass

    def generate_prompt(self):
       # Generate prompt logic here
       pass
    def get_explanation(self):
       pass

if __name__ == "__main__":
    moves = "d4 d6 Bf4 e5 Bg3 Nf6 e3 exd4 exd4 d5 c3 Bd6 Bd3 O-O Nd2 Re8+ Kf1 Bxg3 hxg3 b6 g4 Ba6 g5 Bxd3+ Ne2 Ne4 Nxe4 Bxe4 Nf4 Qxg5 Nh3 Bxg2+ Kg1 Qg6 Nf4 Qg5 Nxg2 Re6 Qd3 Rh6 Qe2 Nc6 Re1 g6 f4 Rxh1+ Kxh1 Qh6+ Kg1 a5 Qb5 Na7 Re8+ Rxe8 Qxe8+ Kg7 Qe5+ Kg8 Qxc7 Qh5 Qxa7 Qd1+ Kh2 Qa1 Nh4 Qxb2+ Kh3 Qxc3+ Kg4 Qxd4 Qb8+ Kg7 Nf3 Qa1 Kg5 Qxa2 Ne5 Qg2+ Kh4 h5 Nxf7 Qg4#"
    app = ChessBoard(MyChess(moves))
    app.mainloop()
