user_choice = input("Enter name of shape: ")  
check_input = isinstance(user_choice, str)

def rectangle_area(length: int, width: int) -> int:
    area = length * width
    return area

def triangle_area(length: int, height: int) -> int:
    area = length * height * 1/2
    return area

def circle_area(radius: int) -> float:
    PI = 3.14
    area = PI * radius**2
    return area  

if check_input is False:
    print("Wrong input")
else:
    if user_choice == "Rectangle":
        length = int(input("Enter lenght: "))
        width = int(input("Enter width: "))
        area = rectangle_area(length, width)
        print(f"Area of rectangle = {area}")

    elif user_choice == "Triangle":
        length = int(input("Enter lenght: "))
        height = int(input("Enter height: "))
        area = triangle_area(length, height)
        print(f"Area of triangle = {area}")

    elif user_choice == "Circle":
        radius = int(input("Enter radius: "))
        area = circle_area(radius)
        print(f"Area of circle = {area}")
    else:
        print("Wrong name of shape")