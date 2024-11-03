list_div_2 = [x for x in range(2, 11, 2)]
list_div_3 = [x for x in range(10) if x % 2 == 1 and x % 3 == 0]
list_div_23 = [x for x in range(10) if x % 2 == 1 and x % 3 != 0]

print(
    f"""
Even numbers that are divisible by 2        : {list_div_2}
Odd numbers, which are divisible by 3       : {list_div_3}
Numbers that are not divisible by 2 and 3   : {list_div_23}
"""
)
