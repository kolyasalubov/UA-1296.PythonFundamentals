import random


def get_user_number(trying: int = 3) -> int:
    """
    Prompts the user to input a valid number with up to 3 retries.

    Parameters:
    trying (int): Number of allowed retries for input validation.

    Returns:
    int: The valid user-entered number owerwithe False
    """
    if trying > 0:
        user_input = input("Please enter a number: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input.  Try again")
            trying -= 1
            return get_user_number(trying)
    return False


def number_game():
    """
    A number guessing game where the user has 10 attempts to guess a random number between 1 and 100.
    """
    target_number = random.randint(1, 101)
    remaining_attempts = 10
    max_invalid_inputs = 3

    print("Welcome to the Number Guessing Game!")
    print("You have 10 attempts to guess the number between 1 and 100.\n")

    while remaining_attempts:
        guessed_number = get_user_number(max_invalid_inputs)
        if not guessed_number:
            print("Game over due to invalid input")
            return

        if guessed_number == target_number:
            print("Congratulations! You guessed the number!")
            return
        elif guessed_number < target_number:
            print("The number is greater than your guess")
        else:
            print("The number is less than your guess")

        remaining_attempts -= 1
        print(f"Remaining attempts: {remaining_attempts}\n")

    print("Sorry, you've used all attempts. Better luck next time!")


number_game()
