class Cell:

    def __init__(self, bomb) -> None:
        self._has_bomb = bomb
        self._tapped = False


    def tap(self) -> None:
        self._tapped = True


    @property
    def has_bomb(self):
        return self._has_bomb

    
    @property
    def tapped(self) -> bool:
        return self._tapped

        
    def __repr__(self) -> str:
        if not self._tapped:
            return "#"
        if self._has_bomb:
            return "x"
        return " "