__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Recieves update messages from subject
        """

        pass