farm_animals: set[str] = {"cow", "sheep", "hen", "goat", "horse"}

#! Sets are unordered, so the order of the elements in the set is not guaranteed

print(farm_animals)
for animal in farm_animals:
    print(animal)

choice = "-"  # initialise choice to something invalid
while choice != "0":
    if choice in set("12345"):
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()
