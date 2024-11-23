import sys
from typing import Generator


def my_range(n: int) -> Generator[int, None, None]:
    start = 0
    while start < n:
        yield start
        start += 1


big_range = range(10000)
print(f"big_range is {sys.getsizeof(big_range)} bytes")

# Create a list of numbers from 0 to 999
big_list = list(big_range)
print(f"big_list is {sys.getsizeof(big_list)} bytes")

big_my_range: Generator[int, None, None] = my_range(10000)
print(f"big_range is {sys.getsizeof(big_range)} bytes")

print(next(big_my_range))
