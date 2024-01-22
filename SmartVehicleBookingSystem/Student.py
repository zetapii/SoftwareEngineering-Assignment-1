from User import User


class Student(User):
    '''
    Inherited from User class
    '''

    def __init__(self, username, hashed_password, identification_method,
                 identifying_document):
        '''
        Initializes the Student object
        Amount added to fees is the amount that the student has to pay to the college
        '''
        super().__init__(username, hashed_password, identification_method,
                         identifying_document)
        self.__amount_added_to_fees = 0.0

    def get_overdue(self):
        return self.__amount_added_to_fees

    def pay_overdue(self, amount):
        self.__amount_added_to_fees += amount
