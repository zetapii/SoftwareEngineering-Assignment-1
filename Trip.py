from datetime import datetime
from SmartVehicle import SmartVehicle
from User import User
from PricingStrategy import PricingStrategy
import math 

class Trip:
    def __init__(self, vehicle, user, pricing_strategy):    
        self.vehicle_used = vehicle
        self.user_riding = user
        self.start_time = datetime.now()
        self.last_renew_time = datetime.now()
        self.bill_settled = False
        self.trip_finished = False
        self.distance_travelled_in_km = 0.0
        self.pricing_strategy = pricing_strategy
        self.total_fine = 0.0

    def start_trip(self, vehicle, user, starting_time):
        self.start_time = starting_time
        self.vehicle_used = vehicle 
        self.user_riding = user
        self.last_renew_time = starting_time

    def get_vehicle_used(self):
        return self.vehicle_used

    def get_user_riding(self):
        return self.user_riding
    
    def is_bill_settled(self):
        return self.bill_settled 
    
    def get_total_fine(self):
        return self.total_fine

    def calculate_total_bill(self):
        self.distance_travelled_in_km = self.vehicle_used.get_distance_travelled_in_km()
        if self.distance_travelled_in_km <= self.pricing_strategy.get_base_distance():
            return self.distance_travelled_in_km * self.pricing_strategy.get_base_price()+self.total_fine
        return self.pricing_strategy.get_base_distance()*self.pricing_strategy.get_base_price() + \
            (self.distance_travelled_in_km-self.pricing_strategy.get_base_distance())*self.pricing_strategy.get_per_km_price()

    def update_fine(self, current_time):
        time_difference  = current_time - self.last_renew_time
        hours_difference = time_difference.total_seconds() / 3600
        if hours_difference > 8:
            self.total_fine = self.total_fine + math.ceil(hours_difference/24)*self.pricing_strategy.get_fine_per_day()  
    
    def renew(self, current_time):
        self.update_fine(self, current_time)
        self.last_renew_time = current_time

    def finish_trip(self, current_time, user_payment_management):
        self.update_fine(self,current_time)
        self.trip_finished = True
        if user_payment_management.is_auto_deduct():
            user_payment_management.pay_for_trip(self.calculate_total_bill())
                        
    def update_bill_status(self,status):
        self.bill_settled = status 

