import re


def is_valid_password(password: str) -> bool:
    # truly not my, finded +-pattern in the internet, but I know what's going on
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$"
    return bool(re.match(pattern, password))


password = input("Enter your password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")
