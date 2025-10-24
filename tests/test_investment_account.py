"""
Description: Unit tests for the InvestmentAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests.test_investment_account
"""

__author__ = "Ralph Vitug"
__version__ = "ISD 1.0.0"

import unittest
from datetime import date, timedelta
from bank_account import *


class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        # Arrange for most tests
        self.account = InvestmentAccount(2121, 2222, 1000.00, date.today(), 2.00)

    def test_init_valid(self):
        # Act & Assert
        self.assertEqual(1000.00, self.account.balance)
        self.assertEqual(2.00, self.account._InvestmentAccount__management_fee)
        self.assertEqual(date.today(), self.account._date_created)

    def test_init_invalid_management_fee(self):
        # Arrange & Act
        account = InvestmentAccount(
            2121, 2222, 1000.00, date.today(), "not_Mark"
        )
        # Assert
        self.assertEqual(2.55, account._InvestmentAccount__management_fee)

    def test_service_charges_date_more_than_10_years(self):
        # Arrange
        old_date = date.today() - timedelta(days=int(11 * 365.25))
        account = InvestmentAccount(
            2121, 2222, 1000.00, old_date, 2.00
        )
        expected = BankAccount.BASE_SERVICE_CHARGE

        # Act & Assert
        self.assertEqual(expected, round(account.get_service_charges(), 2))

    def test_service_charges_date_exactly_10_years(self):
        # Arrange
        exact_date = date.today() - timedelta(days=int(10 * 365.25))
        account = InvestmentAccount(
            2121, 2222, 1000.00, exact_date, 2.00
        )
        expected = BankAccount.BASE_SERVICE_CHARGE

        # Act & Assert
        self.assertEqual(expected, round(account.get_service_charges(), 2))

    def test_service_charges_date_within_10_years(self):
        # Arrange
        recent_date = date.today() - timedelta(days=int(5 * 365.25))
        account = InvestmentAccount(
            2121, 2222, 1000.00, recent_date, 2.00
        )
        expected = BankAccount.BASE_SERVICE_CHARGE + 2.00

        # Act & Assert
        self.assertEqual(expected, round(account.get_service_charges(), 2))

    def test_str_fee_waived_for_old_account(self):
        # Arrange
        old_date = date.today() - timedelta(days=int(11 * 365.25))
        account = InvestmentAccount(
            2121, 2222, 1000.00, old_date, 2.00
        )
        expected = (
            f"Account Number: 2121 Balance: $1,000.00\n"
            f"Date Created: {old_date} "
            f"Management Fee: Waived "
            f"Account Type: Investment"
        )

        # Act & Assert
        self.assertEqual(expected, str(account))

    def test_str_with_fee_for_recent_account(self):
        # Arrange
        recent_date = date.today() - timedelta(days=int(5 * 365.25))
        account = InvestmentAccount(
            2121, 2222, 1000.00, recent_date, 2.00
        )
        expected = (
            f"Account Number: 2121 Balance: $1,000.00\n"
            f"Date Created: {recent_date} "
            f"Management Fee: $2.00 "
            f"Account Type: Investment"
        )

        # Act & Assert
        self.assertEqual(expected, str(account))


if __name__ == "__main__":
    unittest.main()