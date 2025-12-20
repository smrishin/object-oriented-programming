import time
from .board import Board

class GameState:
    def __init__(self, rows: int, cols: int, mines: int) -> None:
        self.board = Board(rows, cols, mines)
        self.status = "ready"
        self.started_at = -1

    def start_if_needed(self):
        if self.status == "ready":
            self.status = "playing"
            self.started_at = time.time()

    def elapsed_seconds(self) -> int:
        if self.started_at == -1:
            return 0
        return int(time.time() - self.started_at)
    
    def handle_reveal(self, r: int, c: int) -> str:
        if self.status in ("won", "lost"):
            return "noop"
        
        self.start_if_needed()

        result = self.board.reveal(r, c)
        if result == "boom":
            self.status = "lost"
            self.board.reveal_all_mines()
        elif result == "ok" and self.board.all_safe_cells_reached():
            self.status = "won"
            self.board.reveal_all_mines()
        
        return result
