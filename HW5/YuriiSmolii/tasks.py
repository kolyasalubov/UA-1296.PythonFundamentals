# Task1
list_of_integers = range(0, 15)


def to_float(intagers_list):
    floats_list = []
    for number in intagers_list:
        floats_list.append(float(number))
    return floats_list


print(list(list_of_integers))
print(to_float(list_of_integers))

############################################

# Task2
# number = int(input("Enter a number to set the limit for the Fibonacci sequence: "))


# def make_fibonacci_sequence(limit):
#     fibonacci_list = []
#     next_value = 1
#     current = 0
#     while current < limit:
#         fibonacci_list.append(current)
#         previous = current
#         current = next_value
#         next_value = previous + current
#     return fibonacci_list


# print(make_fibonacci_sequence(number))

############################################

# Task3
# number = int(input("Enter a number to calculate the factorial: "))


# def calculate_factorial(number):
#     i = 1
#     factorial = 1
#     while i <= number:
#         factorial *= i
#         i += 1
#     return factorial


# print(f"Factorial number {number} is {calculate_factorial(number)}")
