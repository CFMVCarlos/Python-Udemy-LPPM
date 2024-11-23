menu: list[list[str]] = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["spam", "bacon", "spam", "tomato", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print(f"{meal} has a spam score of {meal.count("spam")}")

print("\n\nMeal without spam")
for meal_index, meal in enumerate(menu):
    top_index: int = len(meal) - 1
    
    #! Reverse the list to avoid index out of range error
    for index, ingredient in enumerate(reversed(meal)):
        if ingredient == "spam":
            del meal[top_index - index]
    print(", ".join(meal))

## Convert list of number into a integer
list_to_be_converted: list[int] = [1,2,3,4,5,6,7,8,9,0]
int_converted: int = int("".join(map(lambda x: str(x), list_to_be_converted)))
print(f"\n\nConverted integer: {int_converted}")
