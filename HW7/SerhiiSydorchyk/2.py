def rectangle_area(length, width):
    return length * width
def triangle_area(base, height):
    return 0.5 * base * height
def circle_area(radius):
    pi = 3.14
    return pi * radius ** 2
def main ():
    print("Choose a figure to calculate the area: " )
    print("1 - rectangle")
    print("2 - triangle")
    print("3 - circle")
    choice = int(input("Your choice is (1/2/3): "))

    if choice == 1:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print(f"Rectangle area: {rectangle_area(length,width)}: ")
    elif choice == 2:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print (f"Triangle area: {triangle_area(base, height)}: ")
    elif choice == 3:
        radius = float(input("Enter radius: "))
        print(f"Circule area: {circle_area(radius)}")
    else :
        print("Wrong choice!")
    
main ()


    

