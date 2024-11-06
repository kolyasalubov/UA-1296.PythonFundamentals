temperature_celcius = float(input("Enter the temperature in Celsius: "))

if temperature_celcius >= -273.15:
    temperature_farenheit = (temperature_celcius * 9 / 5) + 32
    print(
        f"Temrature {temperature_celcius}°C is equivalent to {temperature_farenheit}°F"
    )
else:
    print("Error. Temperature below absolute zero (-273.15°C)")
