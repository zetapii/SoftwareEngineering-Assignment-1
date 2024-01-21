class PricingStrategy:
    def __init__(self, base_price, per_km_price, fine_per_day):
        self.base_price = base_price
        self.per_km_price = per_km_price
        self.fine_per_day = fine_per_day

    def get_base_price(self):
        return self.base_price

    def get_per_km_price(self):
        return self.per_km_price

    def get_fine_per_day(self):
        return self.fine_per_day

    def set_base_price(self, updated_price):
        self.base_price = updated_price

    def set_per_km_price(self, updated_price):
        self.per_km_price = updated_price

    def set_fine_per_day(self, updated_price):
        self.fine_per_day = updated_price
