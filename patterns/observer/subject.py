__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from typing import List
from observer import Observer

class Subject:
    """
    Subject class manages a list of observers 
    and sends them updates.
    """

    def __init__(self):
        """
        List: Private list of Observers
        """
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        observer (Observer): Observer that 
        wants to receive updates.
        """
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        observer (Observer): Observer that 
        does not wants updates.
        """
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        message (str): Notification message 
        to send to observers.
        """
        for observer in self._observers:
            observer.update(message)