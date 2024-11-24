from modules import *

user_object = str(input("Enter what shape you want to calculate: "))

if user_object == "rectangle":
    rectangle_lenght = float(input("Enter the lenght of your rectangle: "))
    rectangle_height = float(input("Enter the height of your rectangle: "))
    rectangle_area(rectangle_lenght, rectangle_height)

if user_object == "triangle":
    triangle_base = float(input("Enter base of your triangle:"))
    triangle_height = float(input("Enter height of your triangle:"))
    triangle_area(triangle_base, triangle_height)

if user_object == "circle":
    circle_radius = float(input("Enter the radius of your circle: "))
    circle_area(circle_radius)

