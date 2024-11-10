x = int(input('Type a number to calculate the factorial: '))

f = 1  
while x > 0:
    f = f * x 
    x = x - 1  

print('Factorial:', f)

