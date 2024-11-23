# Some ANSI escape sequences for colours and effects

class Color:
    # Foreground colors
    BLACK = "\u001b[30m"
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    # Reset all attributes
    RESET = "\u001b[0m"
    # Effects
    BOLD = "\u001b[1m"
    ITALIC = "\u001b[3m"
    UNDERLINE = "\u001b[4m"
    INVERT = "\u001b[7m"

def color_print(
    text: str,
    *effects: str,
    sep: str = " ",
    end: str = "\n",
) -> None:
    """
    Print `text` using the ANSI sequences to change color or add text variations

    Args:
        effect (str): The text to print
        text (str): The effect to apply to the text.
    """
    print(f"{"".join(effects)}{text}{Color.RESET}")
