"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = "Ralph Vitug"
__version__ = "ISD.1.0.0"

import unittest
from library_item.library_item import LibraryItem
from genre.genre import Genre

class TestClient(unittest.TestCase): # initializing class of testclient

    def setUp(self):
        # runs before test to reduce code redundancy
        self.library = LibraryItem("ISD", "Michael", Genre.FANTASY, True, 1234)

    def test_init_valid(self): 
        # Arrange & Act
        library = LibraryItem("ISD", "Michael", Genre.FANTASY, True, 1234) # object attributes

        # Assert
        self.assertEqual("ISD", library._LibraryItem__title) # testing validity of title
        self.assertEqual("Michael", library._LibraryItem__author) # testing validity of author
        self.assertEqual(Genre.FANTASY, library._LibraryItem__genre) # testing validity of genre


    def test_init_title_blank_raises_exception(self): # unit test to check title
        # Arrange & Act
        with self.assertRaises(ValueError):
            library = LibraryItem(" ", "Michael", Genre.FANTASY, True, 1234 )

    def test_init_author_blank_raises_exception(self): # unit test to check author
        # Arrange & Act
        with self.assertRaises(ValueError):
            library = LibraryItem("ISD", " ", Genre.FANTASY, True, 1234)

    def test_init_genre_invalid_raises_exception(self): # unit test to check genre
        # Arrange & Act
        with self.assertRaises(ValueError):
            library = LibraryItem("ISD", "Michael", 2, True, 1234)
    
    def test_init_is_borrowed_blank_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            library = LibraryItem("ISD", "Michael", Genre.FANTASY, " ", 1234)
    
    def test_init_item_id_invalid_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            library = LibraryItem("ISD", "Michael", Genre.NON_FICTION, True, "hello")

    def test_title_accessor(self):
        # Arrange is setUp
        # Act & Assert
        self.assertEqual("ISD", self.library.title)

    def test_author_accessor(self):
        # Arrange is setUp
        # Act & Assert
        self.assertEqual("Michael", self.library.author)

    def test_genre_accessor(self):
        # Arrange & Act is setUp
        # Act & assert
        self.assertEqual(Genre.FANTASY, self.library.genre)

    def test_is_borrowed_accessor(self):
        # Arrange & Act is setUp
        # Act and assert
        self.assertEqual(True, self.library.is_borrowed)

    def test_item_id_accessor(self):
        # Arrange & Act is setUp
        # Act and assert
        self.assertEqual(1234, self.library.item_id)