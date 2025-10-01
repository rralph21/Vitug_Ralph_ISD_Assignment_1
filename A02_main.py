"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date, timedelta

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(account_number=2121, client_number=2222,
                                   balance=-200.00, date_created=date.today(),
                                   overdraft_limit=-100.00, overdraft_rate=0.05)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Chequing account: {chequing_account}")
print("Service charges:", round(chequing_account.get_service_charges(), 2))

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
chequing_account.deposit(210.00)
print(f"Chequing account: {chequing_account}")
print("Service charges:", round(chequing_account.get_service_charges(), 2))

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(account_number=2121, client_number=2222,
                                   balance=2100.00, date_created=date.today(),
                                   minimum_balance=50.00)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Savings account: {savings_account}")
print("Service charges:", round(savings_account.get_service_charges(), 2))

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
savings_account.withdraw(2060.00)
print(f"Savings account: {savings_account}")
print("Service charges:", round(savings_account.get_service_charges(), 2))

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_account = InvestmentAccount(2122,2222,2000.00,
                            date.today() - timedelta(days=5 * 365),2.00 )

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(f"Investment account (new): {investment_account}")
print("Service Charges:", round(investment_account.get_service_charges(), 2))

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_account_old = InvestmentAccount(2122,2222,2000.00,
                            date.today() - timedelta(days=11 * 365),2.00 )

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(f"Investment account (old): {investment_account_old}")
print("Service Charges:", round(investment_account_old.get_service_charges(), 2))
print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
accounts = [chequing_account, savings_account, investment_account, investment_account_old]

for account in accounts:
    charge = account.get_service_charges()
    account.withdraw(charge)
    
# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print("Service Charges for All Accounts:\n")
for account in accounts:

    print(account)
    print(f"Service Charges Withdrawn: {round(charge, 2)}\n")
