from random import choice

class Field:
    
    def __init__(self, height, width):
        
        self.cells = [ [] for i in range(height) ]
        i = 0
        while i < len(self.cells):
        
            self.cells[i] = [ choice([0,1]) for i in range(width) ]
            i+=1

    def __repr__(self) -> str:
        
        r = ""
        for row in self.cells:
            str_row = [ str(n) for n in row ]
            r += " ".join(str_row) + "\n"
        
        return r