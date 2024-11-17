numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_divisible_by_2 = []
odd_numbers_divisible_by_3 = []
numbers_not_divisible_by_2_3 = []

for number in numbers:
    if number % 2 == 0:
        even_numbers_divisible_by_2.append(number)
    if number % 2 != 0 and number % 3 == 0:  
        odd_numbers_divisible_by_3.append(number)
    if number % 2 != 0 and number % 3 != 0:  
        numbers_not_divisible_by_2_3.append(number)

print("Even numbers divisible by 2:", even_numbers_divisible_by_2)
print("Odd numbers divisible by 3:", odd_numbers_divisible_by_3)
print("Numbers not divisible by 2 or 3:", numbers_not_divisible_by_2_3)
