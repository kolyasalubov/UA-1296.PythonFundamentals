n = int(input("Число, факторіал якого будем розраховувать "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факторіал числа {n} дорівнює: {factorial}")
