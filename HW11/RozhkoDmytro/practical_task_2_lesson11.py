def get_week_day(value: str) -> str:
    num = int(value)
    result = ""
    match num:
        case 1:
            result = "Monday"
        case 2:
            result = "Tuesday"
        case 3:
            result = "Wednesday"
        case 4:
            result = "Thursday"
        case 5:
            result = "Friday"
        case 6:
            result = "Saturday"
        case 7:
            result = "Sunday"
        case _:
            raise ValueError("Number shoude be ∈[1,7]")

    return result


try:
    day = get_week_day(input("Enter day number:"))
    print("Day is ", day)
except ValueError as e:
    print(e)
