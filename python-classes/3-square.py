#!/usr/bin/python3
""" This class defines a Square class
for a geometric square representation """


class Square:
    """ A class that defines a Square by its size
    with private attribute control """

    def __init__(self, size=0):
        """ Initialize a new Square instance
        with specified size """
        self.__size = size

    @property
    def size(self):
        """ Get the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the with validation """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    def area(self):
        """ Calculate and return the area of the square """
        return self.__size ** 2
