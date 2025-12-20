from js import document
from pyodide.ffi import create_proxy

from model.gamestate import GameState

DIFFICULTIES = {
    "Beginner (9x9, 10 mines)": (9, 9, 10),
    "Intermediate (16x16, 40 mines)": (16, 16, 40),
    "Expert (16x30, 99 mines)": (16, 30, 99),
}

game = None

def set_text(id_, text):
    document.getElementById(id_).innerText = text

def build_difficulty_options():
    sel = document.getElementById("difficulty")
    sel.innerHTML = ""
    for label in DIFFICULTIES.keys():
        opt = document.createElement("option")
        opt.value = label
        opt.text = label
        sel.appendChild(opt)

def render():
    b = game.board
    set_text("status", f"Status: {game.status}")
    set_text("meta", f"Mines: {b.mines} | Flags: {b.flags_count()}")

    board_el = document.getElementById("board")
    board_el.style.gridTemplateColumns = f"repeat({b.cols}, 34px)"
    board_el.innerHTML = ""

    for r in range(b.rows):
        for c in range(b.cols):
            cell = b.grid[r][c]
            div = document.createElement("div")
            div.classList.add("cell")

            if cell.revealed:
                div.classList.add("revealed")
                if cell.is_mine:
                    div.classList.add("mine")
                    div.innerText = "💣"
                else:
                    div.innerText = "" if cell.adjacent_mines == 0 else str(cell.adjacent_mines)
            else:
                if cell.flagged:
                    div.classList.add("flagged")
                    div.innerText = "🚩"
                else:
                    div.innerText = ""

            # attach click handlers only if game still playable
            if game.status not in ("won", "lost"):
                div.addEventListener("click", create_proxy(make_left_click(r, c)))
                div.addEventListener("contextmenu", create_proxy(make_right_click(r, c)))

            board_el.appendChild(div)

def make_left_click(r, c):
    def handler(evt):
        game.handle_reveal(r, c)
        render()
    return handler

def make_right_click(r, c):
    def handler(evt):
        evt.preventDefault()  # block browser right-click menu
        game.board.toggle_flag(r, c)
        render()
    return handler

def new_game(rows, cols, mines):
    global game
    game = GameState(rows, cols, mines)
    render()

def wire_controls():
    # reset
    reset_btn = document.getElementById("reset")
    def on_reset(evt):
        label = document.getElementById("difficulty").value
        r, c, m = DIFFICULTIES[label]
        new_game(r, c, m)
    reset_btn.addEventListener("click", create_proxy(on_reset))

    # difficulty change
    sel = document.getElementById("difficulty")
    def on_change(evt):
        label = sel.value
        r, c, m = DIFFICULTIES[label]
        new_game(r, c, m)
    sel.addEventListener("change", create_proxy(on_change))

build_difficulty_options()
wire_controls()

# start default
default_label = "Beginner (9x9, 10 mines)"
document.getElementById("difficulty").value = default_label
r, c, m = DIFFICULTIES[default_label]
new_game(r, c, m)
