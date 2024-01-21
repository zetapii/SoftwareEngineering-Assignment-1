from enum import Enum

class ExternalPaymentOptions(Enum):
    UPI = "UPI"
    NetBanking = "NetBanking"
    CreditCard = "CreditCard"

class UserPaymentManagementInterface:
    def is_auto_deduct(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def pay_for_trip(self, trip):
        raise NotImplementedError("Subclasses must implement this method.")

    def add_money_externally(self, payment_type, amount_to_add):
        raise NotImplementedError("Subclasses must implement this method.")
