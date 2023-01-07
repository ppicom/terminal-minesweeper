from random import choice
from .cell import Cell

class Field:
    
    def __init__(self, height, width):
        
        self.cells = [ [] for i in range(height) ]
        i = 0
        while i < len(self.cells):
        
            self.cells[i] = [ Cell(choice([False,True])) for i in range(width) ]
            i+=1

    def __repr__(self) -> str:
        
        r = ""
        for row in self.cells:
            str_row = [ str(n) for n in row ]
            r += " ".join(str_row) + "\n"
        
        return r