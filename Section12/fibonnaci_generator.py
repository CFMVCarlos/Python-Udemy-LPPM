from typing import Generator, NoReturn


def fibonacci() -> Generator[int, None, NoReturn]:
    current, previous = 0, 1
    while True:
        yield current
        current, previous = previous, current + previous


def main():
    fib: Generator[int, None, NoReturn] = fibonacci()
    for _ in range(99):
        next(fib)
    print(f"100th fibonacci number is {next(fib)}")


if __name__ == "__main__":
    main()
