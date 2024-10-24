from functools import reduce

FOUR_DIGIT_NATURAL_NUMBER = 72934
natural_number_string_list = list(str(FOUR_DIGIT_NATURAL_NUMBER))

# Task 2.1
print(
    f"The product of the digits of {FOUR_DIGIT_NATURAL_NUMBER} is {reduce(lambda x, y: int(x) * int(y), natural_number_string_list)}"
)
##################################################################################################

# Task 2.2
natural_number_string = str(FOUR_DIGIT_NATURAL_NUMBER)
print(f"Reverse {FOUR_DIGIT_NATURAL_NUMBER} is {int(natural_number_string[::-1])}")
##################################################################################################

# Task 2.3
natural_number_string_list.sort()
print(f"Sorted digits: {int(''.join(natural_number_string_list))}")

##################################################################################################

# Task 3
a = 4
b = 5
print("Before interchange values")
print(f"a = {a}, b = {b}")
a, b = b, a
print("After interchange values")
print(f"a = {a}, b = {b}")

c = 6
k = 8
print("Before interchange values:")
print(f"c = {c}, k = {k}")
[c, k] = [k, c]
print("After interchange values:")
print(f"c = {c}, k = {k}")
