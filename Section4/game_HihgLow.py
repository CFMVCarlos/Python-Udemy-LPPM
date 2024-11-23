low: int = 1
high: int = 1000
attempts: int = 0

print(f"Please think of a number between {low} and {high}.")
input("Press ENTER to start.")

guess: int = low
while low != high:
    guess = low + (high - low) // 2
    attempts += 1
    high_low: str = input(
        f"My guess is {guess}. Should I guess higher or lower? "
        "Enter h or l, or c if my guess was correct: "
    ).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print(f"I got your number {guess} in {attempts} attempts.")
        break
    else:
        print("Please enter h, l, or c.")
else:
    print(f"You thought of the number {low}.")
    print(f"I got it in {attempts} attempts.")
