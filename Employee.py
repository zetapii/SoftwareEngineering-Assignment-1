from User import User

class Employee(User):
    def __init__(self, username, hashed_password, identification_method, identifying_document):
        super().__init__(username, hashed_password,identification_method,identifying_document)
        self.amount_deducted_from_salary = 0.0
    
    def pay_overdue(self,amount):
        self.amount_deducted_from_salary += amount