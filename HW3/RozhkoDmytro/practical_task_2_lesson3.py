MAX_NUMBER = 9999
MIN_NUMBER = 999


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
num_list = list(int(digit) for digit in str(num))

# find the product of the digits of this number
product = 1
for digit in num_list:
    product *= digit

print("Product:", product)

# write the number in reverse order

# Solution 1: num_list.reverse()  ~~~~ o_O ~~~~~
# Solution 2
revers_num = 0
for i in range(len(num_list) - 1, -1, -1):
    revers_num = revers_num * 10 + num_list[i]

print("Number in reverse order:", revers_num)

# in ascending order, you need to sort the numbers included in the given number
num_list.sort()
print("Sorted: ", num_list)
