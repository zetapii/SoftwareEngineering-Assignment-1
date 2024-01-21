from User import User
from IdentificationMethod import IdentificationMethod

class AuthenticationSystem:
    def __init__(self):
        self.user_list = []

    def login_user(self, username, password):
        pass
        #hash the password passed and then compare it        

    def register_user(self, username, password, identification_method, identifying_document):
        pass
        #to do -> actual password is passed here ,  using hashing algorithm create hashed password
        #then create user instance and add it to user_list