#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.__size = None
        self.size = size
        self.condition = "old"

    
    @property 
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else: 
            self.__size = value
    
    def cobble(self): 
        self.condition = "New"
        print("Your shoe is as good as new!")


adidas = Shoe("Adidas", 12)

