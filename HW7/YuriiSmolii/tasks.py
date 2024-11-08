import math

# Task1

# def get_larger_number(num1, num2) -> Union[int, float]:
#     """
#     The function returns the largest of two numbers.

#     Parameters:
#     num1 (int or float): First number to compare
#     num2 (int or float): Second number to compare

#     Returns:
#     int or float: The largest number of two given
#     """
#     return max(num1, num2)


# print(get_larger_number(5, 7))
#########################################################


# Task2
# def calculate_rectangle_area(width: float, height: float) -> float:
#     """
#     Calculates the area of a rectangle

#     Parameters:
#     width float: Rectangle width
#     height float: Rectangle height

#     Returns:
#     float: Rectangle area
#     """
#     return width * height


# def calculate_triangle_area(base: float, height: float) -> float:
#     """
#     Calculate the area of a triangle.

#     Parameters:
#     base (float): The base length of the triangle.
#     height (float): The height of the triangle.

#     Returns:
#     float: The calculated area of the triangle.
#     """
#     return base * height / 2


# def calculate_circle_area(radius: float) -> float:
#     """
#     Calculate the area of a circle

#     Parameters:
#     radius (float): The radius of the circle

#     Returns:
#     float: The calculated area of the circle
#     """
#     return (radius**2) * math.pi


# def calculate_shape_area() -> str:
#     """
#     The function gets user parameters and return sahpe area.

#     Returns:
#     str: The calculated area of the circle
#     """
#     shape = input("Chouse a shape(rectangle, triangle, circle): ").lower()

#     if shape == "rectangle":
#         width = input("Enter width: ")
#         height = input("Enter height: ")
#         if (
#             width.replace(".", "", 1).isdigit()
#             and height.replace(".", "", 1).isdigit()
#             and float(width) > 0
#             and float(height) > 0
#         ):
#             return f"The rectangle area is {calculate_rectangle_area(width=float(width), height=float(height))}"
#         else:
#             return "Entered parameters are incorrect"

#     elif shape == "triangle":
#         base = input("Enter base: ")
#         height = input("Enter height: ")
#         if (
#             base.replace(".", "", 1).isdigit()
#             and height.replace(".", "", 1).isdigit()
#             and float(base) > 0
#             and float(height) > 0
#         ):
#             return f"The triangle area is {calculate_triangle_area(base=float(base), height=float(height))}"
#         else:
#             return "Entered parameters are incorrect"

#     elif shape == "circle":
#         radius = input("Enter radius: ")
#         if radius.replace(".", "", 1).isdigit() and float(radius) > 0:
#             return f"The circle area is {calculate_circle_area(radius=float(radius))}"
#         else:
#             return "Entred radius is incorrect"
#     else:
#         return "You shoud chouse correct shape (rectangle, triangle, circle)"


# print(calculate_shape_area())
#########################################################


# Task3
def calculate_characters(string: str) -> dict[str, int]:
    """
    Calculate a count of each character in the string

    Parameters:
    string (str): The input string to analyze.

    Returns:
    dict[str, int]: A dictionary where each key is a character and the value is its frequency in the string.
    """
    string = string.replace(" ", "")
    return {x: string.count(x) for x in string}


print(calculate_characters("Helloo"))
