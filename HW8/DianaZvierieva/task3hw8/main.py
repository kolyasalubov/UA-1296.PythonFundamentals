from modules import *

while True:
    shape_choice = input("Enter the name of the shape:").lower() 

    if shape_choice == "rectangle":
        length = float(input("Enter the length of the rectangle:"))
        width = float(input("Enter the widht of the rectangle:"))
        print("The area of ​​the rectangle in cm² is equal to", rectangle_area(length, width))
        break
    elif shape_choice == "triangle":
        base = float(input("Enter the base of the triangle:"))
        height = float(input("Enter the height of the triangle:"))
        print("The area of ​​the triangle in cm² is equal to", triangle_area(base, height))
        break
    elif shape_choice == "circle":
        radius = float(input("Enter the base of the circle:"))
        print("The area of ​​the circle in cm² is equal to", circle_area(radius))
        break
    else:
        print("Invalid choice, please try again") 