from User import User
from IdentificationMethod import IdentificationMethod
from enum import Enum
from hashlib import md5, sha512


class HashingAlgorithm(Enum):
    MD5 = 1
    SH5 = 2


class AuthenticationSystem:
    '''
    This class is responsible for managing the authentication of users.
    '''

    def __init__(self, hashing_algorithm):
        self.__user_list = []
        self.__hashing_algorithm = hashing_algorithm

    def get_hash(self, data):
        '''
        This method returns the hash of the data using the hashing algorithm specified in the constructor.
        '''
        match self.__hashing_algorithm:
            case HashingAlgorithm.MD5:
                hashed_data = md5(data.encode()).hexdigest()
                return hashed_data
            case HashingAlgorithm.SH5:
                hashed_data = sha512(data.encode()).hexdigest()
                return hashed_data
            case _:
                raise ValueError(
                    f"Unsupported hashing algorithm: {self.__hashing_algorithm}"
                )

    def get_hashing_algorithm(self):
        return self.__hashing_algorithm
    
    def login_user(self, username, password):
        '''
        This method returns the user object if the username and password matches, else it returns None.
        '''
        for user in self.__user_list:
            if user.get_username() == username:
                if user.get_hashed_password() == self.get_hash(password):
                    return user
        return None

    def register_user(self, username, password, identification_method,
                      identifying_document):
        '''
        This method registers a new user and returns the user object if the username is not already taken, else it returns None.
        '''
        for user in self.__user_list:
            if user.get_username() == username:
                return None
        user = User(username, self.get_hash(password), identification_method,
                    identifying_document)
        self.__user_list.append(user)
        return user

