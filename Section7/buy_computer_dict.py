available_parts: dict[int, str] = {
    1: "Computer",
    2: "Monitor",
    3: "Keyboard",
    4: "Mouse",
    5: "Mouse Mat",
    6: "HDMI Cable",
}

current_choice: int = -1
computer_parts: dict[int, str] = {}  # create an empty dict

while current_choice != 0:
    if current_choice in available_parts:
        chosen_part: str = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your list now contains {computer_parts}")
    else:
        print("Please add options from the list below:")
        for key, part in available_parts.items():
            print(f"{key}: {part}")
        print("0: to finish")
    try:
        current_choice = int(input("-> "))
    except ValueError as e:
        print("Please enter a valid option")

print(f"Your list of computer parts: {computer_parts}")
