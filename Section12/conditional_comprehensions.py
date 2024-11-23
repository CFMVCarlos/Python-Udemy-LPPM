menu: list[list[str]] = [
    ["egg", "bacon"],
    ["egg", "sausage"],
    ["egg", "bacon", "sausage"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "spam", "spam", "spam", "spam", "spam", "bacon"],
]

meals: list[list[str]] = [meal for meal in menu if "spam" not in meal]
print(meals)

# This acts as a filter to remove any meal that contains spam
fussy_meals: list[list[str]] = [
    meal for meal in menu if "spam" in meal and "sausage" in meal
]
print(fussy_meals)

# The if acts now as a conditional expression to replace the spam with "meal skipped"
meal_or_not: list[list[str] | str] = [
    meal if "spam" not in meal else "meal skipped" for meal in menu
]
print(meal_or_not)
