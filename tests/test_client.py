"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

__author__ = "Ralph Vitug"
__version__ = "ISD.A.1.0.0"


import unittest
from client.client import Client

class TestClient(unittest.TestCase): # initializing class of test client

    def setUp(self):
        # runs before test to reduce code redundancy
        self.client = Client(12345, "Wendy", "Ways", "WendyWays@pixell.com")

    def test_init_valid(self):
        # Arrange & Act
        client = Client(12345, "Wendy", "Ways", "WendyWays@pixell.com")

        # Assert
        self.assertEqual(12345, client._Client__client_number) # testing client number if valid
        self.assertEqual("Wendy", client._Client__first_name) # testing first name if valid
        self.assertEqual("Ways", client._Client__last_name) # testing lst name if valid
        self.assertEqual("WendyWays@pixell.com", client._Client__email_address) # testing email address if valid

    def test_init_client_number_raises_exception(self): # test to check client number
        # Arrange & Act
        with self.assertRaises(ValueError):
            client = Client("hello world", "Wendy", "Ways", "WendyWays@pixell.com")

    def test_init_first_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError): # test to check first name
            client = Client(12345, " ", "Ways", "WendyWays@pixell.com")

    def test_init_last_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError): # test to check last name
            client = Client(12345, "Wendy", " ", "WendyWays@pixell.com")

    def test_init_email_address_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError): # test to check email address
            client = Client(12345, "Wendy", "Ways", "123 ")

    def test_client_number_accessor(self):

    



