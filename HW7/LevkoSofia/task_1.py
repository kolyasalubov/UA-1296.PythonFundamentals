def largest_number(num1, num2):
    """ This function returns the largest number """

    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Values are equal"
    
print(largest_number(2, 2))
