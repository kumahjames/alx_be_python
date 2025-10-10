import math

class Shape:
    def area(self):
        """Base method to be overridden by derived classes"""
        raise NotImplementedError("Subclasses must implement area() method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Rectangle class - inherits from Shape"""
        self.length = length
        self.width = width
    
    def area(self):
        """Override area method for rectangle"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Circle class - inherits from Shape"""
        self.radius = radius
    
    def area(self):
        """Override area method for circle"""
        return math.pi * self.radius ** 2