burguers: list[str] = ["beef", "chicken", "spicy bean"]
toppings: list[str] = ["cheese", "egg", "beans", "spam"]

meals: list[tuple[str, str]] = [
    (burguer, topping) for burguer in burguers for topping in toppings
]
print(meals)

print("*" * 80)

for burguer, topping in meals:
    print(f"{burguer} with {topping}")

print("*" * 80)

for meal in [[(burguer, topping) for burguer in burguers] for topping in toppings]:
    print(meal)

print("*" * 80)

for meal in [[(burguer, topping) for topping in toppings] for burguer in burguers]:
    print(meal)
