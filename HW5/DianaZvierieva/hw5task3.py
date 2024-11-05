#a for loop
b = int(input("Enter number for finding factorial with a for loop: "))
factorial = 1

for a in range(1, b + 1):
    factorial *= a

print(factorial)

#a while loop
b = int(input("Enter number for finding factoria a while loop: "))
factorial = 1
a = 1

while a <= b:
    factorial *= a
    a += 1

print(factorial)