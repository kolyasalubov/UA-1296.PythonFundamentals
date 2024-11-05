def get_valid_number(prompt):
    while True:
        user_input = input(f"Input {prompt}: ")
        try:
            return int(user_input)
        except ValueError:
            print(f"Please enter a valid integer for {prompt}.")


def input_list():
    list_length = get_valid_number("length of list")
    numbers = []

    if list_length <= 0:
        print("List length should be a positive integer.")
        return []

    for _ in range(list_length):
        numbers.append(get_valid_number("next number"))
    return numbers


my_list = input_list()

for i in range(len(my_list)):
    my_list[i] = float(my_list[i])

print(my_list)
