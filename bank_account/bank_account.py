__author__ = "Ralph Vitug"
__version__ = "ISD 3.0.2"


class BankAccount: # initialing a class Client
    """
    
    Bank Account information

    args:

        account_number (int): An integer value representing the account number
        client_number (int): An integer value representing the client number
        balance (float): A floating number representing the balance of the account


    """

    def __init__(self, account_number: int, client_number: int, balance: float):
        
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
        """

        try:
            amount = float(amount)
        except (ValueError):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        if amount <= 0:
            validated = f"${amount:,.2f}"
            raise ValueError(f"Deposit amount: {validated} must be positive.")

        self.update_balance(amount)

    
