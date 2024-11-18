import area_calculator_methods


def get_shape_parameters(shape: str) -> str:
    """
    Prompts the user for the necessary dimensions to calculate the area of the specified shape.
    
    Parameters:
    shape (str): The type of shape for which dimensions are required. Options are "rectangle", "triangle", or "circle".
    
    Returns:
    tuple or str or bool: 
        - For "rectangle", returns a tuple (width, height) if inputs are valid.
        - For "triangle", returns a tuple (base, height) if inputs are valid.
        - For "circle", returns a string representing the radius if input is valid.
        - Returns False if any input is invalid.
    """
    if shape == "rectangle":
        width = input("Enter width: ")
        height = input("Enter height: ")
        if (
            width.replace(".", "", 1).isdigit()
            and height.replace(".", "", 1).isdigit()
            and float(width) > 0
            and float(height) > 0
        ):
            return width, height
        return False
    elif shape == "triangle":
        base = input("Enter base: ")
        height = input("Enter height: ")
        if (
            base.replace(".", "", 1).isdigit()
            and height.replace(".", "", 1).isdigit()
            and float(base) > 0
            and float(height) > 0
        ):
            return base, height
        return False
    elif shape == "circle":
        radius = input("Enter radius: ")
        if radius.replace(".", "", 1).isdigit() and float(radius) > 0:
            return radius
        return False


def calculate_shape_area() -> str:
    """
    The function gets user parameters and return sahpe area.

    Returns:
    str: The calculated area of the circle
    """
    shape = input("Chouse a shape(rectangle, triangle, circle): ").lower()

    if shape == "rectangle":
        parameters = get_shape_parameters("rectangle")
        if parameters:
            return f"The rectangle area is {area_calculator_methods.calculate_rectangle_area(width=float(parameters[0]), height=float(parameters[1]))}"
        else:
            return "Entered parameters are incorrect"

    elif shape == "triangle":
        parameters = get_shape_parameters("triangle")
        if parameters:
            return f"The triangle area is {area_calculator_methods.calculate_triangle_area(base=float(parameters[0]), height=float(parameters[1]))}"
        else:
            return "Entered parameters are incorrect"

    elif shape == "circle":
        parameters = get_shape_parameters("circle")
        if parameters:
            return f"The circle area is {area_calculator_methods.calculate_circle_area(radius=float(parameters))}"
        else:
            return "Entred radius is incorrect"
    else:
        return "You shoud chouse correct shape (rectangle, triangle, circle)"


if __name__ == "__main__":
    print(calculate_shape_area())
