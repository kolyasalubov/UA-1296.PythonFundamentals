user_number = int(input("Enter the temperature in  Celsius: "))

def checker(valid_number):    
    if valid_number < -273.15:
        print("Error: Temperature below absolute zero (-273.15)")
    else:
        F = (valid_number * 9/5) + 32              
        print(f"{valid_number}°С is equivalent to {int(F)}°F")

checker(user_number)
    


