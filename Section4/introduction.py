for i in range(1, 13):
    # raise NotImplementedError("This code is not yet implemented")
    print(f"No. {i} squared is {i**2} and cubed is {i**3}")

print("*" * 50)

name: str = input("Please enter your name: ")
age: int = int(input(f"How old are you, {name}? "))

# if age >= 18:
#     print("You are old enough to vote.")
# else:
#     print(f"Please come back in {18 - age} years.")

if age < 18:
    print(f"Please come back in {18 - age} years.")
elif age == 900:
    print("Sorry, Yoda, you died in Return of the Jedi.")
else:
    print("You are old enough to vote.")

print("*" * 50)

if 16 <= age <= 65:
    print("Have a good day at work.")
else:
    print("Enjoy your free time.")

if age in range(16, 66):
    print("Have a good day at work.")
else:
    print("Enjoy your free time.")

print("*" * 50)

string = "Norwegian Blue"
letter = input("Enter a character: ")

#! Use casefold() to make the comparison case-insensitive
#! str.lower() is another option but does not handle all cases

if letter in string.casefold():
    print(f"Letter {letter} is in the string.")
else:
    print(f"Letter {letter} is not in the string.")
