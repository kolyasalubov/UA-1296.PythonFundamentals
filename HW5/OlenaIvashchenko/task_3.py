# Task 3

user_number = int(input("Enter number to calculate the factorial: "))
factorial = 1

for number in range(1, user_number + 1):
    factorial *= number

print(f"The factorial of your number '{user_number}' : {factorial}")