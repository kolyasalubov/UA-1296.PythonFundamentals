from math import pow, pi
from input import *

def rectangle():
    if choice == 1:
        num1 = float(input("Enter the length of the 1-st side of the rectangle "))
        num2 = float(input("Enter the length of the 2-nd side of the rectangle "))
        s_rect = num1 * num2
        print("Area of a your rectangle is", s_rect)
rectangle()

def triangle():
    if choice == 2:
        num1 = float(input("Enter a side of the triangle "))
        num2 = float(input("Enter the height on this side "))
        s_trian = (num1 * num2) / 2
        print("Area of a your triangle is", s_trian)
triangle()

def circle():
    if choice == 3:
        num1 = float(input("Enter the radius of the circle "))
        s_cir = pi * pow(num1, 2)
        print("Area of a your circle is", s_cir)
circle()