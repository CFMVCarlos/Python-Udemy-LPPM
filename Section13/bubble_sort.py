def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n: int = len(data)
    comparison_count: int = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparison_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        print(f"End of pass {i + 1}: {data}")
        if not swapped:
            break
    print(f"Total comparisons made: {comparison_count}")


def main():
    data: list = [5, 3, 8, 6, 1, 9, 2, 7]
    print(f"Unsorted: {data}")
    bubble_sort(data)
    print(f"Sorted: {data}")


if __name__ == "__main__":
    main()
