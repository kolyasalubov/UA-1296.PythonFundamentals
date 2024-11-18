number = int(input("Write the number: "))

def factorial(n):
    result = 1 
    for i in range (1, n + 1):
        result *= i 
    return result 
print("Factorial of a number ", number , "is: ", factorial(number))