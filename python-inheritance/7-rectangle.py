"""this is an empty class"""
class BaseGeometry:
    """this is a place holder for this empty class"""
    
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise Exception(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")



class Rectangle(BaseGeometry):
    """this is  a class that inherits from the BaseGeometry Class"""
    def __init__(self, width, hieght):
        self.__width = width
        self.__hieght = hieght
        
        self.integer_validator("width", width)
        self.integer_validator("hieght", hieght)
        
        
    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"