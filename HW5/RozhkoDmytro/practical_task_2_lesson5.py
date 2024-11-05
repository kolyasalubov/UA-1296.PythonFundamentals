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

# Solution 1
a, b = 0, 1
while a <= len:
    print(a, end=" ")
    a, b = b, a + b

print("\n")
# Solution 2
match len:
    case 1:
        print("0")
    case 2:
        print("0 1")
    case _:
        grand = 0
        parent = 1
        print(grand, parent, end=" ")
        for _ in range(2, len):
            grand, parent = parent, grand + parent
            print(parent, end=" ")
