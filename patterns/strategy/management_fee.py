__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from typing import List
from patterns.strategy.service_charge import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(BankAccount):
    """
     Initializes ManagementFeeStrategy upon received argument
    (if valid).

    ars:
        TEN_YEARS_AGO (date): Constant of date type will be calculated
        to the current date minus ten years using the following
        formula.
        management_fee (float): The management_fee is a float which
        stores a flat-rate fee the bank charges for managing an 
        InvestmentAccount.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):

        try:
            self.__management_fee = float(management_fee)

        except ValueError:
            self.__management_fee = 2.55

    def calculate_service_charge(self, account: BankAccount) -> float:
         """
        Calculate service charges

        returns:
            InvestmentAccount (float): > 10 y.o + BSC,
            < 10 y.o + (BSC + MF).
        """

        if self._date_created <= ManagementFeeStrategy.TEN_YEARS_AGO:
            return BankAccount.BASE_SERVICE_CHARGE
    
        else:
            return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee 