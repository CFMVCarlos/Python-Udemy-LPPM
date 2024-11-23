print(__file__)

numbers: list[int] = [1, 2, 3, 4, 5, 6]

squares: list[int] = []
for number in numbers:
    squares.append(number**2)

print(squares)
