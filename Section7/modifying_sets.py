data = [
    "blue",
    "red",
    "green",
    "yellow",
    "blue",
    "red",
    "green",
    "yellow",
    "blue",
    "red",
    "green",
    "yellow",
]

# Create a set from the data list, which will remove duplicates
# This does not preserve the order of the elements in the list
unique_data = set(data)
print(unique_data)

# To preserve the order of the elements in the original list
unique_data = list(dict.fromkeys(data).keys())
print(unique_data)

small_ints = set(range(21))
print(small_ints)

small_ints.add(21)
# Discard will not raise an error if the element is not in the set
small_ints.discard(10)
# Remove will raise an error if the element is not in the set
small_ints.remove(11)
print(small_ints)
