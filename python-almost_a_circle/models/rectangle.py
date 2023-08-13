from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # Use __init__ instead of init
        self._width = width   # Use private attribute names to avoid naming conflicts
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, int) and value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive integer")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive integer")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            self._x = value
        else:
            raise ValueError("X must be an integer")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            self._y = value
        else:
            raise ValueError("Y must be an integer")

    def area(self):
        return self._width * self._height

    def display(self):
        for _ in range(self._y):
            print()
        for _ in range(self._height):
            print(" " * self._x + "#" * self._width)

    def __str__(self):  # Use __str__ instead of str
        return f"[Rectangle] ({self.id}) {self._x}/{self._y} - {self._width}/{self._height}"
