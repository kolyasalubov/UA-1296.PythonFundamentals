x = int(input("Enter the number of Fibonacci terms: "))
a, b = 0, 1

for i in range(x):
    print(a, end=" ")
    a, b = b, a + b