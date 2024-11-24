from math import (pow, pi)



def rectangle_area(lenght:float, height:float) -> float :
    print(lenght * height)

def triangle_area(base: float, height: float) -> float:
    print(base * height * 0.5)

def circle_area(radius: float) -> float:
    print(pi * pow(radius, 2))