__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account import BankAccount
from typing import List

class ServiceChargeStrategy(ABC):
    """
    ServiceChargeStrategy charges a fee to appropriate back account
    const: BASE_SERVICE_SERVICE: float = 0.50
    """

    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount): float
    """
    calculate_service_charge method will be implemented in each
    of the sublcasses of ServiceChargeStrategy baed on the specific
    strategy being employed.
    """
    pass
