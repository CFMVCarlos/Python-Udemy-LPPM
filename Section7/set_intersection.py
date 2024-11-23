from primes_and_squares import primes_generator, squares_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(f"{evens = }")
print(f"{odds = }")

primes = set(primes_generator(100))
squares = set(squares_generator(100))

print(f"{primes = }")
print(f"{squares = }")

print(f"{odds & squares = }")
print(f"{evens & squares = }")

#! Intersection with a iterable can only be done with intersection method
even_squares_iterable = evens.intersection(squares_generator(100))
print(f"{even_squares_iterable = }")

trial_1 = {"Bob", "Charley", "Georgia", "John"}
trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}

check_set = trial_1 & trial_2
print(f"\n{check_set = }")

print()

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides = {"donkey", "horse", "camel"}

mounts = farm_animals & wild_animals & potential_rides
# mounts = farm_animals.intersection(wild_animals, potential_rides)
print(f"{mounts = }")
