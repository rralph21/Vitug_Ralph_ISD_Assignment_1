"""
Description: Unit tests for the SavingsAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests.test_savings_account
"""

__author__ = "Ralph Vitug"
__version__ = "ISD 1.0.0"

import unittest
from datetime import date, timedelta
from bank_account import *

class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        # Arrange for most tests
        self.account = SavingsAccount(2121, 2222, 1000.00, date.today(), 50.00)

    def test_init_valid(self):
        # Act & Assert
        self.assertEqual(1000.00, self.account.balance)
        self.assertEqual(50.00, self.account._SavingsAccount__minimum_balance)
        self.assertEqual(date.today(), self.account._date_created)

    def test_init_invalid_minimum_balance(self):
        # Arrange & Act
        account = SavingsAccount(
            2121, 2222, 1000.00, date.today(), "not_Mark"
        )
        # Assert
        self.assertEqual(50.00, account._SavingsAccount__minimum_balance)

    def test_service_charges_balance_greater_than_minimum(self):
        # Arrange
        account = SavingsAccount(
            2121, 2222, 500.00, date.today(), 50.00
        )
        expected = BankAccount.BASE_SERVICE_CHARGE

        # Act & Assert
        self.assertEqual(expected, round(account.get_service_charges(), 2))

    def test_service_charges_balance_equal_to_minimum(self):
        # Arrange
        account = SavingsAccount(
            2121, 2222, 50.00, date.today(), 50.00
        )
        expected = BankAccount.BASE_SERVICE_CHARGE

        # Act & Assert
        self.assertEqual(expected, round(account.get_service_charges(), 2))

    def test_service_charges_balance_less_than_minimum(self):
        # Arrange
        account = SavingsAccount(
            2121, 2222, 49.99, date.today(), 50.00
        )
        expected = BankAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM

        # Act & Assert
        self.assertEqual(expected, round(account.get_service_charges(), 2))

    def test_str(self):
        # Arrange
        expected = (
            "Account number: 2121 Balance: $1,000.00\n"
            "Minimum balance: $50.00 Account type: Savings"
        )

        # Act & Assert
        self.assertEqual(expected, str(self.account))


if __name__ == "__main__":
    unittest.main()