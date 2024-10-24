def get_valid_number(name_value):
    while True:
        num = input(f"Input number {name_value}:")
        try:
            num = int(num)
            return num
        except ValueError:
            print("Please enter a valid number.")


def reverse(a, b):
    return b, a


# Input
a = get_valid_number("a")
b = get_valid_number("b")

# Solution 1
a, b = b, a

# Output
print("Value a:", a)
print("Value b:", b)


# Solution 2
a, b = b, a

a = a + b
b = a - b
a = a - b

# Output
print("Value a:", a)
print("Value b:", b)

# Solution 3
a, b = b, a

a, b = reverse(a, b)

# Output
print("Value a:", a)
print("Value b:", b)
