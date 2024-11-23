import math
import turtle


def square(length: int) -> None:
    """Draws a square with sides of the given length."""
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)


def encircled_square(length: int) -> None:
    """Draws a squareof length `length` encircled by a circle."""
    square(length)
    angle: float = math.radians(45)
    radius: float = length * math.cos(angle)
    turtle.right(135)
    turtle.circle(radius)
    turtle.left(135)


def main() -> None:
    # square(120)

    # turtle.speed(200)
    # for value in range(72):
    #     square(120)
    #     turtle.left(5)

    # encircled_square(300)

    # turtle.speed(200)
    # for s in range(72):
    #     encircled_square(120)
    #     turtle.left(5)

    turtle.Screen().tracer(0)
    for s in range(72):
        encircled_square(120)
        turtle.left(5)
    turtle.Screen().update()

    turtle.done()


if __name__ == "__main__":
    main()
