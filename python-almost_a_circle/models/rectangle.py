"""this the module"""
from models.base import Base

class Rectangle(Base):
    """class base"""
    def init(self, width, height, x=0, y=0, id=None):
        """intialization"""
        super().init(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if isinstance(value, int) and value > 0:
            self.width = value
        else:
            raise ValueError("Width must be a positive integer")

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value > 0:
            self.height = value
        else:
            raise ValueError("Height must be a positive integer")

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            self.x = value
        else:
            raise ValueError("X must be an integer")

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            self.y = value
        else:
            raise ValueError("Y must be an integer")

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.__y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def str(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.__height}"