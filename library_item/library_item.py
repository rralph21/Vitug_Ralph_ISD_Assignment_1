""""
Description: A class to manage LibraryItem objects.
"""


__author__ = "Ralph Vitug"
__version__ = "ISD.1.0.0"

from genre.genre import Genre

class LibraryItem:
    """
    Contains items from library

    args:

        title (str): The title of the library item
        author (str): The author of the library item
        genre (Genre): The genre of the library item

    """

    def __init__(self, title: str, author: str, genre: Genre, is_borrowed: bool, item_id: int):

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
        
        if isinstance(is_borrowed, bool): # checks if item is borrowed, boolean value.
            self.__is_borrowed = is_borrowed
        else:
            raise ValueError("Is Borrowed must be a boolean value")

        if isinstance(item_id, int):
            self.__item_id = item_id
        else:
            raise ValueError("Item ID must have numeric value")

      
    @property # defining an accessor
    def title(self) -> str: # made public
        return self.__title
  
    @property # defining an accessor
    def author(self) -> str: # made public
        return self.__author
  
    @property # defining an accessor
    def genre(self) -> Genre:
        return self.__genre # made public
    
    @property # defining an accessor
    def is_borrowed(self) -> bool:
        return self.__is_borrowed
    
    @property # defining an accessor
    def item_id(self) -> int:
        return self.__item_id
     

    def __str__(self) -> str: # prints in string form the title, author and genre.
        return (f"Title: {self.__title}"
        + f"\nAuthor: {self.__author}"
        + f"\nGenre: {self.__genre.name}"
        + f"\nItem ID: {self.__item_id}"
        + f'\nBorrowed: {self.__is_borrowed}')

     
