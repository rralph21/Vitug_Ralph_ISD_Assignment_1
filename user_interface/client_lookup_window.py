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

    @Slot
    def on_lookup_client(self) -> None:
        """
        slot for lookup_button signal

        raises: ValueError
            QMessageBox.Warning: error message
        """

        client_text = self.client_number_edit.text().strip()

        try:
            client_number = int(client_text)

        except ValueError:
            QMessageBox.warning(
                self,
                "Non-Numberic Client",
                "Client Number must be a numeric value."
            )

            #reset
            self.reset_display()
            return
        
        #reset before showing new results
        self.reset_display()

        if client_number not in self.client_listing:
