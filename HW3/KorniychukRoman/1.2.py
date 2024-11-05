numbers = (input("Enter 3 digit number:"))

calculations = int(numbers[0]) * int(numbers[1])* int(numbers[2])

reverseList = numbers[::-1]

sortedDigits = list(numbers)
sortedDigits.sort()
sortedList = ''.join(sortedDigits)

print('The product of the digits of number:', calculations)
print('The number in reverse order:', reverseList)
print('Sorted number:', sortedList)
