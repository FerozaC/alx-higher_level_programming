#!/usr/bin/python3
"""Rectangle component"""


class Rectangle:
    """Rectangle class with width and height attributes"""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the rectangle perimeter."""
        return 2 * (self.__width + self.__height)


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(f"Width: {rect.width}, Height: {rect.height}")
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
