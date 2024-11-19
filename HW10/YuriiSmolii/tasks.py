# Task 1
class Polygon:
    def __init__(self, no_of_sides):
        self.n  = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n): print("Side",i+1,"is",self.sides[i])


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findArea(self):
        a, b = self.sides
        if a > 0 and b > 0:
            print(f"The area of rectangle is {a * b}")
        else:
            print(f"The rectangle sides coud not be equel 0")


class Triangle(Polygon): 
    def __init__(self):
        super().__init__(3) 
    
    def findArea(self): 
        a, b, c = self.sides 
        if not (a + b > c and b + c > a and c + a > b):
            print("Entered sides do not form a valid triangle")
            return
        s = (a + b + c) / 2 
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
        print('The area of the triangle is %0.2f' %area)
print("--- Rectangle ---")
rectangle = Rectangle()
rectangle.inputSides()
rectangle.findArea()
print("--- Triangle ---")
triangle = Triangle()
triangle.inputSides()
triangle.findArea()

# Task 2

# class Human:
#     species = "Homosapiens"
#     def __init__(self, name) -> None:
#         self.name = name

#     def welcome(self):
#         print(f"Hello {self.name}")

#     @classmethod
#     def get_species(cls):
#         return cls.species

#     @staticmethod
#     def arbitrary_message():
#         return "static method that returns an arbitrary message"

# joi = Human("Joi")
# joi.welcome()
# print(joi.get_species())
# print(Human.get_species())
# print(joi.arbitrary_message())
# print(Human.arbitrary_message())

# Task 3


# class Employee:
#     """Represents an employee data"""

#     counter = 0

#     def __init__(self, name: str, salary: float) -> None:
#         """
#         Initialize an Employee object

#         Parameters:
#         name (str): The name of the employee.
#         salary (float): The salary of the employee.
#         """
#         self.name = name
#         self.salary = salary
#         Employee.counter += 1

#     @classmethod
#     def employee_count(cls) -> int:
#         """
#         Returns the total number of Employee instances

#         Returns:
#         int: Total number of employees
#         """
#         return cls.counter

#     def get_employee_data(self) -> str:
#         """
#         Returns the employee's data

#         Returns:
#         str: A string containing the employee's name and salary.
#         """
#         return f"Name: {self.name} \nSalary: {self.salary}"


# employee_rick = Employee("Rick", 25000)
# print(employee_rick.get_employee_data())
# print(f"Employee count {employee_rick.counter}\n")

# employee_morty = Employee("Morty", 20000)
# print(employee_morty.get_employee_data())
# print(f"Employee count {employee_rick.counter}\n")

# print(f"Base class: {Employee.__base__}\n")

# print(f"Class namespace: {Employee.__dict__}\n")

# print(f"Class name: {Employee.__name__}\n")

# print(f"Module name: {Employee.__module__}\n")

# print(f"Documentation: {Employee.__doc__}\n")
