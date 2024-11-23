from functools import lru_cache


@lru_cache(3)
def fibonacci(n) -> float:
    """Return the `n`th Fibonacci number, for positive `n`."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterative(n) -> float:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_memoization(n, memo={}) -> float:
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(
            n - 2, memo
        )
        return memo[n]


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    else:
        memo[n] = n * factorial_memoization(n - 1, memo)
        return memo[n]


if __name__ == "__main__":
    while True:
        try:
            number = int(input("\nInsert a positive number: "))
            if number == 0:
                break
            if number < 496:
                print(f"-> The fibonnacci number is {fibonacci(number)}")
                print(f"\t-> The factorial number is {factorial_recursive(number)}")

            print(
                f"-> The fibonnacci number iterative is {fibonacci_iterative(number)}"
            )
            if number < 1500:
                print(
                    f"\t-> The factorial number iterative is {factorial_iterative(number)}"
                )

            if number < 996:
                print(
                    f"-> The fibonnacci number memoization is {fibonacci_memoization(number)}"
                )
                print(
                    f"\t-> The factorial number memoization is {factorial_memoization(number)}"
                )

        except ValueError:
            print("Please insert a valid positive number")
