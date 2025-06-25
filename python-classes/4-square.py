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
        """ This is for getting the value of square's size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of Square with validation """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """ This method returns the area of a square """
        return self.__size ** 2

    def my_print(self):
        """ This method prints the square
        according to given size and using the hash character
        """
        for _ in range(size):
            for _ in range(size):
                print('#', end="")
            print()
