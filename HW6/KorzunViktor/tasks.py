################     1    ###################


# even_by_two =[]
# odd_by_three = []
# numbers_not_divisible = []

# for num in range(1, 10):
#     if num %2 == 0:
#         even_by_two.append(num)
#     elif num % 3 == 0:
#         odd_by_three.append(num)
#     elif num % 2 !=0 and num % 3 != 0:
#         numbers_not_divisible.append(num)

# print(even_by_two)
# print(odd_by_three)
# print(numbers_not_divisible)




################     2    ###################

game = True

while game:
    login = 'First'
    user_login = input("Enter your login: ")
    if user_login != login:
        print("Uncorect login, please enter valid login: ")
    if user_login == login:
        print("You enter correct login!")
        game = False
    



