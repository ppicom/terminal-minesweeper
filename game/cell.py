class Cell:

    def __init__(self, bomb) -> None:
        self.has_bomb = bomb
        self.tapped = False

    def tap(self) -> None:
        self.tapped = True

    def __repr__(self) -> str:
        if not self.tapped:
            return "#"
        if self.has_bomb:
            return "x"
        return " "