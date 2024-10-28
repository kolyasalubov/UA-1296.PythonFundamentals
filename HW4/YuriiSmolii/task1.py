
def celsius_to_fahrenheit():
    temperature_celsius = int(input("Enter a temperature in Celsius: ").strip())
    ABSOLUTE_ZERO = -273.15
    if temperature_celsius > ABSOLUTE_ZERO:
        print(
            f"{temperature_celsius}{chr(176)}C is equivalent to {round(temperature_celsius * 9 / 5 + 32)}{chr(176)}F"
        )
    else:
        print(f"Error: Temperature below absolute zero ({ABSOLUTE_ZERO}){chr(176)}C")


celsius_to_fahrenheit()
