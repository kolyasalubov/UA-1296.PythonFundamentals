c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
ABSOLUTE_ZERO = -273.15

if c > ABSOLUTE_ZERO:
    print(f"{c}°С equivalent to {f}°F")
else:
    print(f"Temperature below absolute zero ({ABSOLUTE_ZERO})")

