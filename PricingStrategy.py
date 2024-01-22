class PricingStrategy:
    def __init__(self, base_distance , base_price, per_km_price, fine_per_day):
        self.__base_distance = base_distance
        self.__base_price = base_price
        self.__per_km_price = per_km_price
        self.__fine_per_day = fine_per_day

    def get_base_distance(self):
        return self.__base_distance
    
    def get_base_price(self):
        return self.__base_price

    def get_per_km_price(self):
        return self.__per_km_price

    def get_fine_per_day(self):
        return self.__fine_per_day

    def set_base_distance(self, updated_distance):
        self.__base_distance = updated_distance 
        
    def set_base_price(self, updated_price):
        self.__base_price = updated_price

    def set_per_km_price(self, updated_price):
        self.__per_km_price = updated_price

    def set_fine_per_day(self, updated_price):
        self.__fine_per_day = updated_price
