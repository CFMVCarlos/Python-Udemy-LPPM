from data import basic_plants_list, people, plants_dict, plants_list

if people and all(person[1] for person in people):
    print("Sending email")
else:
    print("User must edit the record")

if any(plant.plant_type == "Grass" for plant in plants_list):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

word_to_check = "Grass"
if any(plant.plant_type == word_to_check for plant in plants_dict.values()):
    print(f"This pack contains {word_to_check}")
else:
    print(f"No {word_to_check} in this pack")
