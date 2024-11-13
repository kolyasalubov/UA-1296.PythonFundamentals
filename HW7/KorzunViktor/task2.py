def rectangle_area(length, width):
    print(f'The area of your rectangle is {length * width} cm²')

def triangle_area(side1, side2, side3):
    if side1 + side2 > side3 and side3 + side2 > side1 and side1 + side3 > side2:
        p = (side1 + side2 + side3) / 2
        area = (p * (p-side1) * (p-side2) * (p-side3))**0.5
        print(f'The area of your triangle is {round(area, 2)} cm²')
    else:
        print("Triangle with such sides is impossible")

def circle_area(r):
    print(f'The area of your cirсle is {round((3.14 * r ** 2), 2)} cm²')




while True:
    user_choice = input("Enter what area you want to calculate(rectangle, triangle, circle) : ")

    if user_choice == 'rectangle':
        user_lenght = float(input('Enter the lenght of your rectangle(cm): '))
        user_width = float(input('Enter the width of your rectangle(cm): '))
        rectangle_area(user_lenght, user_width)
        break
    elif user_choice == 'triangle':
        user_side1 = float(input("Enter the first side of your triangle(cm): "))
        user_side2 = float(input("Enter the second side of your triangle(cm): "))
        user_side3 = float(input("Enter the third side of your triangle(cm): "))
        triangle_area(user_side1, user_side2, user_side3)
        break
    elif user_choice == 'circle':
        user_radius = float(input('Enter the radius of your circle(cm): '))
        circle_area(user_radius)
        break
    else:
        print("You enter shape uncorrectly!!!")
        continue