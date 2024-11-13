# Task 2

valid_login = "First"

while True:
    user_login = input("Enter your login: ")

    if user_login == valid_login:
        print("Hey, user :) \nThank you for joining us! ")
        break
    else:
        print("Error:( \nYou have entered the wrong login. Please, try again!")