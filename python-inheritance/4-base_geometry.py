"""this is an empty class"""
"""this is my class"""
class BaseGeometry(metaclass = metaclassbase):
    """this is a place holder for this empty class"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    
    def area(self):
        raise Exception("area() is not implemented")
    
bg = BaseGeometry()
print(dir(bg))