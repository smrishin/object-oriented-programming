import tkinter as tk
from typing import Callable

from model.gamestate import GameState
from ..view_tk.tk_view import TkMinesweeperView

class GameController:
    DIFFICULTIES = {
        "Begginer (9x9, 10 Mines)" : (9, 9, 10),
        "Intermediate (16x16, 40 Mines)": (16, 16, 40),
        "Expert (16x30, 99 Mines)": (16, 30, 99)
    }

    def __init__(
            self, 
            root: tk.Tk,
            game: GameState, 
            view: TkMinesweeperView, 
            status_label: tk.Label, 
            info_label: tk.Label,
            difficulty_var: tk.StringVar
            ) -> None:
        self.root = root
        self.game = game
        self.view = view
        self.difficulty_var = difficulty_var
        self.status_label = status_label
        self.info_label = info_label

        self.rows = game.board.rows
        self.cols = game.board.cols
        self.mines = game.board.mines

    def new_games(self, rows: int, cols: int, mines: int, game_factory: Callable[[int, int, int], GameState]):
        self.view.frame.destroy()
        
        self.game = game_factory(rows, cols, mines)
        self.rows, self.cols, self.mines = rows, cols, mines

        self.view = self.view.__class__(self.root, rows, cols)
        self.view.build_grid(self.on_left_click, self.on_right_click)
        self.render()

    def on_reset(self, game_factory: Callable[[int, int, int], GameState]):
        rows, cols, mines = self.rows, self.cols, self.mines
        self.new_games(rows, cols, mines, game_factory)

    def on_change_difficulty(self, selected_label: str, game_factory: Callable[[int, int, int], GameState]):
        rows, cols, mines = self.DIFFICULTIES[selected_label]
        self.new_games(rows, cols, mines, game_factory)


    def render(self):
        self.status_label["text"] = f"{self.game.status.capitalize()}!!!" if self.game.status != "playing" else ""
        self.info_label["text"] = (
            f"Mines: {self.mines} | "
            f"Flags: {self.game.board.flags_count()} | "
            f"Time: {self.game.elapsed_seconds()}"
        )

        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.game.board.grid[r][c]
                
                if cell.revealed:
                    if cell.is_mine:
                        text = "💥"
                        bg = "#ff4d4d" 
                        
                    else:
                        text = "" if cell.adjacent_mines == 0 else str(cell.adjacent_mines)
                        bg = "#d9d9d9"
                    disabled = True
                else:
                    text = "🚩" if cell.flagged else " "
                    bg = "#ffd966" if cell.flagged else "SystemButtonFace"
                    disabled = False

                self.view.set_cell_text(r, c, text, disabled, bg)
        
        if self.game.status in ("won", "lost"):
            for r in range(self.rows):
                for c in range(self.cols):
                    self.view.buttons[r][c]["state"] = "disabled"   

    def on_left_click(self, r: int, c: int):
        self.game.handle_reveal(r, c)
        self.render()

        print(f"Left click at ({r}, {c})")

    def on_right_click(self, r: int, c: int):
        if self.game.status in ("won", "lost"):
            return        

        self.game.board.toggle_flag(r, c)
        self.render()

        print(f"Right click at ({r}, {c})")




