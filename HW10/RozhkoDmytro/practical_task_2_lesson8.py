import random


class Homosapiens: ...


class Human(Homosapiens):
    def __init__(self, name: str):
        self.name = name

    def display_welcome(self):
        print(f"Hi, {self.name}")

    @classmethod
    def is_Homosapiens(self, obj1):
        return "is Homosapiens" if isinstance(obj1, Homosapiens) else "not Homosapiens"

    @staticmethod
    def get_TIN():
        return "".join(random.choices("0123456789", k=11))


person = Human("Dima")
print("Object", Human.is_Homosapiens(person))
print("TIN =", person.get_TIN())
