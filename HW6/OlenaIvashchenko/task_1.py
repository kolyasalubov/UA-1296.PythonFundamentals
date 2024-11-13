# Task 1

numbers_range = range(1, 10)
numbers_divisible2 = []
numbers_divisible3 = []
numbers_notdivisible2_3 = []

for item in numbers_range:
    if item % 2 == 0:
        numbers_divisible2.append(item)
    elif item % 3 == 0:
        numbers_divisible3.append(item)
    else:
        numbers_notdivisible2_3.append(item)

print(
    f"""
List of even numbers that are divisible by 2: {numbers_divisible2}
List of odd numbers that are divisible by 3: {numbers_divisible3}
List of numbers that aren't divisible by 2 and 3: {numbers_notdivisible2_3}
"""
)