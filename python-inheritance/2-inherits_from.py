def inherits_from(obj, a_class):
    """
    Checks whether the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """
    return isinstance(obj, type) or issubclass(type(obj), a_class) and type(obj) != a_class
