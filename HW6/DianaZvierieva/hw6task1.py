range_list = range(1, 10)

list_divisible2 = [] 
list_divisible3 = [] 
list_notdivisible = []


for item in range_list:
    if item % 2 == 0:
        list_divisible2.append(item)
    elif item % 3 == 0:
        list_divisible3.append(item)
    else:
        list_notdivisible.append(item)

print(f"Even numbers that are divisible by 2: {list_divisible2}\n"
      f"Odd numbers that are divisible by 3: {list_divisible3}\n"
	  f"Numbers that are not divisible by 2 and 3: {list_notdivisible}")