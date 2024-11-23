# In an early video, we used a for loop to print the times tables, for values from 1 to 10.
# That was a nested loop, which appears below.
#
# The challenge is to use a nested comprehension, to produce the same values.
# You can iterate over the list, to produce the same output as the for loop, or just print out the list.

from typing import Generator

for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

print("*" * 80)

multiply_table: Generator[tuple[int, int], None, None] = (
    (i, i * j) for i in range(1, 11) for j in range(1, 11)
)
for i, j in multiply_table:
    print(f"{i:2d} {j:3d}")
