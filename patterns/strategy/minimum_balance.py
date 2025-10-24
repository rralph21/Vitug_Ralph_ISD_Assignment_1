__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from typing import List
from patterns.strategy.service_charge import ServiceChargeStrategy
from bank_account import *

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    MinimumBalanceStrategy charges a fee to accounts that exceeds
    below minimum balance.

    raises/exception:
        minimum_balance (float): converts to float, but
        defaults to 50.00 if value is invalid.
    """

    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, minimum_balance: float):

        try:
            self.__minimum_balance = float(minimum_balance)

        except ValueError:
            self.__minimum_balance = 50.00

    def calculate_service_charges(self, account: BankAccount, balance: float) -> float:
        """
        Calculates service charges

        Returns:
            balance >= minimum_balance + BSC.
            balance < minimum_balance + (BSC * SCP)
        
        """

        if account.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM