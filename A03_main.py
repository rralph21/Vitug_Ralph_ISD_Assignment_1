"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client 
from patterns.observer.observer import Observer



# 2. Create a Client object with data of your choice.
client_1 = Client(
    client_number = 1001,
    first_name = "Ralph",
    last_name = "Vitug",
    email_address = "ralph.vitug@email.com"
)


# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_1 = ChequingAccount(
    account_number = 2001,
    client_number = client_1.client_number,
    balance = 500.00,
    date_created = date.today(),
    overdraft_limit = -100.00,
    overdraft_rate = 0.05
)

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
savings_1 = SavingsAccount(
    account_number = 2002,
    client_number = client_1.client_number,
    balance = 150.00,
    date_created = date.today(),
    minimum_balance = 100.00
)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
chequing_1.attach(client_1)
savings_1.attach(client_1)

# 5a. Create a second Client object with data of your choice.
client_2 = Client(
    client_number = 1002,
    first_name = "Not",
    last_name = "Mark",
    email_address = "Not.Mark@email.com"
)

# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
savings_2 = SavingsAccount(
    account_number = 2003,
    client_number = client_2.client_number,
    balance = 80.00,
    date_created = date.today(),
    minimum_balance = 100.00
)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

def safe_deposit(acct, amount):
    """Deposit with error handling and a friendly print."""
    try:
        acct.deposit(amount)
        print(f"Deposited ${amount:,.2f} into Account #{acct.account_number}."
              f" New balance: ${acct.balance:,.2f}")
    except Exception as e:
        print(f"[DEPOSIT ERROR on #{acct.account_number}] {e}")

def safe_withdraw(acct, amount):
    """Withdraw with error handling and a friendly print."""
    try:
        acct.withdraw(amount)
        print(f"Withdrew ${amount:,.2f} from Account #{acct.account_number}. New balance: ${acct.balance:,.2f}")
    except Exception as e:
        print(f"[WITHDRAW ERROR on #{acct.account_number}] {e}")



