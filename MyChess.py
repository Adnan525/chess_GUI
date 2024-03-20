import chess
import chess.svg


class MyChess(chess.Board):
    def __init__(self, moves : str):
        super().__init__()
        self.moves = moves
        self.make_moves(moves)
        self.save_svg("board.svg")

    def make_moves(self, moves):
        move_list = moves.split()
        for move in move_list:
            try:
                self.push_san(move)
            except ValueError:
                print("Invalid move:", move)

    def generate_svg(self):
        svg_board = chess.svg.board(board=self)
        return svg_board

    def save_svg(self, filename):
        svg_data = self.generate_svg()
        with open(filename, "w") as f:
            f.write(svg_data)
