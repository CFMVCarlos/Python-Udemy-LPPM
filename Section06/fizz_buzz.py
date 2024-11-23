def fizz_buzz(number: int) -> str:
    """
    Return 'Fizz' if `number` is divisible by 3, 'Buzz' if divisible by 5, 'FizzBuzz' if divisible by 3 and 5,
    or the number itself if none of the above.
    
    Args:
        number (int): The number to check
    
    Returns:
        str: The result of the FizzBuzz game
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)

def main():
    # Test the function
    # for i in range(1, 101):
    #     print(fizz_buzz(i))

    input("Play FizzBuzz. Press ENTER to start")
    print()

    next_number = 0
    while next_number  < 99:
        next_number += 1
        print(fizz_buzz(next_number))
        next_number += 1
        correct_answer = fizz_buzz(next_number)
        player_answer = input("Your go: ")
        if player_answer != correct_answer:
            print(f"You lose, the correct answer was {correct_answer}")
            break
    else:
        print("Well done, you reached 100")
        



if __name__ == '__main__':
    main()