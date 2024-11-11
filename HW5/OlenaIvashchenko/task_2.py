# Task 2

user_number = int(input("Enter a limit for the Fibonacci sequence: "))
fibonacci_list = []

value = 0
next_value = 1

while value <= user_number:
    fibonacci_list.append(value)
    previous_value = value
    value = next_value
    next_value = previous_value + value

print(fibonacci_list)