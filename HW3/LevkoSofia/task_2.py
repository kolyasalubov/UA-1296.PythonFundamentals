
number = 9813

product = int(str(number)[0]) * int(str(number)[1]) * int(str(number)[2]) * int(str(number)[3])

reverse = str(number)[::-1]

sorted_list = list(str(number))
sorted_list.sort()
sorted_number = ''.join(sorted_list)

print(f"Product of digits : {product}")
print(f"Reversed number: {reverse}")
print(f"Sorted number: {sorted_number}")


