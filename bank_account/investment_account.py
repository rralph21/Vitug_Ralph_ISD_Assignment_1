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
        management_fee (float): converts to float but, defaults
        to 2.55 if value is invalid.
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

    def get_service_charges(self) -> float:
        """
        Calculate service charges

        returns:
            InvestmentAccount (float): > 10 y.o + BSC,
            < 10 y.o + (BSC + MF).
        """

        if self._date_created <= InvestmentAccount.TEN_YEARS_AGO:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee



    def __str__(self) -> str:
        """
        String method of InvestmentAccount

        fee: InvestmentAccount < 10 y.o
            returns: "Waived"

        returns:
            str: details as required.
        """

        if self._date_created <= InvestmentAccount.TEN_YEARS_AGO:
            fee = "Waived"

        else:
            fee = f"${self.__management_fee:,.2f}"

        return (
            super().__str__()
            + f"Date Created: {self._date_created}"
            + f" Management Fee: {fee}"
            + " Account type: Investment"
            )
