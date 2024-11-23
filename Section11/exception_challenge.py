import sys


def get_int() -> int:
    while True:
        try:
            return int(input("Please enter a number: "))
        except ValueError:
            print("Please enter a valid number")
        except EOFError:
            sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(0)


def main() -> None:
    input_numer_1: int = get_int()
    input_numer_2: int = get_int()
    try:
        divided_number: float = input_numer_1 / input_numer_2
    except ZeroDivisionError:
        print("You cannot divide by zero")
        return
    print(f"{input_numer_1} divided by {input_numer_2} is {divided_number}")


if __name__ == "__main__":
    main()
