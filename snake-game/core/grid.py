import random

class Grid:
    def __init__(self, rows: int, cols: int, cell_size: int) -> None:
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

    def in_bounds(self, pos: int) ->  bool:
        return 0 <= pos[0] < self.cols and 0 <= pos[1] < self.rows
    
    def to_pixels(self, pos: tuple[int, int]) -> tuple[int, int]:
        return (
            pos[0] * self.cell_size,
            pos[1] * self.cell_size
        )

    def random_cell(self):
        return (random.randrange(self.cols), random.randrange(self.rows))
    
    def random_free_cell(self, occupied):
        while True:
            cell = self.random_cell()
            if cell not in occupied:
                return cell
    
    