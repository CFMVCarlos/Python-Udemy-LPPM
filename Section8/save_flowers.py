data: list[str] = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_print_filename = "Section8/plants_print.txt"
with open(plants_print_filename, "w") as plant_file:
    for plant in data:
        print(plant, file=plant_file)

new_list: list[str] = []
with open(plants_print_filename) as plant_file:
    for plant in plant_file:
        new_list.append(plant.rstrip())
print(new_list)

#! Write function must be used with a string
plants_write_filename = "Section8/plants_write.txt"
with open(plants_write_filename, "w") as plant_file:
    for plant in data:
        plant_file.write(plant)
