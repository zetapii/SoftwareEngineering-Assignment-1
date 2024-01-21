from Wallet import Wallet
from IdentificationMethod import IdentificationMethod
from abc import ABC, abstractmethod 

class User:
    def __init__(self, username, hashed_password, identification_method, identifying_document):
        self.username = username
        self.hashed_password = hashed_password
        self.wallet = Wallet()
        self.identification_method = identification_method
        self.identifying_document = identifying_document
        self.past_trips = []

    def get_username(self):
        return self.username
    
    def get_hashed_password(self):
        return self.hashed_password
    
    def update_past_trips(self,trip):
        self.past_trips.append(trip)

    def get_past_trips(self):
        return self.past_trips
    
    @abstractmethod
    def pay_overdue(self):
        pass
