import datetime
import random
from re import I

import pytz

# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

total_timezones = 9
timezones_indexes: list[int] = random.sample(
    range(len(pytz.all_timezones)), total_timezones
)


def display_menu() -> None:
    print("\nChoose a time zone:")
    for i in range(len(timezones_indexes)):
        print(f"{i+1}. {pytz.all_timezones[timezones_indexes[i]]}")
    print("0. Quit\n")


def get_user_choice() -> int:
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 0 or choice > total_timezones:
                raise ValueError
            return choice
        except ValueError:
            print(
                f"Invalid choice. Please enter a number between 0 and {total_timezones}."
            )


def display_time_in_timezone(timezone) -> None:
    tz = pytz.timezone(timezone)
    current_time: datetime.datetime = datetime.datetime.now(tz)
    local_time: datetime.datetime = datetime.datetime.now()
    utc_time: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)

    print(f"Time in {timezone}: {current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
    print(f"Local time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"UTC time: {utc_time.strftime('%Y-%m-%d %H:%M:%S')}")


def main() -> None:
    while True:
        display_menu()
        choice: int = get_user_choice()
        if choice == 0:
            break
        timezone = pytz.all_timezones[timezones_indexes[choice - 1]]
        display_time_in_timezone(timezone)


if __name__ == "__main__":
    main()
