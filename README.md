# Chess GUI with Tkinter

This is a simple Python application that generates a chess GUI using Tkinter, Chess and Chess.svg. It includes a chess board rendered from SVG using the python-chess library and displays it within a Tkinter window. Additionally, it provides a text input box for user interaction.
![Chess GUI](GUI.png)

## Features

- Renders a chess board using python-chess library.
- Displays the chess board within a Tkinter window.
- Allows user interaction via a text input box.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your_username/chess_gui.git
cd chess_gui
```
2. The ChessBoard in render_board.py will render the chess board and it expects a MyChess object with a list of moves.
```%python
    moves = "d4 Nf6 c4 c5 e3 cxd4 exd4 d5 Nf3"
    app = ChessBoard(MyChess(moves))
    app.mainloop()
```
## To do -
- Top left box for API integration
- Fix previous and current move widget