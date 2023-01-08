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
        row_n = len(self.cells)
        col_n = 0 if row_n == 0 else len(self.cells[0])
        
        r = self.header(col_n)
        for row in self.cells:
            str_row = [ str(cell) for cell in row ]
            r += " ".join(str_row) + "\n"
        
        return r

    def header(self, col_n) -> str:
        columns_numbers = " ".join([ str(i+1) for i in range(col_n) ]) + "\n"
        separator = " ".join([ "-" for _ in range(col_n) ]) + "\n"
        return columns_numbers + separator