def check_login():      
    while True:
        login = input("Enter login: ")
        if login == "First":
            print(f"Hello, {login}")
            break
        else:
            print("Wrong login.")

check_login()
