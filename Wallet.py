class Wallet:
    def __init__(self, min_balance = 0):
        self.__current_balance = 0.0
        self.__min_balance = min_balance
        self.__transaction_history = []
        
    def add_funds(self, amount):
        if amount > 0:
            self.__current_balance += amount
            self.__transaction_history.append(f"Added {amount} funds.")
            return True
        return False

    def deduct_funds(self, amount):
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
        return amount > 0 and amount + self.__min_balance <= self.__current_balance
