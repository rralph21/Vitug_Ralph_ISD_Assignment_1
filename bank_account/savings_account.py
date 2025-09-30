__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):

    """
    Initializes SavingsAccount upon received argument
    (if valid).

    args:
        SERVICE_CHARGE_PREMIUM (float: 2.00): 
        The SERVICE_CHARGE_PREMIUM constant is set to a 
        flat rate of 2.00. That is, a SavingsAccounts will
        incur 2 times the BASE_SERVICE_CHARGE when the
        balance drops below the minimum_balance.

        minimum_balance: The minimum value a balance can 
        be before further service charges are applied.

    raises/exception:


    """
    SERVICE_CHARGE_PREMIUM = 2.00

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date,
                 minimum_balance: float):
        super().__init__(account_number, client_number, balance,
                         date_created, minimum_balance)
        
        try:
            self.__minimum_balance = float(minimum_balance)

        except ValueError:
            self.__minimum_balance = 50

