# Fizz buzz challenge with list comprehension
def is_fizz_or_buzz(number: int) -> str:
    if not number:  # Deal with zero
        return str(number)

    if not number % 15:
        return "FizzBuzz"

    if not number % 3:
        return "Fizz"

    if not number % 5:
        return "Buzz"

    return str(number)


fizz_max_number: int = 10
fizz_numbers: list[str] = [is_fizz_or_buzz(number) for number in range(fizz_max_number)]
print(fizz_numbers)

# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that lead to each of the
# other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.


locations: dict[int, str] = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of a hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in the forest",
}

exits: dict[int, dict[str, int]] = {
    0: {"Q": 0},
    1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    2: {"N": 5, "Q": 0},
    3: {"W": 1, "Q": 0},
    4: {"N": 1, "W": 2, "Q": 0},
    5: {"W": 2, "S": 1, "Q": 0},
}

location_with_exit: list[tuple[int, str]] = [
    (index, locations[index]) for index, exit in exits.items() if 5 in exit.values()
]
print(location_with_exit)
