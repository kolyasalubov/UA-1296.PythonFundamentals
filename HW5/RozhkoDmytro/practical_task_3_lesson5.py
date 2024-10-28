def get_valid_number(prompt):
    while True:
        user_input = input(f"Input {prompt}: ")
        try:
            num = int(user_input)
            if num <= 0:
                print(f"Number can't be less than 0. Please enter a valid number.")
            else:
                return num
        except ValueError:
            print(f"Please enter a valid integer for {prompt}.")


len = get_valid_number("N")

f = 1
for num in range(1, len + 1):
    f *= num

print(f)
