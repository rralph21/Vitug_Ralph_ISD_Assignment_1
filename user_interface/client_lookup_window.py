__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
import user_interface.manage_data as manage_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    
    def __init__(self):
        super().__init__()
        
        self.client_listing, self.accounts = load_data()

        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
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

    @Slot()
    def on_text_changed(self, text: str) -> None:
        """
        Slot for on_text_signal

        """

        self.account_table.setRowCount(0)

    @Slot(int, int)
    def on_select_account(self, row: int, column: int) -> None:
        """
        Slot for the account_table cellClicked signal

        ValueError:
                QMessageBox.warning: error message
        """

        item = self.account_table.item(row, 0)

        if item is None:
            QMessageBox.warning(
                self, 
                "Please select a valid record", 
                "Please select a valid record"
                )
            return
        
        account_number_text = item.text().strip()

        if account_number_text == "":
            QMessageBox.warning(
                self, 
                "Please select a valid record",
                "Please select a valid record"
                )
            return
        
        try:
            account_number = int(account_number_text.replace(",", ""))

        except ValueError:
            QMessageBox.warning(
                self, 
                "Please select a valid record", 
                "Please select a valid record"
                )
            return
        
        if account_number not in self.accounts:
            QMessageBox.warning(
                self,
                "Bank Account Error",
                "Bank Account selected does not Exists"
            )
            return
        
        selected_account = self.accounts[account_number]

        details_window = AccountDetailsWindow(selected_account)

        #connects to the dialogs signal to update_data
        details_window.balance_updated.connect(self.update_data)

        details_window.exec_()

    @Slot(BankAccount)
    def update_data(self, account: BankAccount) -> None:
        """
        Slot for the balance_update signal.
        """

        row_count = self.account_table.rowCount()

        for row in range(row_count):
            item = self.account_table.item(row,0)
            if item is None:
                continue

            try:
                table_account_number = int(item.text())

            except ValueError:
                continue

            if table_account_number == account.account_number:
                new_balance_text = f"${account.balance:,.2f}"

                balance_item = self.account_table.item(row, 1)

                if balance_item is None:
                    balance_item = QTableWidgetItem(new_balance_text)
                    self.account_table.setItem(row, 1, balance_item)

                else:
                    balance_item.setText(new_balance_text)

                break

        self.accounts[account.account_number] = account

        manage_data.update_data(account)
