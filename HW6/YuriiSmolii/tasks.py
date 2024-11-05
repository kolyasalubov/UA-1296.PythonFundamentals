# Task1
range_to_ten = range(1, 11)

print(
    f"""Even numbers that are divisible by 2: 
    {[number for number in range_to_ten if number % 2 == 0]}"""
)
print(
    f"""Odd numbers that are divisible by 3: 
    {[number for number in range_to_ten if number % 2 != 0 and number % 3 == 0]}"""
)
print(
    f"""Numbers that are not divisible by 2 and 3: 
    {[number for number in range_to_ten if number % 2 != 0 and number % 3 != 0]}"""
)

#########################################################################################

# Task2

# while True:
#   login = input("Please enter your login: ")
#   if login != "First":
#     print("Login is incorrect. Please try again")
#     continue
#   else:
#     print("Login is correct")
#     break
