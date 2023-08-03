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
        