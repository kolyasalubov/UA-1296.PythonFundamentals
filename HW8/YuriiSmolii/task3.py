import area_calculator_methods


def calculate_shape_area() -> str:
    """
    The function gets user parameters and return sahpe area.

    Returns:
    str: The calculated area of the circle
    """
    shape = input("Chouse a shape(rectangle, triangle, circle): ").lower()

    if shape == "rectangle":
        width = input("Enter width: ")
        height = input("Enter height: ")
        if (
            width.replace(".", "", 1).isdigit()
            and height.replace(".", "", 1).isdigit()
            and float(width) > 0
            and float(height) > 0
        ):
            return f"The rectangle area is {area_calculator_methods.calculate_rectangle_area(width=float(width), height=float(height))}"
        else:
            return "Entered parameters are incorrect"

    elif shape == "triangle":
        base = input("Enter base: ")
        height = input("Enter height: ")
        if (
            base.replace(".", "", 1).isdigit()
            and height.replace(".", "", 1).isdigit()
            and float(base) > 0
            and float(height) > 0
        ):
            return f"The triangle area is {area_calculator_methods.calculate_triangle_area(base=float(base), height=float(height))}"
        else:
            return "Entered parameters are incorrect"

    elif shape == "circle":
        radius = input("Enter radius: ")
        if radius.replace(".", "", 1).isdigit() and float(radius) > 0:
            return f"The circle area is {area_calculator_methods.calculate_circle_area(radius=float(radius))}"
        else:
            return "Entred radius is incorrect"
    else:
        return "You shoud chouse correct shape (rectangle, triangle, circle)"

if __name__ == "__main__":
  print(calculate_shape_area())
