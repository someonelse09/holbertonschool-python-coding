#!/usr/bin/python3
""" This module defines a square class for geometric square representation """


class Square:
    """ This class creates a square class with initializeed size inside of constructor """

    def __init__(self, size=0):
        """ This method allows us to initialize an object based on the structure defined inside of this class """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
