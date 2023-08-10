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
        
        

        
   
    def get_width(self):
         """ 
        This the 
        Getter  for width specifies
        the getter method for the Rectangle class
        """
         return self.__width
    
    
    
    def set_width(self, width):
        """setter for width"""
        if width > 0:
            self.__width = width
    
    def get_height(self):
        
        """Getter  for height"""
        return self.__height
    
    def set_height(self, height):
        """setter for width"""
        if height > 0:
            self.__height = height
    
   
    def get_x(self):
        """Getter  for x"""
        return self.__x
    
    def set_x(self, x):
        """setter for x"""
        self.__x = x
    
    
    def get_y(self):
        """Getter for y"""
        return self.__y
    
    def set_y(self, y):
        """setter for y"""
        self.__y = y
        
        

    def __validate_integer_positive(self, name, value):
        """the validator methods are here"""
        if not isinstance(value, int):
            """checks whether the value is an interger"""
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            """checks whether the value is greater than 0"""
            raise ValueError(f"{name} must be > 0")
        return value

    def __validate_integer_nonnegative(self, name, value):
        """this is the nanonegative validator"""
        if not isinstance(value, int):
            """checks whether the value is an interger"""
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            """checks whether the value is greater or equal to 0"""
            raise ValueError(f"{name} must be >= 0")
        return value
"""create an instance of the rectangle class"""  
rectangle_instance = Rectangle()

"""Print the attributes of the rectangle instance"""
print( rectangle_instance.get_width())
print( rectangle_instance.get_height())