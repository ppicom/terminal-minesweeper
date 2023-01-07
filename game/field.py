from random import choice
from game.cell import Cell

class Field:
    
    def __init__(self, height, width):
        
        self.cells = [ [] for i in range(height) ]
        for row in range(len(self.cells)):

            self.cells[row] = [ Cell(choice([False,True])) for _ in range(width) ]

    
    def tap_cell_at(self, row_n, col_n) -> None:
        
        row_idx, col_idx = row_n - 1, col_n -1
        
        if row_idx >= len(self.cells):
            return

        row = self.cells[row_idx]
        if col_idx >= len(row):
            return

        cell = row[col_idx]
        cell.tap()
        

    def __repr__(self) -> str:
        
        r = ""
        for row in self.cells:
            str_row = [ str(n) for n in row ]
            r += " ".join(str_row) + "\n"
        
        return r