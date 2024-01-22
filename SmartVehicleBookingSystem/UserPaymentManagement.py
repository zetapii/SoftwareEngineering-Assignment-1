from User import User
from Wallet import Wallet


class UserPaymentManagement:
    '''
    This class is responsible for user payment management.
    '''

    def __init__(self, user, auto_deduct):
        self.__user = user
        self.__auto_deduct = auto_deduct

    def get_user(self):
        return self.__user

    def is_auto_deduct(self):
        return self.__auto_deduct

    def update_user(self, user):
        self.__user = user

    def pay_for_trip(self, amount, pay_from_wallet):
        '''
        This method is called when the user pays for the trip.
        If pay_from_wallet is True, then the amount is deducted from the wallet.
        Else, the amount is added to the overdue amount (either salary or fees, depending on the type of user).
        '''
        if pay_from_wallet:
            wallet = self.__user.get_wallet()
            if wallet.can_pay_amount(amount):
                return wallet.deduct_funds(amount)
            return False
        else:
            self.__user.pay_overdue(amount)
            return True
