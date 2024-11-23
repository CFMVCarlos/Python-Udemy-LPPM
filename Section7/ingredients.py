import time

from colors import Color, color_print

pantry: dict[str, int] = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes: dict[str, dict[str, int]] = {
    "Butter chicken": {
        "chicken": 750,
        "lemon": 1,
        "cumin": 1,
        "paprika": 1,
        "chilli powder": 2,
        "yogurt": 250,
        "oil": 50,
        "onion": 1,
        "garlic": 2,
        "ginger": 3,
        "tomato puree": 240,
        "almonds": 25,
        "rice": 360,
        "coriander": 1,
        "lime": 1,
    },
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
    "Pizza": {
        "pizza": 1,
    },
    "Egg sandwich": {
        "egg": 2,
        "bread": 80,
        "butter": 10,
    },
    "Beans on toast": {
        "beans": 1,
        "bread": 40,
    },
    "Spam a la tin": {
        "spam": 1,
        "tin opener": 1,
        "spoon": 1,
    },
}


def main():
    display_dict: dict[int, str] = {
        index + 1: meal for index, meal in enumerate(recipes)
    }

    shopping_list: dict[str, int] = {}

    while True:
        # Display the recipes
        color_print("\nPlease choose your recipe:", Color.BLUE)
        color_print("---------------------------", Color.BLUE)
        for key, value in display_dict.items():
            print(f"{Color.YELLOW}{key}{Color.RESET}. {value}")
        print()
        try:
            choice = int(input(f"{Color.BLUE}Enter the number of your choice: "))
            print(Color.RESET)
        except ValueError:
            color_print("\nPlease enter a valid number!", Color.RED, Color.BOLD)
            continue

        if not choice:
            break
        if choice in display_dict:
            selected_meal: str = display_dict[choice]
            color_print(f"\nYou have chosen {selected_meal}", Color.BLUE)

            print(f"{Color.BLUE}{Color.ITALIC}Checking ingredients", end="", flush=True)
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print(Color.RESET)

            ingredients: dict[str, int] = recipes[selected_meal]
            color_print("You need the following ingredients:", Color.BLUE)
            for food_item, required_quantity in ingredients.items():
                # Check if the food item is in the pantry
                quantity_in_pantry: int = pantry[food_item]
                print(f" - {food_item:13} ", end="")

                # Check if the food item is in the pantry
                shopping_quantity: int = required_quantity - quantity_in_pantry
                if required_quantity <= quantity_in_pantry:
                    # If the required quantity is less than or equal to the quantity in the pantry
                    pantry[food_item] -= required_quantity
                    color_print(f"OK", Color.GREEN, Color.BOLD)
                else:
                    # If the required quantity is more than the quantity in the pantry
                    pantry[food_item] = 0
                    add_shopping_item(shopping_list, food_item, shopping_quantity)
                    color_print(
                        f"X (Missing {shopping_quantity})",
                        Color.RED,
                        Color.BOLD,
                    )

    # Display the shopping list
    color_print("Your shopping list:", Color.BLUE)
    for item, quantity in shopping_list.items():
        print(f" - {item:13} {quantity}")
    print()


def add_shopping_item(
    shopping_list: dict[str, int], food_item: str, shopping_quantity: int
) -> None:
    # if food_item in shopping_list:
    #     shopping_list[food_item] += shopping_quantity
    # else:
    #     shopping_list[food_item] = shopping_quantity
    #! The above code can be replaced by the following single-line code
    shopping_list[food_item] = (
        shopping_list.setdefault(food_item, 0) + shopping_quantity
    )


if __name__ == "__main__":
    main()
