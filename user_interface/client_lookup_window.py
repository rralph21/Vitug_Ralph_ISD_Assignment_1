__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount
from .manage_data import load_data

class ClientLookupWindow(LookupWindow):
    
    def __init__(self):
        super().__init__()
        
    self.client_listing, self.accounts = load_data()

    self.lookup_button.clicked.connect(self.on_lookup_client)
    self.client_number_edit.textChange.connect(self.on_text_changed)
    self.account_table.cellClicked.connect(self.on_select_account)

    @Slot()
    def on_lookup_client(self) -> None:
        """
        slot for lookup_button signal

        ValueError:
            QMessageBox.Warning: error message
        """

        client_text = self.client_number_edit.text().strip()

        try:
            client_number = int(client_text)

        except ValueError:
            QMessageBox.warning(
                self,
                "Non-Numeric Client",
                "Client Number must be a numeric value."
            )

            #reset
            self.reset_display()
            return
        
        #reset before showing new results
        self.reset_display()

        if client_number not in self.client_listing:
            QMessageBox.information(
                self,
                "Client Not Found",
                f"Client Number {client_number} not found"
            )

            #reset
            self.reset_display()
            return
        
        #get Client object if calient is valid
        client = self.client_listing[client_number]

        #display client information
        self.client_info_label.setText(str(client))

        #display all client's account
        self.account_table.setRowCount(0)

        for account in self.accounts.values():
            if account.client_number == client.client_number:

                row = self.account_table.rowCount()
                self.account_table.insertRow(row)

                account_number_item = QTableWidgetItem(str(account.account_number))

                balance_text = f"${account.balance:,.2f}"
                balance_item = QTableWidgetItem(balance_text)

                data_text = str(account.date_created.date())
                date_item = QTableWidgetItem(data_text)

                account_type_text = account.__class__.__name__
                account_type_item = QTableWidgetItem(account_type_text)

                self.account_table.setItem(row, 0, account_number_item)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, date_item)
                self.account_table.setItem(row, 3, account_type_item)

        self.account_table.resizeColumnsToContents()
