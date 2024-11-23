from timeit import timeit

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)


def spamless_comp():
    meals = [meal for meal in menu if not_spam(meal)]
    return meals


def not_spam(meal_list: list) -> bool:
    return "spam" not in meal_list


def spamless_filter():
    meals = list(filter(not_spam, menu))
    return meals


def main():
    time1 = timeit(spamless_comp, number=100000)
    time2 = timeit(spamless_filter, number=100000)

    print(f"Comprehension time:\t{time1}")
    print(f"Filter time:\t\t{time2}")


if __name__ == "__main__":
    main()
