num1 = 1
num2 = 1

n = int(input("n = "))

print(num1, num2, end=' ')

while n > 2 :
    num1, num2 = num2, num1 + num2 
    print(num2, end= ' ')
    n -= 1