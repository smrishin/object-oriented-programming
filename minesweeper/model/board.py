import random
from collections import deque
from .cell import Cell

class Board:
    def __init__(self, rows: int, cols: int, mines: int) -> None:
        if mines>=rows*cols:
            raise ValueError("Too many mines for this board size")
        
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self._mines_planted = False

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols
    
    def neighbors(self, r: int, c: int):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if self.in_bounds(nr, nc):
                    yield nr, nc
    
    def plant_mines(self, safe_r: int, safe_c: int):
        forbidden = {(safe_r, safe_c)}
        for nr, nc in self.neighbors(safe_r, safe_c):
            forbidden.add((nr, nc))
        
        candidates = [(r, c) for r in range(self.rows) for c in range(self.cols) 
                      if (r,c) not in forbidden]
        
        for r,c in random.sample(candidates, self.mines):
            self.grid[r][c].is_mine = True

        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                if cell.is_mine:
                    continue
                cell.adjacent_mines = sum(
                    1 for nr, nc in self.neighbors(r, c) if self.grid[nr][nc].is_mine
                )

        self._mines_planted = True

    def toggle_flag(self, r: int, c: int):
        cell = self.grid[r][c]
        if cell.revealed:
            return
        cell.flagged = not cell.flagged

    def reveal(self, r: int, c: int) -> str:
        """
        Returns:
          "noop" = nothing happened (already revealed or flagged)
          "boom" = hit a mine
          "ok"   = revealed successfully
        """

        if not self._mines_planted:
            self.plant_mines(r,c)

        cell = self.grid[r][c]

        if not cell.can_reveal():
            return "noop"

        if cell.is_mine:
            cell.revealed = True
            return "boom"
    
        self._flood_reveal(r,c)
        return "ok"

    def _flood_reveal(self, start_r: int, start_c: int):
        q = deque([(start_r, start_c)])

        while q:
            r, c = q.popleft()
            cell = self.grid[r][c]
            if not cell.can_reveal():
                continue

            cell.revealed = True

            if cell.adjacent_mines == 0:
                for nr, nc in self.neighbors(r, c):
                    ncell = self.grid[nr][nc]
                    if ncell.can_reveal() and (not cell.is_mine):
                        q.append((nr, nc))
            
    def all_safe_cells_reached(self) -> bool:
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                if (not cell.is_mine) and (not cell.revealed):
                    return False
        return True
    
    def reveal_all_mines(self):
        for row in self.grid:
            for cell in row:
                if cell.is_mine:
                    cell.revealed = True
    
    def flags_count(self) -> int:
        return sum(1 for row in self.grid for cell in row if cell.flagged)
    


