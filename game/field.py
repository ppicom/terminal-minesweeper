from random import choice
from game.cell import Cell

class Field:
    padding = "    "

    def trailing(row_n):
        return str(row_n+1) + " | "
    

    def __init__(self, height, width):
        
        self.cell_rows = [ [] for i in range(height) ]
        for row in range(len(self.cell_rows)):

            self.cell_rows[row] = [ Cell(choice([False,True])) for _ in range(width) ]

    
    def tap_cell_at(self, row_n, col_n) -> bool:
        
        row_idx, col_idx = row_n - 1, col_n -1
        
        if row_idx >= len(self.cell_rows):
            
            return False

        row = self.cell_rows[row_idx]
        if col_idx >= len(row):
            
            return False

        cell = row[col_idx]
        cell.tap()
        return True


    def get_game_status(self) -> int:
        """Returns -1 if a mine is tapped, 1 if all blanks have been tapped, 0 otherwise"""

        blanks_remain = False
        for row in self.cell_rows:
            
            for cell in row:
                
                if cell.tapped and cell.has_bomb:
                    
                    return -1
                
                if not cell.tapped and not cell.has_bomb: 
                    
                    blanks_remain = True

        return 0 if blanks_remain else 1
        

    def __repr__(self) -> str:
        row_n = len(self.cell_rows)
        col_n = 0 if row_n == 0 else len(self.cell_rows[0])
        
        r = self.header(col_n)
        for i, row in enumerate(self.cell_rows):
            str_row = [ str(cell) for cell in row ]
            r += Field.trailing(i) + " ".join(str_row) + "\n"
        
        return r


    def header(self, col_n) -> str:
        columns_numbers = Field.padding + " ".join([ str(i+1) for i in range(col_n) ]) + "\n"
        separator = Field.padding + " ".join([ "-" for _ in range(col_n) ]) + "\n"
        return columns_numbers + separator