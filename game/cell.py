class Cell:

    def __init__(self, bomb) -> None:
        self._has_bomb = bomb
        self.tapped = False

    def tap(self) -> None:
        self.tapped = True

    @property
    def has_bomb(self):
        return self._has_bomb
        
    def __repr__(self) -> str:
        if not self.tapped:
            return "#"
        if self._has_bomb:
            return "x"
        return " "