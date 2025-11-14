__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy
from PySide6.QtCore import Slot

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        if isinstance(account, BankAccount):

            self.account = copy.copy(account)

            self.account_number_label.setText(str(self.account.account_number))

            self.balance_label.setText(f"${self.account.balance:,.2f}")

            #Connect buttons to their slots
            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)

    @Slot()
    def on_apply_transaction(self):
        """
        Transaction handler
        """
        pass

    @Slot()
    def on_exit(self):
        """
        Exit handler
        """
        pass
    