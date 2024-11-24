import random


class Employee:
    total_employees = 0

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

        Employee.total_employees += 1

    @classmethod
    def total_count(cls):
        print(f"Total count: {cls.total_employees}")

    def employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary:,.2f}")


def generate_name(length=6):
    """Procedurally generates a name with the given length."""
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    name = ""
    for i in range(length):
        if i % 2 == 0:
            name += random.choice(consonants)
        else:
            name += random.choice(vowels)
    return name.capitalize()


for i in range(random.randint(1, 15)):
    name = generate_name(random.randint(3, 10))
    salary = random.randint(5000, 1000000)
    emp_temp = Employee(name, salary)
    emp_temp.employee_info()


Employee.total_count()

# Displaying information about the Employee class
print(f"Base classes of Employee: {Employee.__bases__}")  # _base_
print(f"Employee class namespace: {Employee.__dict__}")  # _dict_
print(f"Employee class name: {Employee.__name__}")  # _name_
print(f"Module where Employee is defined: {Employee.__module__}")  # _module_
print(f"Employee class documentation: {Employee.__doc__}")  # _doc_
