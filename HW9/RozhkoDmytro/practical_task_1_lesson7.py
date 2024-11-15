from random import randint

MIN_NUMBER = 0
MAX_NUMBER = 100
MAX_TRY = 10


def get_valid_number(prompt: str) -> int:
    while True:
        user_input = input(f"{prompt}: ")
        try:
            num = int(user_input)
            if MAX_NUMBER < num < MIN_NUMBER:
                print(
                    f"Number can't be less than {MIN_NUMBER} or more than {MAX_NUMBER}."
                    f"Please enter a valid number."
                )
            else:
                return num
        except ValueError:
            print(f"Please enter a valid integer for {prompt}.")


number = randint(MIN_NUMBER, MAX_NUMBER)

current_try = 0
while current_try < MAX_TRY:
    match get_valid_number(f"Guess {MAX_NUMBER} < number < {MIN_NUMBER} "):
        case x if x < number:
            print(f"try [{current_try+1}]: my number is more stronger!")
        case x if x > number:
            print(f"try [{current_try+1}]: my number is smaller than your")
        case _:
            print("You win!")
            break
    current_try += 1
else:
    print("You lose!")
