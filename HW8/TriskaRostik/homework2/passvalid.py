import re

def check(password):
    if len(password)< 6 or len(password) > 60:
        return("Password length must be between 6 and 16 characters")
    if len(password) >= 6 or len(password) <= 60:
        if not re.search(r"[a-z]", password):
            return("Password must contain at least one lowercase letter")
        if not re.search(r"[A-Z]", password):
            return("Password must contain at least one uppercase letter")
        if not re.search(r"[0-9]", password):
            return ("Password must contain at least one digit")
        if not re.search(r"[$#@]", password):
            return ("Password must contain at least one special character ($, #, @).")
    return "Valid password"

def brute(password):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?*^%)&(.~|:;`></$#@"
    attempt = [None] * len(password)
    attempt_count = 0
    
    for i in range(len(password)):
        for char in chars:
            attempt[i] = char
            attempt_count += 1
            if ''.join(attempt[:i + 1]) == password[:i + 1]:
                print(f"Found char '{char}' at pos {i + 1} ")
                break
            elif  attempt_count == 999999999:
                print("Good password")
    if ''.join(attempt) == password:
        print(f"Password: {''.join(attempt)} (Attempts: {attempt_count})")
    else:
        print("Brute failed")

