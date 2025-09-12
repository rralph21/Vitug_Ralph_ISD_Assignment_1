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
from email_validator import EmailNotValidError

class TestClient(unittest.TestCase): # initializing class of test client

    def setUp(self):
        # runs before test to reduce code redundancy
        self.client = Client(12345, "Wendy", "Ways", "WendyWays@pixell-river.com")

    def test_init_valid(self):
        # Arrange & Act
        client = Client(12345, "Wendy", "Ways", "WendyWays@pixell-river.com")

        # Assert
        self.assertEqual(12345, client._Client__client_number) # testing client number if valid
        self.assertEqual("Wendy", client._Client__first_name) # testing first name if valid
        self.assertEqual("Ways", client._Client__last_name) # testing lst name if valid
        self.assertEqual("WendyWays@pixell-river.com", client._Client__email_address) # testing email address if valid

    def test_init_client_number_raises_exception(self): # test to check client number
        # Arrange & Act
        with self.assertRaises(ValueError):
            client = Client("hello world", "Wendy", "Ways", "WendyWays@pixell-river.com")

    def test_init_first_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError): # test to check first name
            client = Client(12345, " ", "Ways", "WendyWays@pixell-river.com")

    def test_init_last_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError): # test to check last name
            client = Client(12345, "Wendy", " ", "WendyWays@pixell-river.com")

    # def test_invalid_email_sets_default(self):
    #     # Arrange & Act
    #     # client = Client(12345, "Wendy", "Ways", "not-an-email")  # purposely invalid

    #     with self.assertRaises(EmailNotValidError):
    #         Client(12345, "Wendy", "Ways", "not-an-email")

        # Assert
        # default attribute when invalid email is inputed
        # self.assertEqual("email@pixell-river.com", client._Client__email_address) 

    def test_invalid_email_address(self):
        # Test invalid email address
        with self.assertRaises(EmailNotValidError):
            client = Client(12345, "Wendy", "Ways", "invalid email")
        

    def test_client_number_accessor(self):
        # Arrange is setUp
        # Act and Assert
        self.assertEqual(12345, self.client.client_number)

    def test_first_name_accessor(self):
        # Arrange is setUp
        # Act and Assert
        self.assertEqual("Wendy", self.client.first_name)

    def test_last_name_accessor(self):
        # Arrange is setUp
        # Act and Assert
        self.assertEqual("Ways", self.client.last_name)

    def test_email_address_accessor(self):
        # Arrange is setUp
        # Act and Assert
        self.assertEqual("WendyWays@pixell-river.com", self.client.email_address)

    def test_str(self):
        # Arrange is setUp

        expected = (f"Ways, Wendy [{12345}] - WendyWays@pixell-river.com")
        # Assert
        self.assertEqual(expected, str(self.client))


    



