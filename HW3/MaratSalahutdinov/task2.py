number = int(input("Write four-digit natural number:  "))

if number > 9999 or number < 1000:
        raise IndexError("Wrong number")

product = 1

for digit in str(number): 
        product = product * int(digit) 
  

print("Добуток числа: ", product)

reversed_number = int(str(number)[:: -1])
print("Перевернуте число: ", reversed_number)

sorted_number = "".join(sorted(str(number)))
print("Відсортоване число: ",sorted_number)

