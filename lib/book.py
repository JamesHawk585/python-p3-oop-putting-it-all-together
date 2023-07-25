#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title 
        self.page_count = page_count 
        page_count = int(page_count)


harry_potter = Book("Harry Potter", 100)

harry_potter.page_count

