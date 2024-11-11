n = int(input("Enter the number for calculating factorial: "))
factorial = 1
for i in range (1,n+1):
    factorial *= i
print(f"Factorial of the number{n} =: {factorial}")
