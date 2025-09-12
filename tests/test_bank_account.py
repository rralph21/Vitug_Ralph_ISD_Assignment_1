"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # runs before each test to reduce redundancy
        self.account = BankAccount(123, 456, 100.0)

    def test_init_valid(self):
        # Arrange & Act
        account = BankAccount(123, 456, 100.0)

        # Assert (private attributes via name mangling)
        self.assertEqual(123, account._BankAccount__account_number)
        self.assertEqual(456, account._BankAccount__client_number)
        self.assertEqual(100.0, round(account._BankAccount__balance, 2))