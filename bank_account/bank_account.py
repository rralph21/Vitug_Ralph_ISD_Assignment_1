__author__ = "Ralph Vitug"
__version__ = "ISD 3.1.1"

from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC): 

    BASE_SERVICE_CHARGE: float = 0.50

    """
    
    Bank Account information

    args:

        account_number (int): An integer value representing the account number
        client_number (int): An integer value representing the client number
        balance (float): A floating number representing the balance of the account

    Raises:
        ValueError 1 is raised if the account number is not an integer data type.
        ValueError 2 is raised if the client number is not an integer data type.

    __str__:
        Produces a string value that is formatted as per
            assignment requirements.
    """

    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date):
        
        if isinstance(account_number, int):
            self.__account_number = account_number

        else:
            raise ValueError("The account number must be a numerical form")
        

        if isinstance(client_number, int):
            self.__client_number = client_number

        else:
            raise ValueError("The client number must be a numerical form")
        
        if isinstance(balance, float):
            self.__balance = balance
        
        else:
            try:
                self.__balance = float(balance)

            except (ValueError):
                self.__balance = 0
        
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    
    @property
    def account_number(self) -> int:
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        return self.__client_number
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    def update_balance(self, amount) -> None:

        """
        Updates the amount of the balance.
        If amount is not valid, it will not update.

        args:
            amount (None): A float value representing 
            the value of the balance.

        Raises:
            ValueError is raised but passed if the amount is invalid
        """

        try:
            self.__balance += float(amount)

        except (ValueError):
            pass

    def deposit(self, amount: float) -> None:

        """
        Deposits a positive amount into the account.
        Raises ValueError if amount is not numeric.
        Validates deposit amount if its positive.

        args:
            amount (None): A float value representing the 
            deposit amount.

        Raises:
            ValueError raised if deposit amount is non numeric.
            ValueError raised if deposit amount is of negative value.
        """

        try:
            amount = float(amount)
        except (ValueError):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        if amount <= 0:
            validated = f"${amount:,.2f}"
            raise ValueError(f"Deposit amount: {validated} must be positive.")

        self.update_balance(amount)


    def withdraw(self, amount: float) -> None:
        """
        Withdraws a positive amount if sufficient balance exists.
        Raises ValueError if amount is invalid, not positive, or exceeds balance.

        args:
            amount (float): A float value representing 
            the withdrawal amount.

        Raises:
            ValueError 1 raised if amount is none numeric.
            ValueError 2 raised if amount is of negative value.
            ValueError 3 raised if withdrawal amount exceeds the balance.
        """
        
        try:
            amount = float(amount)
        except (ValueError):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")

       
        if amount <= 0:
            validated = f"${amount:,.2f}"
            raise ValueError(f"Withdraw amount: {validated} must be positive.")

        
        if amount > self.__balance:
            validated_amt = f"${amount:,.2f}"
            validated_bal = f"${self.__balance:,.2f}"
            raise ValueError(
                f"Withdraw amount: {validated_amt} must not exceed the account balance: {validated_bal}."
            )

        self.update_balance(-amount)

    @abstractmethod
    def get_service_charges(self) -> float:
       
       pass

    def __str__(self) -> str:
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}\n"
        

    
