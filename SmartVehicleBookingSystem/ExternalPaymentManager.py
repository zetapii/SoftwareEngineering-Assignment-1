from UserPaymentManagement import ExternalPaymentOptions
from Wallet import Wallet
from enum import Enum
class ExternalPaymentOptions(Enum):
    UPI = "UPI"
    NetBanking = "NetBanking"
    CreditCard = "CreditCard"

class ExternalPaymentManager:
    def __init__():
        pass
    def add_money_externally(type,username,password,amount_to_add,wallet):
        #possible external authentication and external api calls
        ##############################################
        wallet.add_funds(amount_to_add)