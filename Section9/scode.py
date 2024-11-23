def fact(n):
    """Calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    """Calculate n! recursively"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fib(n):
    """F(n) = F(n-1) + F(n-2)"""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fibonacci(n: int) -> int:
    if n < 2:
        return n

    n_minus1: int = 1
    n_minus2: int = 0
    for f in range(1, n):
        result: int = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for i in range(130):
    # print(f"{i:3}: {fact(i)}")
    print(f"{i:3}: {factorial(i)}")

print()

for i in range(36):
    # print(f"{i:3}: {fib(i)}")
    print(f"{i:3}: {fibonacci(i)}")
