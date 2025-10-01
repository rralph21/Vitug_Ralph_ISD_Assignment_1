"""
Description: Unit tests for the ChequingAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests.test_chequing_account.py
"""

__author__ = "Ralph Vitug"
__version__ = "ISD 1.0.0"

import unittest
from datetime import date
from bank_account import *


class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        # Arrange for most tests
        self.account = ChequingAccount(2121,2222,1000.00,date.today(),-100.00,0.05)

    def test_init_valid(self):
        # Act & Assert
        self.assertEqual(1000.00, self.account.balance)
        self.assertEqual(-100.00, self.account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.05, self.account._ChequingAccount__overdraft_rate)

    def test_init_invalid_overdraft_limit(self):
        # Arrange & Act
        account = ChequingAccount(2121, 2222, 1000.00, date.today(), "not_Mark", 0.05)

        # Assert
        self.assertEqual(-100.00, account._ChequingAccount__overdraft_limit)

    def test_init_invalid_overdraft_rate(self):
        # Arrange & Act
        account = ChequingAccount(2121, 2222, 1000.00, date.today(), -100.00, "not_Mark")

        # Assert
        self.assertEqual(0.05, account._ChequingAccount__overdraft_rate)

    def test_init_invalid_date_created(self):
        # Arrange & Act
        invalid_account = ChequingAccount(2121,2222,1000.0,"not_Mark", -100.00, 0.05)

        # Assert
        self.assertEqual(invalid_account._date_created, date.today())

    def test_service_charges_balance_greater_than_limit(self):
        # Arrange
        account = ChequingAccount(2121, 2222, 50.00, date.today(), -100.00, 0.05)
        expected = BankAccount.BASE_SERVICE_CHARGE

        # Act & Assert
        self.assertEqual(expected, round(account.get_service_charges(), 2))

    def test_service_charges_balance_less_than_limit(self):
        # Arrange
        account = ChequingAccount(2121, 2222, -600.00, date.today(), -100.00, 0.05)
        expected = BankAccount.BASE_SERVICE_CHARGE + (-100.00 - (-600.00)) * 0.05

        # Act & Assert
        self.assertEqual(expected, round(account.get_service_charges(), 2))

    def test_service_charges_balance_equal_to_limit(self):
        # Arrange
        account = ChequingAccount(2121, 2222, -100.00, date.today(), -100.00, 0.05)
        expected = BankAccount.BASE_SERVICE_CHARGE

        # Act & Assert
        self.assertEqual(expected, round(account.get_service_charges(), 2))

    def test_str(self):
        # Arrange 
        expected = (
            "Account Number: 2121 Balance: $1,000.00\n"
            + "Overdraft limit: $-100.00 "
            + "Overdraft rate: %5.00 "
            + "Account type: Chequing"
        )

        # Act & Assert
        self.assertEqual(expected, str(self.account))


if __name__ == "__main__":
    unittest.main()
