data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

# print(ord("a"))
# print(ord("b"))
# print(ord("z"))


def simple_hash(s: str) -> int:
    """A simple hash function to demonstrate collisions"""
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> str | None:
    """ " Return the value for a given key or None if the key is not in the hash table"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys: list[str] = [""] * 10
values: list[str] = keys.copy()


def main():
    global keys, values

    # for key, _ in data:
    #     h = simple_hash(key)
    #     h2 = hash(key)
    #     print(f"{key:10} | {h:2} | {h2}")

    for key, value in data:
        h = simple_hash(key)
        # h2 = hash(key)
        print(f"{key:10} | {h:2}")
        keys[h] = key
        values[h] = value
    print(f"\nkeys: {keys}")
    print(f"values: {values}")
    print(f"\nHash value: {get("lemon")}")
    print(f"Hash value: {get("banana")}") # Same hash value as lemon


if __name__ == "__main__":
    main()
