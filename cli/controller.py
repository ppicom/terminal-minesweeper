from game.service import Service
from cli.prompts import *

class Controller:
    
    def __init__(self) -> None:
        self.service = Service()
    

    def start_game(self) -> None:
        
        print(title_prompt)
        print(welcome_prompt)
        
        level_str = input(choose_level_prompt)
        self.service.set_difficulty(int(level_str))
    

    def is_game_done(self) -> bool:

        return self.service.is_game_done()
    

    def play_turn(self) -> None:

        self.service.print_field()
        cell_pos_str = input(choose_cell_prompt)
        row_str, col_str = cell_pos_str.split("x")
        self.service.play_turn(int(row_str), int(col_str))

    
    def end_game(self):

        if not self.service.is_game_done():
            raise Exception("Oh, that's a pickle! We should not be here.")

        self.service.print_field()

        if self.service.did_player_win():
            print(player_wins_prompt)
            return
        
        print(player_loses_prompt)