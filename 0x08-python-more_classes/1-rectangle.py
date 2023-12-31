#!/usr/bin/python3
"""Rectangle component"""


class Rectangle:
    """Rectangle class with width and height attributes"""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height."""
        self.__width = width
        self.__height = height

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


if __name__ == "__main__":

    rect = Rectangle()
    print(f"Width: {rect.width}, Height: {rect.height}")
    rect.width = 10
    rect.height = 5
    print(f"Width: {rect.width}, Height: {rect.height}")
