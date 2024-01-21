from enum import Enum
from UserPaymentManagementInterface import UserPaymentManagementInterface, ExternalPaymentOptions

class EmployeePaymentManagement(UserPaymentManagementInterface):
    def __init__(self, employee, auto_deduct=False):
        self.employee = employee
        self.auto_deduct = auto_deduct
        self.amount_deducted_from_salary = 0.0

    def get_employee(self):
        return self.employee

    def deduct_from_salary(self, amount):
        self.amount_deducted_from_salary += amount

    def pay_for_trip(self, amount):
        # logic here
        pass

    def is_auto_deduct(self):
        return self.auto_deduct

    def add_money_externally(self, payment_type, amount_to_add):
        pass
        #just add the external payment management thing