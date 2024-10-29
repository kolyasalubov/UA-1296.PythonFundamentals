number = 1986
number_str = str(number)
digit1 = int(number_str[0])
digit2 = int(number_str[1])
digit3 = int(number_str[2])
digit4 = int(number_str[3])

print (f"First number is {digit1}, Second number is {digit2}, Third number is {digit3}, Fourth number is {digit4}")
product_of_digits = digit1 * digit2 * digit3 * digit4
print (f"Product of digits of {number} is {product_of_digits}")

reversed_number = int(number_str[::-1])
print(f"Reversed number of {number} is {reversed_number}")

sorted_digits = sorted(number_str)
sorted_string = "".join(sorted_digits)
sorted_number = int(sorted_string)
print(f"Digits of the number {number} in ascending order:{sorted_number}")
