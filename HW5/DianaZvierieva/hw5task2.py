n = int(input("Enter number n: "))
a, b = 0, 1

while a <= n:
    print(a, end=" ")
    a, b = b, b + a