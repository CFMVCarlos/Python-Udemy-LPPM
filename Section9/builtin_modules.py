import shelve

print([d for d in dir() if not d.startswith("__")])

print("*" * 60)

# print(dir(__builtins__))
for d in dir(__builtins__):
    print(d)

print("*" * 60)

print(dir(shelve))

print("*" * 60)

for obj in dir(shelve.Shelf):
    if not obj.startswith("__"):
        print(obj)

print("*" * 60)

help(shelve)