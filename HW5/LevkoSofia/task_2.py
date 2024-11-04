n = int(input("Enter number: "))
first_num = 0
second_num = 1
fibonacci_numbers = [0]

if n == 0:  
    print(fibonacci_numbers)
elif n == 1:  
    fibonacci_numbers.append(1)
    print(fibonacci_numbers)
elif n > 1:
    fibonacci_numbers.append(1)  
    while second_num <= n:  
        num_sum = first_num + second_num
        first_num = second_num
        second_num = num_sum
        
        if second_num <= n: 
            fibonacci_numbers.append(second_num)
    
    print(fibonacci_numbers)
else:
    print("Invalid input")   
