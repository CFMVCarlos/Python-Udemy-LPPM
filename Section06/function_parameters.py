def func(p1, p2, *args, k, **kwargs):
    print(f"Positional-or-keyword:...{p1}, {p2}")
    print(f"Var-positional (*args):..{args}")
    print(f"Keyword:.................{k}")
    print(f"Var-keyword:.............{kwargs}")


def main():
    func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)


if __name__ == "__main__":
    main()
