#!/usr/bin/python3
""" This module defines a Square class 
for a geometric square representation """


class Square:
    """ This class is a sample structure 
    for the object that will be created based on itself """
    
    def __init__(self, size=0):
        """ This is a constructor that is created
        in order to assign values to generated objects """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size ** 2
