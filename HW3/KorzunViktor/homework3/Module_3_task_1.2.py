number = input("Enter 4 digit number : ")

product = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])

reverse = number[:: -1]

sorted_digits = list(number)
sorted_digits.sort()
sorted_list = ''.join(sorted_digits)

print( f"""
      
Product of the digits in your number is: {product}
Your number in reverse is: {reverse} 
Your number sorted from lower to higher: {sorted_list}

""" )






