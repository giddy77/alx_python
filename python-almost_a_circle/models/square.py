# models/square.py"""
from models.rectangle import Rectangle
"""the Square class that inherits from the class rectangle"""
class Square(Rectangle):
    """
    A class representing a square, inheriting from the Rectangle class.

    Attributes:
        size (int): The size of the square (both width and height).
        x (int): The x-coordinate position of the square.
        y (int): The y-coordinate position of the square.
        id (int): The unique identifier. Inherits from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square instance with specified attributes.

        Args:
            size (int): The size of the square (both width and height).
            x (int, optional): The x-coordinate position of the square. Default is 0.
            y (int, optional): The y-coordinate position of the square. Default is 0.
            id (int, optional): The unique identifier. Inherits from Rectangle class.
        """
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """Get the size of the square."""
        return self.width
    
    @size.setter
    def size(self, new_size):
        """Set the size of the square. Validates size."""
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size <= 0:
            raise ValueError("size must be > 0")
        self.width = new_size
        self.height = new_size
    
    def __str__(self):
        """Returns a formatted output for Square."""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
