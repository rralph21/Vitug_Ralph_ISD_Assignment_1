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
        minimum_balance (float): converts to float, but
        defaults to 50.00 if value is invalid.
    """
    SERVICE_CHARGE_PREMIUM = 2.00

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date,
                 minimum_balance: float):
        super().__init__(account_number, client_number, 
                        balance,date_created)
        
        try:
            self.__minimum_balance = float(minimum_balance)

        except ValueError:
            self.__minimum_balance = 50.00

    def get_service_charges(self) -> float:
        """
        Calculates service charges

        Returns:
            balance >= minimum_balance + BSC.
            balance < minimum_balance + (BSC * SCP)
        """

        if self.balance >= self.__minimum_balance:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM

    def __str__(self) -> str:
        """
        String method of SavingsAccount

        returns: 
            str: details as required
        """

        return (
            f"Account Number: {self.account_number} Balance: ${self.balance:,.2f}\n"
            f"Minimum Balance: ${self.__minimum_balance:,.2f} "
            f"Account Type: Savings"
        )


