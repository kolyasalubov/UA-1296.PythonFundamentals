import re


def password_validation(password: str) -> bool:
    """
    Validates the password

    Parameters:
    password (str): The password to be validated

    Returns:
    bool: True if the password is valid, False otherwise
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$"

    if re.match(pattern, password):
        return True
    return False


print(password_validation(input("Enter your password: ")))
