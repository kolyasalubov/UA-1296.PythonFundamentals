import math


def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Calculates the area of a rectangle

    Parameters:
    width float: Rectangle width
    height float: Rectangle height

    Returns:
    float: Rectangle area
    """
    return width * height


def calculate_triangle_area(base: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Parameters:
    base (float): The base length of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The calculated area of the triangle.
    """
    return base * height * 0.5


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle

    Parameters:
    radius (float): The radius of the circle

    Returns:
    float: The calculated area of the circle
    """
    return math.pow(radius, 2) * math.pi
