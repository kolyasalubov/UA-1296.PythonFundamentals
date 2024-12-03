import re

def passw_valid(symbols):
    if len(symbols) < 6 or len(symbols) > 16:
        return "Enter from 6-16 characters"
    if not re.search(r"[a-z]", symbols):
        return "Enter at least one lowercase letter a-z"
    if not re.search(r"[A-Z]", symbols):
        return "Enter at least one uppercase letter A-Z"
    if not re.search(r"[0-9]", symbols):
        return "Enter at least one digit 0-9"
    if not re.search(r"[$#@]", symbols):
        return "Enter at least one character from: $ # @"
    return "Password is valid"

passw = input("Please enter your password ")

result = passw_valid(passw)
print(result)


    
