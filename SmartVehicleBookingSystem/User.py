from Wallet import Wallet
from IdentificationMethod import IdentificationMethod
from abc import abstractmethod


class User:
    '''
    It is an abstract class which is inherited by Student and Employee classes.
    '''

    def __init__(self, username, hashed_password, identification_method,
                 identifying_document):
        '''
        We are using hashed_password instead of password to ensure security.
        A Wallet is added to the user object, which is used to manage money.
        '''
        self.__username = username
        self.__hashed_password = hashed_password
        self.__wallet = Wallet()
        self.__identification_method = identification_method
        self.__identifying_document = identifying_document
        self.__past_trips = []

    def get_username(self):
        return self.__username

    def get_hashed_password(self):
        return self.__hashed_password

    def get_wallet(self):
        return self.__wallet

    def get_identification_method(self):
        return self.__identification_method

    def get_identifying_document(self):
        return self.__identifying_document

    def update_past_trips(self, trip):
        self.__past_trips.append(trip)

    def get_past_trips(self):
        return self.__past_trips

    # The following methods are abstract methods, which are implemented in the Student and Employee classes.

    @abstractmethod
    def pay_overdue(self):
        pass

    @abstractmethod
    def get_overdue(self):
        pass
