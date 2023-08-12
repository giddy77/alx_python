""" we import the base class"""
from .base import Base

class Rectangle(Base):
    """this is definition of class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """here we have the constructor of the Rectangle Class"""
        self.__width = width
        self.__height =height
        self.__x = x
        self.__y = y
        
        

        
   
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
        
        


    def create(cls, width, height):
        """Create a new Rectangle instance with only width and height"""
        return cls(width, height)