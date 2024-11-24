# Task 1


# def input_data():
#     """Prompts the user to enter their age and validates the input."""
#     age = int(input("Entered your age: "))
#     if age < 1:
#         raise ValueError(
#             "You entered an incorrect age. Age can't be a negative number or zero."
#         )
#     return age


# def print_age():
#     """Print user age"""
#     try:
#         age = input_data()
#         print(f"Your age is {age}.")
#     except ValueError as e:
#         print(e)


# print_age()


# Task 2


def input_day_number():
    """Prompts the user to enter a day number and returns the corresponding day of the week."""
    
    number = int(input("Enter a day number (1-7): "))
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    if not(0 < number < 8):
        raise ValueError("Number of day can't be less 1 and than 7")

    return days[number]


def print_day_by_number():
    """Gets the day number and prints the corresponding day, handling errors."""
    
    try:
        day = input_day_number()
        print(f"The day corresponding to your input is: {day}")
    except ValueError as e:
        print(e)

print_day_by_number()
