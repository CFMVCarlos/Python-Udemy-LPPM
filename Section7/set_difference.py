from primes_and_squares import primes_generator, squares_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(f"{evens = }")
print(f"{odds = }")

primes = set(primes_generator(100))
squares = set(squares_generator(100))

print(f"{primes = }")
print(f"{squares = }")

#! The difference operator is not commutative
print(f"{odds - primes = }")
print(f"{primes - odds = }")
