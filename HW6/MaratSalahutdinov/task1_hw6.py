user_input = input("Enter comma-separated list items from 1 to 10 : ")

user_list = [item.strip() for item in user_input.split(',')]

print("Your list: ", user_list)

try:
    user_list = [int(item) for item in user_list if 1 <= int(item) <= 10]
except ValueError:
    print("Invalid input. Please enter only numbers from 1 to 10.")
    user_list = []

div_by_2 = []
div_by_3 = []
not_div_by_2_and_3 = []

for num in user_list:
    if num % 2 == 0:
        div_by_2.append(num)
    elif num % 3 == 0:
        div_by_3.append(num)
    else:
        not_div_by_2_and_3.append(num)

print("Even numbers that are divisible by 2: ", div_by_2 )
print("Odd numbers that are divisible by 3: ", div_by_3 )
print("Numbers that are not divisible by 2 and 3: ", not_div_by_2_and_3 )