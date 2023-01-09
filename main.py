from cli.controller import Controller

def play():
    controller = Controller()

    controller.start_game()

    while not controller.is_game_done():
        controller.play_turn()

    controller.end_game()

play()