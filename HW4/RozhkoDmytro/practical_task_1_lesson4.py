ABSOLUTE_ZERO_C = -273.15
CONVERSION_COEFFICIENT = 9 / 5
FREEZING_POINT_F = 32


def get_numbr(prompt):
    while True:
        num = input(prompt)
        try:
            num = float(num)
            return num
        except ValueError:
            print("Please enter a valid number.")


celsius = float(get_numbr("Enter the temperature in Celsius: "))

if celsius < ABSOLUTE_ZERO_C:
    print(f"Error: Temperature cannot be below absolute zero ({ABSOLUTE_ZERO_C}°C).")
else:
    fahrenheit = (celsius * CONVERSION_COEFFICIENT) + FREEZING_POINT_F
    print(f"{celsius:.2f}°C is equivalent to {fahrenheit:.2f}°F")
