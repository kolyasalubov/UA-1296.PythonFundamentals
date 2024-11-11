num = int(input("Enter number: "))
result = 1

if num == 0:
    print(f"0! = {result}")
elif num > 0:
    for i in range(1, num + 1):
        result = result * i
        i = i + 1
    print(f"{num}! = {result}")    
else:
    print("Invalid number")



