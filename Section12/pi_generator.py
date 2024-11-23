from typing import Any, Generator, NoReturn


def odd_gen() -> Generator[int, Any, NoReturn]:
    n = 1
    while True:
        yield n
        n += 2


def calculate_pi() -> Generator[float, Any, NoReturn]:
    odd: Generator[int, Any, NoReturn] = odd_gen()
    approx = 0
    while True:
        approx += 4 / next(odd)
        yield approx
        approx -= 4 / next(odd)
        yield approx


def main():
    odd: Generator[int, Any, NoReturn] = odd_gen()
    for _ in range(10):
        print(next(odd))

    print("*" * 80)

    pi: Generator[float, Any, NoReturn] = calculate_pi()
    for _ in range(10):
        print(next(pi))

    print("*" * 80)

    pi_approx: Generator[float, Any, NoReturn] = calculate_pi()
    for _ in range(100_000_000):
        next(pi_approx)
    print(f"Pi is approximately {next(pi_approx)}")


if __name__ == "__main__":
    main()
