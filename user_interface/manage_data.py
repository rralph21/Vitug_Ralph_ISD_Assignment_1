__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# For testing code - python -m user_interface.manage_data

import os
import sys
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime
import logging
from PySide6.QtWidgets import QApplication
import sys
from client.client import Client
from bank_account import *


# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************






def load_data()->tuple[dict[int, Client],dict[int, BankAccount]]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    Returns:
        tuple containing client dictionary and account dictionary.
        dict: key = client_number(int)
              value = Client object
        dict: key = account_number (int)
              value = ChequingAccount, SavingsAccount,
                      InvestmentAccount objects

    exception:
        client_listing: dict[int, Client]
            logging: if client data is invalid, it will log the error
        accounts: dict[int, BankAccounts]
            raises: ValueError if the account type is invalid
            logging: if account_number doesnt match client_number,
                    it will log the error.
    """
    client_listing: dict[int, Client]= {} # key = client_number. value = first_name, last_name and email

    accounts: dict[int, BankAccount] = {} # key = account_number. value = chequing, investment and savings acct.

    # READ CLIENT DATA 
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try: 
                # converting client_numbe to int
                client_number = int(row["client_number"])

                first_name = row["first_name"]
                last_name = row["last_name"]
                email_address = row["email_address"]

                client = Client(
                    client_number = client_number,
                    first_name = first_name,
                    last_name = last_name,
                    email_address = email_address
                )

                client_listing[client_number] = client
            
            except Exception as e:
                # Logging
                logging.error(
                    f"Unable to create client record: {e}"
                )

    # READ ACCOUNT DATA
    with open(accounts_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                #converting numeric values
                account_number = int(row["account_number"])
                client_number = int(row["client_number"])
                balance = float(row["balance"])

                #converting date to datetime object
                date_created = datetime.strptime(row["date_created"], "%Y-%m-%d")

                account_type = row["account_type"]
                
                if row["overdraft_limit"] == "Null":
                    overdraft_limit = None

                else:
                    overdraft_limit = float(row["overdraft_limit"])

                if row["overdraft_rate"] == "Null":
                    overdraft_rate = None

                else:
                    overdraft_rate = float(row["overdraft_rate"])

                if row["minimum_balance"] == "Null":
                    minimum_balance = None

                else:
                    minimum_balance = float(row["minimum_balance"])

                if row["management_fee"] == "Null":
                    management_fee = None
                
                else:
                    management_fee = float(row["management_fee"])

                # BankAccount subclass object
                if account_type == "ChequingAccount":
                    new_account = ChequingAccount(
                        account_number = account_number,
                        client_number = client_number,
                        balance = balance,
                        date_created = date_created,
                        overdraft_limit = overdraft_limit,
                        overdraft_rate = overdraft_limit
                    )

                elif account_type == "InvestmentAccount":
                    new_account = InvestmentAccount(
                        account_number = account_number,
                        client_number = client_number,
                        balance = balance,
                        date_created = date_created,
                        management_fee = management_fee 
                    )

                elif account_type == "SavingsAccount":
                    new_account = SavingsAccount(
                        account_number = account_number,
                        client_number = client_number,
                        balance = balance,
                        date_created = date_created,
                        minimum_balance = minimum_balance,
                    )
                
                else:
                    raise ValueError("Not a valid account type.")
                
                if client_number in client_listing:

                    accounts[account_number] = new_account

                #Exception handler and logging for invalid client
                else:
                    logging.error(
                        f"Bank Account: {account_number} contains invalid"
                        + f" Client Number: {client_number}"
                    )
            #Exception handler and logging for all other errors
            except Exception as e:

                logging.error(
                    f"Unable to create bank account: {e}"
                )
    # RETURN STATEMENT

    return client_listing, accounts
    


def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")