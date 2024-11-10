y = int(input('Type a number to calculate the factorial: '))

f = 1  
while y > 0:
    f = f * y 
    y = y - 1  

print('Factorial:', f)
