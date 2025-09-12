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

    def test_init_invalid_account_number(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            BankAccount("Wendy", 456, 100.0)

    def test_init_invalid_client_number(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            BankAccount(123, "Ways", 100.0)

    def test_init_non_numeric_balance_defaults_to_zero(self):
        # Arrange & Act
        account = BankAccount(123, 456, "invalid")

        # Assert
        self.assertEqual(0.0, round(account._BankAccount__balance, 2))

    def test_account_number_accessor(self):
        # Arrange is setUp
        # Act & Assert
        self.assertEqual(123, self.account.account_number)

    def test_client_number_accessor(self):
        # Arrange is setUp
        # Act & Assert
        self.assertEqual(456, self.account.client_number)

    def test_balance_accessor(self):
        # Arrange is setUp
        # Act & Assert
        self.assertEqual(100.0, round(self.account.balance, 2))

    def test_update_balance_positive(self):
        # Arrange is setUp
        # Act
        self.account.update_balance(50.0)

        # Assert
        self.assertEqual(150.0, self.account.balance)

    def test_update_balance_negative(self):
        # Arrange is setUp
        # Act
        self.account.update_balance(-40.0)

        # Assert
        self.assertEqual(60.0, self.account.balance)

    def test_update_balance_non_numeric(self):
        # Arrange is setUp
        # Act
        self.account.update_balance("invalid")

        # Assert
        self.assertEqual(100.0, self.account.balance)

    def test_deposit_valid_amount(self):
        # Arrange is setUp
        # Act
        self.account.deposit(25.0)

        # Assert
        self.assertEqual(125.0, self.account.balance)

    def test_deposit_negative_raises(self):
        # Arrange & Act / Assert
        with self.assertRaises(ValueError):
            self.account.deposit(-20)

    def test_withdraw_valid(self):
        # Arrange is setUp
        # Act
        self.account.withdraw(50.0)

        # Assert
        expected = 50.0
        actual = self.account.balance
        self.assertEqual(expected, round(actual, 2))

    def test_withdraw_negative_raises(self):
        # Arrange & Act / Assert
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_withdraw_exceeds_balance_raises(self):
        # Arrange & Act / Assert
        with self.assertRaises(ValueError):
            self.account.withdraw(200.0)

    def test_str(self):
        # Arrange is setUp
        expected = "Account Number: 123 Balance: $100.00\n"

        # Assert
        self.assertEqual(expected, str(self.account))


if __name__ == "__main__":
    unittest.main()