import timeit
from typing import Generator

setup = """\
gc.enable()
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
"""

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


def nested_loop() -> list[list[tuple[int, str]]]:
    result: list[list[tuple[int, str]]] = []
    for loc in sorted(locations):
        exits_to_destination_1: list[tuple[int, str]] = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)
    for x in result:
        pass
    return result


def loop_comp() -> list[list[tuple[int, str]]]:
    result: list[list[tuple[int, str]]] = []
    for loc in sorted(locations):
        exits_to_destination_2: list[tuple[int, str]] = [
            (xit, locations[xit]) for xit in exits if loc in exits[xit].values()
        ]
        result.append(exits_to_destination_2)
    for x in result:
        pass
    return result


def nested_comp() -> list[list[tuple[int, str]]]:
    result: list[list[tuple[int, str]]] = [
        [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        for loc in sorted(locations)
    ]
    for x in result:
        pass
    return result


def nested_gen() -> Generator[list[tuple[int, str]], None, None]:
    result: Generator[list[tuple[int, str]], None, None] = (
        [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        for loc in sorted(locations)
    )
    for x in result:
        pass
    return result


number_of_runs: int = 100000
result_1: float = timeit.timeit(nested_loop, setup, number=number_of_runs)
result_2: float = timeit.timeit(loop_comp, setup, number=number_of_runs)
result_3: float = timeit.timeit(nested_comp, setup, number=number_of_runs)
result_4: float = timeit.timeit(nested_gen, setup, number=number_of_runs)

print(f"Nested Loop:\t{result_1:.6f}")
print(f"Loop and Comp:\t{result_2:.6f}")
print(f"Nested Comp:\t{result_3:.6f}")
print(f"Nested Gen:\t{result_4:.6f}")
