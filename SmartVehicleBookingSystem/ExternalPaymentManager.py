from UserPaymentManagement import ExternalPaymentOptions
from Wallet import Wallet
from enum import Enum


class ExternalPaymentOptions(Enum):
    UPI = "UPI"
    NetBanking = "NetBanking"
    CreditCard = "CreditCard"


class ExternalPaymentManager:
    '''
    This class is responsible for external payment management.
    We can specify external payment options here.
    Possible external authentication and external api calls can be made here.
    '''

    def __init__():
        pass

    def add_money_externally(payment_type, username, password, amount_to_add,
                             wallet):
        # TODO: Add external payment logic here
        wallet.add_funds(amount_to_add)
