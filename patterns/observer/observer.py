__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Observer class acts like an interface that 
    defines a rule.

    ABC: Any class inherits from Observer must
    create its own version of the update method.

    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        message (str): The notification message sent by the Subject.
        """

        pass