import geometry

def main():
    print("Choose the figure to calculate the area: ")
    print("1. Rectangle ")
    print("2. Triangle ")
    print("3. Circle ")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        a = float(input("Enter the lemgth of side a: "))
        b = float(input("Emter the length of side b: "))
        area = geometry.rectangle_area (a,b)
        print(f"The area of the rectangle is {area:.2f}")
    elif choice == "2":
        h = float(input("Enter the height: "))
        a = float(input("Enter the base: "))
        area = geometry.triangle_area(h, a)
        print(f"The area of the triangle is {area:.2f}")
    elif choice == "3":
        r = float(input("Enter the radius: "))
        area = geometry.circle_area(r)
        print(f"The area of the circle is {area:.2f}")
    else:
        print("Invalid choice! Please try again.")
if __name__== "__main__":
    main()
