__author__ = "Ralph Vitug"
__version__ = "ISD 2.1.0"


from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from datetime import datetime
from utility.file_utils import simulate_send_email

class Client: # initialing a class Client
    """
    
    Contains client information

    args:

        client_number (int): An integer value representing the client number
        first_name (str): A string value the client's first name
        last_name (str): A string value the client's last name
        email_address (str): A string value the client's email address

    Raises:
        ValueError 1 is raised if client number is not of an integer data type.
        ValueError 2 is raised if the first name is blank
        ValueError 3 is raised if the last name is blank
        EmailNotValidError is raised if the email address is invalid

    Methods:
        client_number attribute converted into a method.
        first_name attribute converted into a method.
        last_name attribute converted into a method.
        email_address attribute converted into a method.

    __str__:
        Produces a string value that is formatted
            as per assignment requirements.

    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
       

        if isinstance(client_number, int): 
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be a numeric type")
           
        
        if len(first_name.strip())> 0: 
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank")
           
        
        if len(last_name.strip())> 0: 
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank")
            
        try: 
            
            validate_email(email_address, check_deliverability=False)
            self.__email_address = email_address
        
        except EmailNotValidError:

            raise
            
        

    @property 
    def client_number(self) -> int: 
        return self.__client_number
        
    @property 
    def first_name(self) -> str: 
        return self.__first_name
        
    @property 
    def last_name(self) -> str: 
        return self.__last_name
        
    @property 
    def email_address(self) -> str: 
        return self.__email_address
    
    def update(self, message: str) -> None:
        """
        update is called automatically when a Subject (i.e BankAccount)
        notifies this Client.

        Args:
            message (str): The message sent by the Subject.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # timestamp is shared by a classmate Matthew T

        subject = f"ALERT: Unusual Activity: {timestamp}"
        body = (f"Notification for {self.client_number}: {self.first_name}"
            f" {self.last_name}: {message}")

        simulate_send_email(self.email_address, subject, body)
        
    def __str__(self) -> str: 
            
        return (f"{self.__last_name}, {self.__first_name}"
        f"[{self.__client_number}] - {self.__email_address}")
        
