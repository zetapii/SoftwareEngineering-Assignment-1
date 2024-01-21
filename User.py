from Wallet import Wallet
from IdentificationMethod import IdentificationMethod

class User:
    # to do 
    # only password is passed , Hash is calculated later based on hashing method
    def __init__(self, username, hashed_password, identification_method, identifying_document):
        self.username = username
        self.hashed_password = hashed_password
        self.wallet = Wallet()
        self.identification_method = identification_method
        self.identifying_document = identifying_document
        self.past_trips = []

    # Methods for getting information and updating
    # ...
