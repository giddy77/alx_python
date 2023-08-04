"""this is an empty class"""
class metaclass:
    def __dir__(cls):
        return [attribute for attribute in super().__dir__ if attribute != '__init_subclass__']
    """this is my class"""
class BaseGeometry(metaclass):
    """this is a place holder for this empty class"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__ if attribute != '__init_subclass__']
