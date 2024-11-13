def controller_password(password): 
    """Validation of password"""
    
    space = (" ")
    if any(x in space for x in password):
         return "Error: Password cannot contain a space."

    if not (6 <= len(password) <= 16):
        return "Error: Password must contain between 6 and 10 characters." 

    if not any(x.isdigit() for x in password):
         return "Error: Password must contain at least one digit."
    
    if not any(x.isupper() for x in password):
         return "Error: Password must contain at least one uppercase letter."
    
    if not any(x.islower() for x in password):
         return "Error: Password must contain at least one  lowercase letter."
    
    special_character = ("$", "#", "@")
    if not any(x in special_character for x in password):
         return "Error: Password must contain at least one special character."
    
    return "Password is valid"