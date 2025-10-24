__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from typing import List
from patterns.strategy.service_charge import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    OverdraftStrategy charges accounts that exceeds the maximum
    threshold of balance insuffeciency.

    
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        
        self.__overdraft_limit = float(overdraft_limit)
    
        self.__overdraft_rate = float(overdraft_rate)
        
    def calculate_service_charges(self, account: BankAccount) -> float:

        """
        Method to calculate service charges.

        args:
            get_service_charges (float): charges that returns float

        """

        if account < self.__overdraft_limit:
        
            overdraft_cost = abs(account - self.__overdraft_limit) * self.__overdraft_rate
            return BankAccount.BASE_SERVICE_CHARGE + overdraft_cost
        else:
            
            return BankAccount.BASE_SERVICE_CHARGE