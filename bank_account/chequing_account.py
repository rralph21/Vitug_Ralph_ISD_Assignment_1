__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft import OverdraftStrategy

class ChequingAccount(BankAccount):

    """
    Initializes ChequingAccount Object upon received argument
        (if valid).
    
    args:
        overdraft_limit (float): The maximum amount a balance
        can be overdrawn (below 0.00) before overdraft fees
        are applied.
        overdraft_rate (float): The rate to which overdraft
        fees will be applied.

    raises:
        overdraft_limit (float): converts to float but defaults
        to -100.0 if value is invalid.
        overdraft_rate (float): converts to float but defaults 
        to 0.05 if value is invalid.
    """
    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date, overdraft_limit: float,
                 overdraft_rate: float):
        
        super().__init__(account_number, client_number, 
                         balance, date_created)

        try:
            self.__overdraft_limit = float(overdraft_limit)
        
        except ValueError:
            self.__overdraft_limit = -100.0

        try:
            self.__overdraft_rate = float(overdraft_rate)

        except ValueError:
            self.__overdraft_rate = 0.05
        
        # OverDraftStrategy
        self.__service_charge_strategy = OverdraftStrategy(
            self.__overdraft_limit, self.__overdraft_rate
        )

    def get_service_charges(self) -> float:
        """
        get_service_charges (float): calulation from OverDraftStrategy
        """

        return self.__service_charge_strategy.calculate_service_charges(self)
        
    def __str__(self) -> str:
        """
        String method of ChequingAccount

        returns:
            str: details as required.

        """

        return (
                super().__str__()
                + f"Overdraft limit: ${self.__overdraft_limit:,.2f} "
                + f"Overdraft rate: %{self.__overdraft_rate * 100:,.2f} "
                + "Account type: Chequing"
            )
    

