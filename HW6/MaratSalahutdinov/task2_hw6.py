expected_login = "First"

while True: 
    user_input = input("Enter your login: ")
    if user_input == expected_login:
        print("Login successful")
        break
    else:
        print("Wrong login. Please try again")
        continue