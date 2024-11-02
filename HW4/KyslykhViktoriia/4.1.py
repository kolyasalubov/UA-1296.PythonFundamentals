C = float(input("Enter the temperature in Celsius "))
print(C)
F = (C * 9/5) + 32

if C < -273.15:
    print (C, "Error: Temperature below absolute zero (-273.15°C)")
else:
    print(C, "°C is equivalent to", F, "°F")