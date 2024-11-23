print(__file__)

numbers: list[int] = [1, 2, 3, 4, 5, 6]

squares: list[int] = [number**2 for number in numbers]

print(squares)
