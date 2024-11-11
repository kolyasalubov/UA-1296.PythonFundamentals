# Task 2

number = 6459
number_str = str(number)

product_of_digits = (
    int(number_str[0]) * int(number_str[1]) * int(number_str[2]) * int(number_str[3])
)

number_reversed = number_str[::-1]

sorted_digits = list(number_str)
sorted_digits.sort()
sorted_list = "".join(sorted_digits)

print(
    f"""
The product of the digits in number '{number}' is {product_of_digits}
Number '{number}' in reverse: {number_reversed}
Number '{number}' sorted from lowest to highest: {sorted_list}
"""
)