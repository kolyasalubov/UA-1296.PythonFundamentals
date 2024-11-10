from modules import *

while True:
    controller_result = controller_password(input("Enter your password:"))
    if controller_result == "Password is valid":
        print(controller_result)
        break
    else: 
        print(controller_result)   



        
