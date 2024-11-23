vehicles: dict[str, str] = {
    "dream": "Honda 250T",
    "road": "Nissan Altima",
    "grail": "Toyota Highlander",
    "work": "Toyota Forklift",
    "tank": "International Harvester",
    "boat": "Grady White",
    "plane": "Cessna",
}

# Add a new key-value pair
vehicles["bike"] = "Harley"

# Get the value of a key
my_car = vehicles["road"]
print(my_car)
commuter = vehicles.get("plane")
print(commuter, "\n")

# Delete a key-value pair
# del vehicles["plane"]
vehicles.pop("plane")
# del vehicles["NotExists"] # KeyError
print(
    vehicles.pop("NotExists", "Key does not exist!")
)  # Try to remove a key that does not exist
print(
    vehicles.pop("boat", "Key does not exist!"), "\n"
)  # Remove the key-value pair and return the value

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")
for key, value in vehicles.items():
    print(key, value, sep=", ")
