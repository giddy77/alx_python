""" we import the base class"""
from .base import Base

class Rectangle(Base):
    """this is definition of class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """here we have the constructor of the Rectangle Class"""
        self.__width = self.__validate_integer_positive("width", width)
        self.__height = self.__validate_integer_positive("height", height)
        self.__x = self.__validate_integer_nonnegative("x", x)
        self.__y = self.__validate_integer_nonnegative("y", y)
        
        

