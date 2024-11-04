n = int(input("Введіть кількість чисел у списку: "))

integer_list = []

for i in range(n):
    number = int(input(f"Введіть ціле число номер {i + 1}: "))
    integer_list.append(number)

float_list = []
for num in integer_list:
    float_list.append(float(num))

print("Список з цілими числами:", integer_list)
print("Список з числами з плаваючою точкою:", float_list)
