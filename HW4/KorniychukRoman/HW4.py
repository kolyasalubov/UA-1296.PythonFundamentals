temperature = int(input("Enter a temperature: "))
if temperature < -273.15:
    print("Temperature is below absolute zero!")
else:
    print('Converted to Farhenheit:', ((temperature * 9/5)+32))