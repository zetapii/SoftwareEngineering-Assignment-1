class Wallet:
    '''
    This class is responsible for managing user's wallet.
    Can be used to add funds, deduct funds, get current balance, etc.
    A Transaction History is also maintained here.
    '''

    def __init__(self, min_balance=0):
        self.__current_balance = 0.0
        self.__min_balance = min_balance
        self.__transaction_history = []

    def add_funds(self, amount):
        '''
        Adds funds to the wallet.
        Returns True if the amount was added, else False.
        '''
        if amount > 0:
            self.__current_balance += amount
            self.__transaction_history.append(f"Added {amount} funds.")
            return True
        return False

    def deduct_funds(self, amount):
        '''
        Deducts funds from the wallet.
        Minimum balance has to be maintained.
        Returns True if the amount was deducted, else False.
        '''
        if amount > 0 and amount + self.__min_balance <= self.__current_balance:
            self.__current_balance -= amount
            self.__transaction_history.append(f"Deducted {amount} funds.")
            return True
        return False

    def get_current_balance(self):
        return self.__current_balance

    def get_transaction_history(self):
        return self.__transaction_history

    def can_pay_amount(self, amount):
        '''
        Returns True if the wallet can pay the amount, else False.
        '''
        return amount > 0 and amount + self.__min_balance <= self.__current_balance
