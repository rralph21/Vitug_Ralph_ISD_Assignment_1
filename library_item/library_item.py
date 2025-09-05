""""
Description: A class to manage LibraryItem objects.
"""


__author__ = "Ralph Vitug"
__version__ = "Act.1.0.0"

from genre.genre import Genre

class LibraryItem:
    """
    Contains items from library

    args:

        title (str): name of items
        author (str): name of writer or author
        genre (Genre): type of the item that it belongs to

    """

    def __init__(self, title: str, author: str, genre: Genre):

        if len(title.strip())> 0: # strip any white space from title
            self.__title = title # name mangling
        else:
            raise ValueError("Title cannot be blank") # prints a message if title is blank
        
        if len(author.strip())> 0: # strips any white space from author
            self.__author = author # name mangling
        else:
            raise ValueError("Author cannot be blank") # prints a message if author is blank
        
        if isinstance(genre, Genre): # checks if genre is valid
            self.__genre = genre
        else:
            raise ValueError("Invalid Genre") # prints a message if genre is invalid
        

        

        

