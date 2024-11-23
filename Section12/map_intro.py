from timeit import timeit

text = "what have the romans ever done for us"


def to_capitals_letters():
    capitals = [char.upper() for char in text]
    return capitals


# Use map
def to_capitals_letters_map():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def to_capitals_words():
    words = [word.upper() for word in text.split(" ")]
    return words


# Use map
def to_capitals_words_map():
    map_capitals = list(map(str.upper, text.split(" ")))
    return map_capitals


def main():
    letters_1 = timeit(to_capitals_letters, number=100000)
    letters_2 = timeit(to_capitals_letters_map, number=100000)
    words_1 = timeit(to_capitals_words, number=100000)
    words_2 = timeit(to_capitals_words_map, number=100000)

    print(f"Capital letters with list comp:\t{letters_1}")
    print(f"Capital letters with map:\t{letters_2}")
    print(f"Capital words with list comp:\t{words_1}")
    print(f"Capital words with map:\t\t{words_2}")


if __name__ == "__main__":
    main()
