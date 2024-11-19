import math
import random
import re


# Regular Ball Super Ball

class Ball(object):
    def __init__(self, ball_type: str = "regular") -> None:
        self.ball_type = ball_type

# Color Ghost

class Ghost(object):
    def __init__(self):
        self.color = random.choice([ "white", "yellow", "purple", "red"])

# Basic-subclasses-Adam-and-Eve

class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man("Adam"), Woman("Eve")]

# Classy Classes

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
    
# Building Spheres

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(((4 / 3) * math.pi * math.pow(self.radius, 3)), 5)
    
    def get_surface_area(self):
        return round((4 * math.pi * math.pow(self.radius, 2)), 5)
    
    def get_density(self):
        return round((self.mass /((4 / 3) * math.pi * math.pow(self.radius, 3))), 5)
    
# Python's Dynamic Classes #1

def class_name_changer(cls, new_name):
    pattern = r"^[A-Z][a-zA-Z0-9_]*$"
    
    if not re.match(pattern, new_name):
        raise ValueError
        
    name = cls.__name__ = new_name