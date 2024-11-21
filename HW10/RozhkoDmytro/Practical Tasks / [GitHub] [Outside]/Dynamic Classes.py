import re


def is_valid(name):
    pattern = r"^[A-Z][a-zA-Z0-9]*$"

    if not re.match(pattern, name):
        raise ValueError(
            "Name must start with an uppercase letter and contain only alphanumeric characters."
        )

    return True


def class_name_changer(cls, new_name):
    if is_valid(new_name):
        cls.__name__ = new_name
