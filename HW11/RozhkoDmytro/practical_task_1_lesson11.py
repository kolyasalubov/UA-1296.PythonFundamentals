def get_analysis_numerologist(value: str) -> str:

    num = int(value)
    if num < 0:
        raise ValueError("Age shoude be positive!")
    return "Even" if num % 2 == 0 else "Odd"


try:
    ancient_prophecy = get_analysis_numerologist(input("Enter your age:"))
    print("Your age is ", ancient_prophecy)
except ValueError as e:
    print(e)
