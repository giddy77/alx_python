# 0-square.py

"""This is a module-level documentation.

This module contains a class called Square, which defines a square by its size.

"""

class Square:
    """Represents a square.

    This class defines a square by its size.

    Attributes:
        __size (int): The size of the square.

    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.

        """
        @property
        def size(self):
            """Get the size of the square.

        Returns:
            int: The size of the square.

        """
            return self.__size

        @size.setter
        def size(self, value):
            """Set the size of the size"""
            """checking whether the value set is an interger"""
            
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            """checks whether the size is greater than 0"""
            if size < 0:
                raise ValueError("size must be >= 0")

            self.__size = size

            def set_size(self):
                """Calculate the area of the square.

          Returns:
            int: The area of the square.

        """
        return self.__size ** 2
