for num in range(1, 11):
    if num % 2 == 0: 
        print(f"{num} - even, divisible by 2 ")
    elif num % 2 != 0 and num % 3 == 0: 
        print(f"{num} - odd, divisible by 3")
    elif num % 2 != 0 and num % 3 != 0:  
        print(f"{num} - is not divisible by 2 or 3")