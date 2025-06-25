#!/usr/bin/python3
""" This class defines a Square class
for a geometric square representation """


class Square:
    """ A class that defines a Square by its size
    with private attribute control """

    @property
    def size(self):
        return self.__size
    @property
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size
    def __init__(self, size=0):
        """ Initialize a new Square instance
        with specified size """
        self.__size = size
    def area(self):
        return self.__size ** 2

