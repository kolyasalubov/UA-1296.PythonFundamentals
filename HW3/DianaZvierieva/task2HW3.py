num = 4529
result = 1

for digit in str(num):
    result *= int(digit)
print(result)

reversed_num = str(num)[::-1]
print(reversed_num)

sort_num = ''.join(sorted(str(num)))
print(sort_num)




