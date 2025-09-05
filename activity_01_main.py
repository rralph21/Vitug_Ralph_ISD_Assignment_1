""""
Description: A client program written to verify correctness of 
the activity classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from library_item.library_item import LibraryItem
from genre.genre import Genre

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.
    try: 
        library_item = LibraryItem("ISD", "Michael", Genre.FANTASY, True, 1234)
    except ValueError as e:
        print(e)


    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.
    try:
        print("Title: ", library_item.title)
        print("Author: ", library_item.author)
        print("Genre: ", library_item.genre.name)
        print("Borrowed: ", library_item.is_borrowed)
        print("Item ID: ", library_item.item_id)

    except ValueError as e:
        print(e)
    
    
    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        invalid_item = LibraryItem("ISD", " ", " ", True, 1234)
        print(invalid_item)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()