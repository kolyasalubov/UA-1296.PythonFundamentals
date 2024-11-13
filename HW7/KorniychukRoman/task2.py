def rectangle(side1, side2):
    s1 = side1 * side2
    return s1

def triangle(height, base):
    s2 = 1/2 * height * base
    return s2

def circle(r):
    s3 = 3.14 * r ** 2  
    return s3

a = int(input('Choose figure (rectangle - 1, triangle - 2, circle - 3): '))
if a == 1:
    b = int(input('Enter the first side: '))
    c = int(input('Enter the second side: '))
    print("Rectangle area:", rectangle(b, c))

elif a == 2:
    d = int(input('Enter the height: '))
    e = int(input('Enter the base of the triangle: '))
    print("Triangle area:", triangle(d, e))

elif a == 3:
    x = int(input('Enter the radius: '))
    print("Circle area:", circle(x))

else:
    print('Try again')
