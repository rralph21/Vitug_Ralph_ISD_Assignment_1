__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from bank_account import BankAccount
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    """
    Initializes InvestmentAccount upon received argument
    (if valid).

    ars:
        TEN_YEARS_AGO (date): Constant of date type will be calculated
        to the current date minus ten years using the following
        formula.
        management_fee (float): The management_fee is a float which
        stores a flat-rate fee the bank charges for managing an 
        InvestmentAccount.

    raises/exception:
        

    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date, 
                 management_fee: float):
        super().__init__(account_number, client_number, balance,
                         date_created)
        
        try:
            self.__management_fee = float(management_fee)

        except ValueError:
            self.__management_fee = 2.55

    def management_fee(self, management_fee) -> float:

        if self.date_created >= 10:
            
            return BankAccount.BASE_SERVICE_CHARGE
        
        else:  
            return BankAccount.BASE_SERVICE_CHARGE + management_fee



    def __str__(self) -> str:

        return (
            super().__str__()
            + f"Date Created: {date}"
            + f"Management Fee: ${self.__management_fee}"
            + "Account Type: Investment"
        )


    