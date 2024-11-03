celsius = float(input("Enter temperature in C: "))

if celsius < -273.15:
    print("Error: The temperature should be higher than absolute zero (-273.15°C)")
else:
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Temperature {celsius}°C is equal {fahrenheit}°F")
