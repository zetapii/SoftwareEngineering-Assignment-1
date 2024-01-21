from User import User
from IdentificationMethod import IdentificationMethod
from enum import Enum 
from hashlib import md5, sha512
import bcrypt

class HashingAlgorithm(Enum):
    MD5 = 1
    SH5 = 2
    Bcrypt = 3

class AuthenticationSystem:
    #add private variables
    def __init__(self, hashing_algorithm):
        self.user_list = []
        self.hashing_algorithm = hashing_algorithm

    def get_hash(self, data):
        match self.hashing_algorithm:
            case 'MD5':
                hashed_data = md5(data.encode()).hexdigest()
                return hashed_data
            case 'SHA5':
                hashed_data = sha512(data.encode()).hexdigest()
                return hashed_data
            case 'Bcrypt':
                salt = bcrypt.gensalt()
                hashed_data = bcrypt.hashpw(data.encode(), salt).decode()
                return hashed_data
            case _:
                raise ValueError(f"Unsupported hashing algorithm: {self.hashing_algorithm}")

    def login_user(self, username, password):
        for user in self.user_list:
            if user.get_username()==username :
                if user.get_hashed_password()==self.get_hash(password):
                    return user
        return None

    def register_user(self, username, password, identification_method, identifying_document):
        for user in self.user_list:
            if user.get_username()==username : 
                return None 
        user = User(username,self.get_hash(username,password),identification_method,identifying_document)
        self.user_list.append(user)