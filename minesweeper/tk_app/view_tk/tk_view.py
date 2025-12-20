import tkinter as tk
from typing import Callable


class TkMinesweeperView:
    def __init__(self, root: tk.Tk, rows: int, cols: int):
        self.root = root
        self.rows = rows
        self.cols = cols

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]

    def build_grid(self, on_left_click: Callable[[int, int], None], on_right_click: Callable[[int, int], None]):
        for r in range(self.rows):
            for c in range(self.cols):
                btn = tk.Button(
                    self.frame,
                    width=3,
                    height=1,
                    text=" ",
                    font=("Segoe UI Emoji", 10),
                    relief="raised", 
                    command=lambda rr=r, cc=c: on_left_click(rr,cc)
                )
                btn.bind("<Button-3>", lambda e, rr=r, cc=c: on_right_click(rr, cc))

                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn
    
    def set_cell_text(self, r: int, c: int, text: str, disabled: bool, bg: str):
        btn = self.buttons[r][c]
        btn["text"] = text
        btn["state"] = "disabled" if disabled else "normal"
        btn["relief"] = "flat" if disabled else "raised"
        btn["bg"] = bg

    
