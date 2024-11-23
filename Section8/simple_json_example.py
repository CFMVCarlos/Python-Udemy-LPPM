import json

#! JSON does not support tuples, sets or complex numbers, it converts them to lists
#! JSON should not be used when its necessary to preserve the data types
languages: list[tuple[str, int]] = [
    ("ABC", 1987),
    ("Algol 68", 1968),
    ("APL", 1962),
    ("C", 1973),
    ("Haskell", 1990),
    ("Lisp", 1958),
    ("Modula-2", 1977),
    ("Perl", 1987),
]

with open("Section8/test.json", "w", encoding="utf-8") as testfile:
    json.dump(languages, testfile)

with open("Section8/test.json", "r", encoding="utf-8") as testfile:
    data: list[list[str | int]] = json.load(testfile)
print(data)
