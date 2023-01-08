from exceptions import WrongInput
from game.field import Field

class Service:

    def __init__(self) -> None:
        
        self.minefield = None


    def set_difficulty(self, difficulty) -> None:
        
        if difficulty is 1:
            self.minefield = Field(5,5)
            return
        if difficulty is 2:
            self.minefield = Field(7,7)
            return
        if difficulty is 3:
            self.minefield = Field(9,9)
            return

        raise WrongInput("Difficulty must be 1, 2 or 3.")


    def print_field(self) -> None:

        print(self.minefield)

    
    def tap_position(self, row_n, col_n) -> None:
        
        ok = self.minefield.tap_cell_at(row_n, col_n)
        if ok is -1:
            raise WrongInput("Row and column must be in grid.")
