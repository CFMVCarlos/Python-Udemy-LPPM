class Player:

    def __init__(self, name) -> None:
        self.name: str = name
        self._lives: int = 3
        self._level: int = 1
        self._score: float = 0

    def _get_lives(self) -> int:
        return self._lives

    def _set_lives(self, lives: int) -> None:
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can't be negative")
            self._lives = 0

    def _get_level(self) -> int:
        return self._level

    def _set_level(self, levels: int = 1) -> None:
        if levels > 0:
            self._score += 1000 * (levels - self._level)
            self._level = levels
        else:
            print("Invalid level change")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self) -> float:
        return self._score

    @score.setter
    def score(self, points: float) -> None:
        self._score += points

    def __str__(self) -> str:
        return f"Name: {self.name}, Lives: {self._lives}, Level: {self._level}, Score: {self._score}"
