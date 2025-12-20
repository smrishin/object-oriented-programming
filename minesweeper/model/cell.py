from dataclasses import dataclass

@dataclass
class Cell:
    is_mine: bool = False
    revealed: bool = False
    flagged: bool = False
    adjacent_mines: int = 0

    def can_reveal(self) -> bool:
        return (not self.revealed) and (not self.flagged)
