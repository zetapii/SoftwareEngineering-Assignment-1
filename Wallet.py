class Wallet:
    def __init__(self, min_balance):
        self.current_balance = 0.0
        self.min_balance = min_balance
        self.transaction_history = []

    def add_funds(self, amount):
        if amount > 0:
            self.current_balance += amount
            self.transaction_history.append(f"Added {amount} funds.")
            return True
        return False

    def deduct_funds(self, amount):
        if amount > 0 and amount + self.min_balance <= self.current_balance:
            self.current_balance -= amount
            self.transaction_history.append(f"Deducted {amount} funds.")
            return True
        return False

    def get_current_balance(self):
        return self.current_balance

    def get_transaction_history(self):
        return self.transaction_history
