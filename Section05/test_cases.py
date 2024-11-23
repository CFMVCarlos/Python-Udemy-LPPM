# Test cases are:
# 1. Outlying values at oth the low and high ends
# 2. Outlying values at the low end only
# 3. Outlying values at the high end only
# 4. No outlying values
# 5. Only outlying values (no valid values)
# 6. An empty data set


def filter_data_range(data) -> None:
    min_valid = 100
    max_valid = 200

    # process the low values in the list
    stop: int = 0
    for index, value in enumerate(data):
        if value >= min_valid:
            stop = index
            break
    del data[:stop]

    # process the high values in the list
    start: int = 0
    for index in range(len(data) - 1, -1, -1):
        if data[index] <= max_valid:
            start = index + 1
            break
    del data[start:]
    print(f"Start: {start}, Stop: {stop} and data: {data}")


def filter_data_range_single_loop(data) -> None:
    min_valid = 100
    max_valid = 200

    for index in range(len(data) - 1, -1, -1):
        if data[index] < min_valid or data[index] > max_valid:
            del data[index]
    print(f"Data: {data}")


def filter_unordered_data_range_single_loop(data) -> None:
    min_valid = 100
    max_valid = 200
    top_index: int = len(data) - 1
    for index, value in enumerate(reversed(data)):
        if value < min_valid or value > max_valid:
            del data[top_index - index]
    print(f"Data: {data}")


def test_filter_data_range(function) -> None:
    # Test case 1: Outlying values at both the low and high ends
    test_case_1_data: list[int] = [
        4,
        5,
        104,
        105,
        110,
        120,
        130,
        130,
        150,
        160,
        170,
        183,
        185,
        187,
        188,
        191,
        350,
        360,
    ]
    # Test case 2: Outlying values at the low end only
    test_case_2_data: list[int] = [
        4,
        5,
        104,
        105,
        110,
        120,
        130,
        130,
        150,
        160,
        170,
        183,
        185,
        187,
        188,
        191,
    ]
    # Test case 3: Outlying values at the high end only
    test_case_3_data: list[int] = [
        104,
        105,
        110,
        120,
        130,
        130,
        150,
        160,
        170,
        183,
        185,
        187,
        188,
        191,
        350,
        360,
    ]
    # Test case 4: No outlying values
    test_case_4_data: list[int] = [
        104,
        105,
        110,
        120,
        130,
        130,
        150,
        160,
        170,
        183,
        185,
        187,
        188,
        191,
    ]
    # Test case 5: Only outlying values (no valid values)
    test_case_5_data: list[int] = [4, 5, 350, 360]
    # Test case 6: An empty data set
    test_case_6_data: list[int] = []

    print(f"\n\nTest case for function: {function.__name__}")
    print("->Test case 1")
    function(test_case_1_data)
    print("->Test case 2")
    function(test_case_2_data)
    print("->Test case 3")
    function(test_case_3_data)
    print("->Test case 4")
    function(test_case_4_data)
    print("->Test case 5")
    function(test_case_5_data)
    print("->Test case 6")
    function(test_case_6_data)


test_filter_data_range(function=filter_data_range)
test_filter_data_range(function=filter_data_range_single_loop)
test_filter_data_range(function=filter_unordered_data_range_single_loop)
