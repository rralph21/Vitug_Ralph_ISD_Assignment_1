__author__ = "Ralph Vitug"
__version__ = "ISD 2.0.0"


from email_validator import validate_email, EmailNotValidError

class Client: # initialing a class Client
    """
    
    Contains client information

    args:

        client_number (int): An integer value representing the client number
        first_name (str): A string value the client's first name
        last_name (str): A string value the client's last name
        email_address (str): A string value the client's email address


    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        # using init to declare class attribute based on the class diagram provided

        if isinstance(client_number, int): # checks if client number is valid
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer/numeric type")
            # raises value error if client is not valid
        
        if len(first_name.strip())> 0: # strips any white space from first name
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank")
            # raises value error if first name is blank
        
        if len(last_name.strip())> 0: # strips any white space from last name
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank")
            # raises value error if last name is blank

        try: # email validation block is invoke in a try and except block
            
            validate_email(email_address, check_deliverability=False)
             # email validation
             # check_deliverability set to false to avoid delay
            self.__email_address = email_address
        
        except EmailNotValidError:

            raise
            # self.__email_address = "email@pixell-river.com"
            # setting email attribute as required
            
        

    @property # defining an accessor
    def client_number(self) -> int: # made public
        return self.__client_number
        
    @property # defining an accessor
    def first_name(self) -> str: # made public
        return self.__first_name
        
    @property # defining an accessor
    def last_name(self) -> str: # made public
        return self.__last_name
        
    @property # defining an accessor
    def email_address(self) -> str: # made public
        return self.__email_address
        
    def __str__(self) -> str: # prints in string form of the last name,
                                # last name, client number and email address
            
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}"
        
