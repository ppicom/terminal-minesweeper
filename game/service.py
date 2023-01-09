from game.exceptions import WrongInput
from game.field import Field

class Service:

    def __init__(self) -> None:
        
        self.minefield = None


    def set_difficulty(self, difficulty) -> None:
        
        if difficulty == 1:
            self.minefield = Field(3, 3)
            return
        if difficulty == 2:
            self.minefield = Field(7, 7)
            return
        if difficulty == 3:
            self.minefield = Field(9, 9)
            return

        raise WrongInput("Difficulty must be 1, 2 or 3.")


    def print_field(self) -> None:

        print(self.minefield)


    def is_game_done(self) -> bool:
        
        return self.minefield.get_game_status() != 0


    def play_turn(self, row_n, col_n) -> None:

        ok = self.minefield.tap_cell_at(row_n, col_n)
        if not ok:
            raise WrongInput("Row and column must be in grid.")
    

    def did_player_win(self) -> bool:
        
        return self.minefield.get_game_status() == 1
