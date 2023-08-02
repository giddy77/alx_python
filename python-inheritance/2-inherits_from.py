"""function that returns True if the object is an 
instance of a class that inherited (directly or indirectly) from the specified class ;"""
def inherits_from(obj, a_class):
    """checks whether the object is an nstance of the class and whether is
    a subclass and the obj is not an instance of the class itself"""
    return isinstance(obj, a_class) and issubclass(type(obj), a_class) and type(obj) != a_class