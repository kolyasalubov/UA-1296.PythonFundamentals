
n = int(input("Введіть число до якого будем писать числа Фібоначчі "))

fib_list = []

fib_sequence = [0, 1]

while True:
    next_fib = fib_sequence[-1] + fib_sequence[-2]
    if next_fib > n:
        break
    fib_sequence.append(next_fib)

print("Числа Фібоначчі до", n, ":", fib_sequence)
