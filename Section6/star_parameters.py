def test_star_parameters(*args: int) -> None:
    for arg in args:
        print(arg, end=" ")
    print()


def main():
    test_star_parameters(10,20,30,40,50)
    numbers: list[int] = [1, 2, 3, 4, 5]
    test_star_parameters(*numbers)


if __name__ == "__main__":
    main()
