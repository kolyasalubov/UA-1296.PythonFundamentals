choice = int(input("Choose a figure: 1 - rectangle, 2 - triangle, 3 - circle "))

def rectangle():
    if choice == 1:
        num1 = float(input("Enter the length of the 1-st side of the rectangle "))
        num2 = float(input("Enter the length of the 2-nd side of the rectangle "))
        s_rect = num1 * num2
        print("Area of a your rectangle is", s_rect)
rectangle()

def triangle():
    if choice == 2:
        num1 = float(input("Enter a side of the triangle "))
        num2 = float(input("Enter the height on this side "))
        s_trian = (num1 * num2) / 2
        print("Area of a your triangle is", s_trian)
triangle()

def circle():
    if choice == 3:
        num1 = float(input("Enter the radius of the circle "))
        s_cir = num1 ** 2 * 3.14
        print("Area of a your circle is", s_cir)
circle()

if choice not in (1, 2, 3):
    print("Enter only 1, 2, 3 ")



#########################################################
# with cycle for turning

# while True:
#     choice = int(input("Choose a figure: 1 - rectangle, 2 - triangle, 3 - circle or 0 to exit "))

#     def rectangle():
#         if choice == 1:
#             num1 = float(input("Enter the length of the 1-st side of the rectangle "))
#             num2 = float(input("Enter the length of the 2-nd side of the rectangle "))
#             s = num1 * num2
#             print("Area of a your rectangle is", s)
#     rectangle()

#     def triangle():
#         if choice == 2:
#             num1 = float(input("Enter a side of the triangle "))
#             num2 = float(input("Enter the height on this side "))
#             s = (num1 * num2) / 2
#             print("Area of a your triangle is", s)
#     triangle()

#     def circle():
#         if choice == 3:
#             num1 = float(input("Enter the radius of the circle "))
#             s = num1 ** 2 * 3.14
#             print("Area of a your circle is", s)
#     circle()

#     if choice == 0:
#         print("Good by")
#         break

#     if choice not in (0, 1, 2, 3):
#         print("Enter only 1, 2, 3 or 0 to exit ")




#########################################################
# all in one function

# def area():
    
#     while True:

#         choice = int(input("Choose a figure: 1 - rectangle, 2 - triangle, 3 - circle or 0 to exit "))
#         if choice == 1:
#             num1 = float(input("Enter the length of the 1-st side of the rectangle "))
#             num2 = float(input("Enter the length of the 2-nd side of the rectangle "))
#             s = num1 * num2
#             print("Area of a your rectangle is", s)
        
#         elif choice == 2:
#             num1 = float(input("Enter a side of the triangle "))
#             num2 = float(input("Enter the height on this side "))
#             s = (num1 * num2) / 2
#             print("Area of a your triangle is", s)

#         elif choice == 3:
#             num1 = float(input("Enter the radius of the circle "))
#             s = num1 ** 2 * 3.14
#             print("Area of a your circle is", s)

#         elif choice == 0:
#             print("Good by")
#             break

#         else: 
#             print("Enter only 1, 2, 3 or 0 to exit ")
  
# area()
