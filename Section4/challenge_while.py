import random

random.seed(69)

highest = 100
magic_number = random.randint(1, highest)
attempts = 0

print(f"I'm thinking of a number between 1 and {highest}. Can you guess it?")
while True:
    number = int(input("Enter your guess: "))
    attempts += 1

    if number == 0:
        print("You have quit the game.")
        break
    elif number > magic_number:
        print("Too high.")
    elif number < magic_number:
        print("Too low.")
    else:
        print(f"You got it in {attempts} attempts.")
        break
