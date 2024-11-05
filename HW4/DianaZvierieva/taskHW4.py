temperature = float(input("Enter the temperature in Celsius:"))

conversion_to_fahrenheit = (temperature * (9 / 5)) + 32

if temperature < -273.15:
    print(f"Error: Temperature below absolute zero ({temperature} °C)")
else:
    print(f"{temperature} °C is equivalent to {conversion_to_fahrenheit} °F")