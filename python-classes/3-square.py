class Square:
    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        """checks whether size is greater than zero
        """
        if value < 0:
            raise ValueError("size must be >= 0")
        """_sets the new value of size
        """
        self.__size = value
        
    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
