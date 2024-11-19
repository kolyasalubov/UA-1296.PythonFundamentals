import re

user_passweord = str(input("Enter your password: "))
valid_passwrd = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$"


if re.match(valid_passwrd, user_passweord):
    print("Your password is good!")
else:
    print("You have a bad password, password need contain one small letter, one upper Letter, digit and (@ # $)")