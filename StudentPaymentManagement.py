from enum import Enum
from UserPaymentManagementInterface import UserPaymentManagementInterface, ExternalPaymentOptions

class StudentPaymentManagement(UserPaymentManagementInterface):
    def __init__(self, student, auto_deduct=False):
        self.student = student
        self.auto_deduct = auto_deduct
        self.amount_added_to_fees = 0.0

    def get_student(self):
        return self.student

    def add_to_fees(self, amount):
        self.amount_added_to_fees += amount

    def pay_for_trip(self, trip):
        # Placeholder for implementation
        pass

    def is_auto_deduct(self):
        return self.auto_deduct

    def add_money_externally(self, payment_type, amount_to_add):
        # Placeholder for implementation
        pass
