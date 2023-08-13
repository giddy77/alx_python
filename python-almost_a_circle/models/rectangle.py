from models.base import Base

class Rectangle(Base):
    """
    A class representing a rectangle.
    Inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int, optional): The x-coordinate of the top-left corner. Default is 0.
        - y (int, optional): The y-coordinate of the top-left corner. Default is 0.
        - id (int, optional): An identifier for the rectangle. Default is None.
        """
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if isinstance(value, int) and value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive integer")

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if isinstance(value, int) and value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive integer")

    @property
    def x(self):
        """Get the x-coordinate of the top-left corner."""
        return self._x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the top-left corner."""
        if isinstance(value, int):
            self._x = value
        else:
            raise ValueError("X must be an integer")

    @property
    def y(self):
        """Get the y-coordinate of the top-left corner."""
        return self._y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the top-left corner."""
        if isinstance(value, int):
            self._y = value
        else:
            raise ValueError("Y must be an integer")

    def area(self):
        """Calculate the area of the rectangle."""
        return self._width * self._height

    def display(self):
        """
        Display a visual representation of the rectangle.
        The rectangle's top-left corner is positioned at (x, y).
        """
        for _ in range(self._y):
            print()
        for _ in range(self._height):
            print(" " * self._x + "#" * self._width)

    def __str__(self):
        """
        Get a string representation of the rectangle.

        Returns:
        A string in the format: "[Rectangle] (id) x/y - width/height"
        """
        return f"[Rectangle] ({self.id}) {self._x}/{self._y} - {self._width}/{self._height}"

# Create an instance of Rectangle with width and height
rectangle_instance = Rectangle(width=10, height=5)

# Call the area method and print the result
print("Area:", rectangle_instance.area())
