x = int(input("Enter the number of Fibonacci terms: "))
a, b = 0, 1

for f in range(x):
    print(a, end=" ")
    a, b = b, a + b