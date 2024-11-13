def number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
""" 
Comparing of numbers

"""
userN1 = int(input("Enter the first number:"))
userN2 = int(input("Enter the second number:"))
print('The largest number:', number(userN1, userN2))