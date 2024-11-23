from Section7.set_remove import adverse_interactions

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

#! Union of two sets can be done using the union method or using the pipe operator
# all_animals = farm_animals.union(wild_animals)
all_animals = farm_animals | wild_animals
print(all_animals)

meds_to_watch = set().union(*adverse_interactions)

print(*sorted(meds_to_watch), sep="\n")
