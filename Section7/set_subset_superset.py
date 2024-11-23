# A subset is a set that is part of a larger set
# A superset is a set that contains another set

# A subset is done in python using <=
# However a proper subset is done using <

animals = {
    "Turle",
    "Horse",
    "Robin",
    "Python",
    "Swallow",
    "Hedgehog",
    "Wren",
    "Aardvark",
    "Cat",
}
birds = {"Robin", "Swallow", "Wren"}

print(
    f"birds is a subset of animals: {birds.issubset(animals)}"
)  # Same as birds <= animals
print(
    f"animals is a superset of birds: {animals.issuperset(birds)}"
)  # Same as animals >= birds

print(
    f"birds is a superset of animals: {birds.issuperset(animals)}"
)  # Same as birds >= animals
print(
    f"animals is a subset of birds: {animals.issubset(birds)}"
)  # Same as animals <= birds

garden_birds = {"Swallow", "Wren", "Robin"}
print(garden_birds == birds)
print(garden_birds <= birds)  # Check if it is a subset
print(garden_birds < birds)  # Check if it is a proper subset

print("*" * 80)

required_skills = ["python", "github", "linux"]
candidates = {
    "anna": {"java", "linux", "windows", "github", "python", "full stack"},
    "bob": {"github", "linux", "python"},
    "carol": {"linux", "javascript", "html", "python", "github"},
    "daniel": {"pascal", "java", "c++", "github"},
    "ekani": {"html", "css", "github", "python", "linux"},
    "fenna": {"linux", "pascal", "java", "c", "lisp", "modula-2", "perl", "github"},
}

interviewess = set()
for candidate, skills in candidates.items():
    # if set(required_skills).issubset(skills): #! Only checks for a subset
    if set(required_skills) < skills:  #! Checks for a proper subset
        interviewess.add(candidate)

print(f"{interviewess = }")
