class Polygon:
    def __init__(self, count):
        self.count = count
        self.sides = [0.0 for _ in range(count)]

    def inputSides(self):
        self.sides = [
            self.get_valid_side(f"Enter side {i+1}") for i in range(self.count)
        ]

    def get_valid_side(self, prompt: str) -> float:
        while True:
            user_input = input(f"{prompt}: ")
            try:
                num = abs(float((user_input)))
                return num
            except ValueError:
                print(f"Please enter a valid integer for {prompt}.")


class Rectangle(Polygon):

    def __init__(self, height: float = 0.0, width: float = 0.0):
        super().__init__(4)  # 4 sides
        self.height = abs(float(height))
        self.width = abs(float(width))
        self.sides[0], self.sides[1], self.sides[2], self.sides[3] = (
            height,
            width,
            height,
            width,
        )

    def inputSides(self):
        self.height = self.get_valid_side("Enter the height")
        self.width = self.get_valid_side("Enter the width")
        self.sides = [self.height, self.width] * 2

    def area(self):

        return self.height * self.width


rect = Rectangle()
rect.inputSides()

print(f"Area: {rect.area()}")
