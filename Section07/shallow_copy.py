from copy import deepcopy

#! Shallow copy copies references, meaning it creates new immutable objects.
#! However, mutable objects are still referenced to the original object.

print("*" * 40)

animals: dict[str, str] = {"lion": "scary", "elephant": "big", "teddy": "cuddly"}
things: dict[str, str] = animals.copy()
animals["teddy"] = "toy"
print(things["teddy"])
print(animals["teddy"])

print("*" * 40)

animals2: dict[str, list[str]] = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}
things2 = animals2.copy()

things2["teddy"].append("toy")
print(id(things2["teddy"]), things2["teddy"])
print(id(animals2["teddy"]), animals2["teddy"])

print("*" * 40)

#! Deep copy copies everything, including the nested objects.

animals3: dict[str, list[str]] = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}
things3 = deepcopy(animals3)
things3["teddy"].append("toy")
print(id(things3["teddy"]), things3["teddy"])
print(id(animals3["teddy"]), animals3["teddy"])

print("*" * 40)
