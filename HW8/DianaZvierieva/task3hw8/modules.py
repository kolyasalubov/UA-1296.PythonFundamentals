from math import (pi, pow)

def rectangle_area(length: float, width: float) -> float:
    return round(length * width, 2)

def triangle_area(base: float, height: float) -> float:
    return round(0.5 * base * height, 2)

def circle_area(radius: float) -> float:
    return round(pi * pow(radius, 2), 2)