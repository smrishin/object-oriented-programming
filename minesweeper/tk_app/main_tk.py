import tkinter as tk
from .view_tk.tk_view import TkMinesweeperView
from model.gamestate import GameState
from .controller_tk.controller import GameController

def game_factory(rows: int, cols: int, mines: int):
    return GameState(rows, cols, mines)

def main():
    root = tk.Tk()
    root.title("Minesweeper by Rishi")

    top = tk.Frame(root)
    top.pack(pady=10)

    # Select Difficulty
    difficulty_var = tk.StringVar(value="Begginer (9x9, 10 Mines)")
    difficulty_menu = tk.OptionMenu(top, difficulty_var, *GameController.DIFFICULTIES.keys())
    difficulty_menu.pack(side="left", padx=5)

    # Reset
    reset_btn = tk.Button(top, text="Reset")
    reset_btn.pack(side="left", padx=5)

    # Labels
    status_label = tk.Label(root, font=("Arial", 12))
    status_label.pack()

    info_label = tk.Label(root, font=("Arial", 12))
    info_label.pack(pady=(0,10))

    # Initial Game setup
    rows, cols, mines = GameController.DIFFICULTIES[difficulty_var.get()]
    game = game_factory(rows, cols, mines)
    view = TkMinesweeperView(root, rows, cols)


    controller = GameController(root, game, view, status_label, info_label, difficulty_var)

    view.build_grid(controller.on_left_click, controller.on_right_click)
    controller.render()
    
    reset_btn.config(command=lambda: controller.on_reset(game_factory))

    def on_diff_change(*_):
        controller.on_change_difficulty(difficulty_var.get(), game_factory)
    
    difficulty_var.trace_add("write", on_diff_change)

    def tick():
        if controller.game.status == "playing":
            controller.render()
        root.after(500, tick)

    tick()

    root.mainloop()

if __name__ == "__main__":
    main()