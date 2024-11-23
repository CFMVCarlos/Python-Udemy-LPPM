class Wing(object):

    def __init__(self, ratio: float) -> None:
        self.ratio: float = ratio

    def fly(self) -> None:
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self) -> None:
        self._wing = Wing(1.8)

    def walk(self) -> None:
        print("Waddle, waddle, waddle")

    def swim(self) -> None:
        print("Come on in, the water's lovely")

    def quack(self) -> None:
        print("Quack quack")

    def fly(self) -> None:
        self._wing.fly()


class Penguin(object):

    def walk(self) -> None:
        print("Waddle, waddle, I waddle too")

    def swim(self) -> None:
        print("Come on in, but it's a bit chilly this far south")

    def quack(self) -> None:
        print("Are you 'avin a larf? I'm a penguin!")


def test_duck(duck) -> None:
    duck.walk()
    duck.swim()
    duck.quack()


def main() -> None:
    # donald = Duck()
    # test_duck(donald)
    # percy = Penguin()
    # test_duck(percy)

    donald = Duck()
    donald.fly()


if __name__ == "__main__":
    main()
