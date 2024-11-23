from data import plants_list


def sort_perennials(item) -> str:
    return (
        "1" + item.name if item.lifecycle.casefold() == "perennial" else "0" + item.name
    )


# plants_list.sort(key=lambda item: "1" + item.name if item.lifecycle.casefold() == "perennial" else "0" + item.name)
plants_list.sort(
    key=lambda item: (
        "1" + item.name if item.lifecycle.casefold() == "perennial" else "0" + item.name
    )
)

with open("Section12/planting_instructions.txt", "w", encoding="utf-8") as output_file:
    # for plant in plants_list:
    #     where_to_plant = "window box" if plant.lifecycle == "Perennial" else "garden"
    #     print(f"Plant {plant.name} in a {where_to_plant}.", file=output_file)

    for plant in plants_list:
        (where_to_plant, who) = (
            ("window box", "me")
            if plant.lifecycle == "Perennial"
            else ("garden", "gardener")
        )
        print(f"Plant {plant.name} in a {where_to_plant}, {who}.", file=output_file)
