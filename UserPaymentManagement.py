from enum import Enum
from User import User
from Wallet import Wallet

class ExternalPaymentOptions(Enum):
    UPI = "UPI"
    NetBanking = "NetBanking"
    CreditCard = "CreditCard"

class UserPaymentManagement:

    def __init__(self,user,auto_deduct):
        self.user = user 
        self.auto_deduct = auto_deduct

    def is_auto_deduct(self):
        return self.auto_deduct
    
    def pay_for_trip(self, amount, pay_from_wallet):
        if pay_from_wallet:
            if self.user.wallet.can_pay_amount(amount):
                return self.user.wallet.deduct_funds(self.user.wallet.deduct_funds(amount))
            return False            
        else : 
            self.user.pay_overdue(amount)
            return True
        
    def add_money_externally(self, payment_type, amount_to_add):
        pass
