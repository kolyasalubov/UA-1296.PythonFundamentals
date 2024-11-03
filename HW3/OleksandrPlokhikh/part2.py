number = (input("Enter number from 1000 to 9999: "))

product_of_digits = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])

reverse = number[::-1]

sorted_number = sorted(str(number))

print(f"""

The product of digits in your number is {product_of_digits}.
The reserved value of your number is {reverse}.
Your sorted number looks {sorted_number}

""")

