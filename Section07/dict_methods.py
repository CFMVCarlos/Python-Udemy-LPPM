d = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ["chicken", "spam", "egg", "bread", "lemon"]

new_dict = dict.fromkeys(pantry_items, 0)
print(new_dict)

d2 = {
    7: "Lucky seven",
    10: "ten",
    3: "This is the magic number",
}

# d.update(d2) # Use this to update the dictionary if using Python 3.8 or below
d |= d2  # Use this to update the dictionary if using Python 3.9 or above
print(d)
