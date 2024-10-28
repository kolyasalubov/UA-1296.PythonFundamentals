MAX_NUMBER = 9999
MIN_NUMBER = 1000


def get_valid_number():
    while True:
        num = input("Input number:")
        try:
            num = int(num)
            if num < MIN_NUMBER or num > MAX_NUMBER:
                print(
                    f"Number can't be more than {MAX_NUMBER} or less than {MIN_NUMBER}. Please enter a valid number."
                )
            else:
                return num
        except ValueError:
            print("Please enter a valid number.")


# Input
num = get_valid_number()

# Convert
digit1 = int(str(num)[0])
digit2 = int(str(num)[1])
digit3 = int(str(num)[2])
digit4 = int(str(num)[3])

# Find the product of the digits of this number
product = digit1 * digit2 * digit3 * digit4
print("Product:", product)

# Write the number in reverse order
revers_num = digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1
print("Number in reverse order:", revers_num)

# Sort
sorted_list = [digit1, digit2, digit3, digit4]
sorted_list = sorted(sorted_list)
print("Sorted: ", sorted_list)
