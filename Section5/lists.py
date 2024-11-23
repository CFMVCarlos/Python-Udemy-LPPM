available_parts: list[str] = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "mouse mat",
    "hdmi cable",
]
current_choice: int = -1
computer_parts: list[str] = []  # create an empty list

while current_choice != 0:
    if current_choice > 0 and current_choice <= len(available_parts):
        chosen_part: str = available_parts[current_choice - 1]
        if chosen_part in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
        print(f"Your list now contains {computer_parts}")
    else:
        print("Please add options from the list below:")
        for index, part in enumerate(available_parts):
            print(f"{index+1}: {part}")
        print("0: to finish")
    try:
        current_choice = int(input())
    except ValueError as e:
        print("Please enter a valid option")

print(computer_parts)