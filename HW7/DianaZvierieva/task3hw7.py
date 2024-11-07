def countCharacter(given_string):
    """"""
    print("Number of character:")
    for character in set(given_string):
        if character == " ":
            continue
        print(character, "-", given_string.count(character), end=", ")

countCharacter("Experience teaches us valuable lessons in life")


