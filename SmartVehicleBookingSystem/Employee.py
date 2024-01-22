from User import User

class Employee(User):
    def __init__(self, username, hashed_password, identification_method, identifying_document):
        '''
        Inherited from User class
        '''
        super().__init__(username, hashed_password,identification_method,identifying_document)
        self.__amount_deducted_from_salary = 0.0

    def get_overdue(self):
        return self.__amount_deducted_from_salary

    def pay_overdue(self,amount):
        self.__amount_deducted_from_salary += amount