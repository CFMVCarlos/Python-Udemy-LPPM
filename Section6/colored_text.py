from colors import Color, color_print


def main() -> None:
    #! This is a way to import all attributes from a class into the current namespace
    #! But it is not recommended because it can pollute the namespace and make it hard to debug
    # attributes = {
    #     name: value for name, value in vars(Color).items() if not name.startswith("__")
    # }
    # globals().update(attributes)

    print("\nThis should be in the default terminal color\n")

    color_print("This is red", Color.RED)
    color_print("This is blue", Color.BLUE)
    color_print("This is yellow", Color.YELLOW)
    color_print("This is green", Color.GREEN)
    color_print("This is magenta", Color.MAGENTA)
    color_print("This is cyan", Color.CYAN)
    color_print("This is white", Color.WHITE)
    color_print("This is black", Color.BLACK)

    print()

    color_print("This is bold", Color.BOLD)
    color_print("This is underline", Color.UNDERLINE)
    color_print("This is reversed", Color.INVERT)

    print()

    color_print("This is bold and red", Color.BOLD, Color.RED)
    color_print("This is underline and blue", Color.UNDERLINE, Color.BLUE)
    color_print("This is reversed and yellow", Color.INVERT, Color.YELLOW)
    color_print("This is italic and green", Color.ITALIC, Color.GREEN)
    color_print(
        "This is bold, underline, and magenta",
        Color.BOLD,
        Color.UNDERLINE,
        Color.MAGENTA,
    )
    color_print(
        "This is bold, reversed, underline, italic, and cyan",
        Color.BOLD,
        Color.INVERT,
        Color.UNDERLINE,
        Color.ITALIC,
        Color.CYAN,
    )


if __name__ == "__main__":
    main()
