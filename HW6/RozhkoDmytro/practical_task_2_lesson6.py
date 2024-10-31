LOGIN = "First"


def get_valid_login():
    is_valid = False
    while not is_valid:
        user_login = input("Input login:")
        is_valid = user_login == LOGIN

        if not is_valid:
            print("Error: please enter a valid login.")
    else:
        print("Greetings!")


get_valid_login()
