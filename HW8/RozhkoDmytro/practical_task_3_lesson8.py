import math


def area_circle(r: float) -> float:
    if r < 0:
        print("Radius can't be a negative")
        return None
    return math.pi * math.pow(r, 2)


def area_rectangle(a: float, b: float) -> float:
    if a < 0 or b < 0:
        print("Values can't be a negative")
    return a * b


def area_triangle(h: float, a: float) -> float:
    return (h * a) / 2


def get_valid_number(prompt) -> float:
    while True:
        user_input = input(f"Input {prompt}: ")
        try:
            num = float(user_input)
            if num < 0:
                print(f"Number can't be less than 0. Please enter a valid number.")
            else:
                return num
        except ValueError:
            print(f"Please enter a valid integer for {prompt}.")


choice = input(
    f"Set type of area :\n"
    f"1 - circle area \n"
    f"2 - rectangle area \n"
    f"3 - triangle area \n"
)

area = None
match choice:
    case "1":
        area = area_circle(get_valid_number("radius: "))
    case "2":
        area = area_rectangle(get_valid_number("a: "), get_valid_number("b: "))
    case "3":
        area = area_triangle(get_valid_number("h: "), get_valid_number("a: "))
    case _:
        print("Bad choise!")

print(f"Area = {area:.2f}")
