#!/usr/bin/python3
""" This class defines a Square class
for a geometric square representation """


class Square:
    """ A class that defines a Square by its size
    with private attribute control """

    def __init__(self, size):
        """ Initialize a new Square instance
        with specified size """
        self.__size = size
