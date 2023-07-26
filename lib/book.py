#!/usr/bin/env python3

class Book:
    # __init__ is a constructor: it is automatically called when an object if the class is created. 
    def __init__(self, title, page_count):
        self.title = title 
        # Initializes the private attribute '__page_count to none. 
        # Private attributes are only available to the class that instantiated them.
        # The double underscores before the attribute name indicate that it is a sprivate attribute. 
        self.__page_count = None 
        self.page_count = page_count
 
    # The property getter defines a getter method for the page_count attribute. It allows us to access the value of the private attribute __page_count like a regular attribute without directly accessing it.
    @property 
    def page_count(self): 
        return self.__page_count
    
    # The @page_count.setter decorator defines a setter method for the page_count attribute. It allows us to set the value of the private attribute __page_count through the page_count attribute. The setter performs a check to ensure that the value being set is an integer. If it's not an integer, it prints a message indicating that page_count must be an integer. Otherwise, it sets the value of __page_count.
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self.__page_count = value 

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    


# Dot notation is often used for piblic attibutes, while setter/getter methods are preferred for private attributes. 


