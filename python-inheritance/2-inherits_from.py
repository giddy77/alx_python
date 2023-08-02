"""
This module provides a function to check whether an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Checks whether the object is an instance of the specified class or if the object is an instance
    of a class that inherited (directly or indirectly) from the specified class.

    :param obj: The object to check.
    :param a_class: The specified class to compare against.
    :return: True if the object is an instance of a subclass of the specified class; False otherwise.
    """
    return isinstance(obj, type) or issubclass(type(obj), a_class) and type(obj) != a_class
