from random import randint


class Enemy:

    def __init__(
        self, name: str = "Enemy", hit_points: float = 0, lives: int = 1
    ) -> None:
        self.name: str = name
        self._hit_points: float = hit_points
        self._lives: int = lives
        self.alive = True
        self.MAX_HIT_POINTS: float = hit_points

    def setup_hit_points(self, hit_points: float) -> None:
        self._hit_points = hit_points
        self.MAX_HIT_POINTS = hit_points

    def take_damage(self, damage: float) -> None:
        remaining_points: float = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(
                f"{self.name} took {damage} points damage and have {self._hit_points} left"
            )
        else:
            self._lives -= 1
            if self._lives > 0:
                print(f"{self.name} lost a life")
                self._hit_points = self.MAX_HIT_POINTS
            else:
                print(f"{self.name} is now dead")
                self.alive = False

    def restore_hit_points(self) -> None:
        self._hit_points = self.MAX_HIT_POINTS

    def __str__(self) -> str:
        return (
            f"Name: {self.name}, Lives: {self._lives}, Hit Points: {self._hit_points}"
        )


class Troll(Enemy):

    def __init__(self, name: str = "Troll") -> None:
        # Enemy().__init__(name=name, lives=1, hit_points=23)
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self) -> None:
        print(f"Me {self.name}. {self.name} stomp you")


class Vampire(Enemy):

    def __init__(self, name: str = "Vampire") -> None:
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self) -> bool:
        return randint(1, 3) == 3

    def take_damage(self, damage: float) -> None:
        (
            super().take_damage(damage)
            if not self.dodges()
            else print(f"{self.name} dodges the attack!")
        )


class VampireKing(Vampire):

    def __init__(self, name: str = "Vampire King") -> None:
        super().__init__(name=name)
        self.setup_hit_points(140)

    def take_damage(self, damage: int) -> None:
        return super().take_damage(damage / 4)
