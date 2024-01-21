from datetime import datetime
from SmartVehicle import SmartVehicle
from User import User
from PricingStrategy import PricingStrategy

class Trip:
    def __init__(self, vehicle, user, pricing_strategy):
        self.vehicle_used = vehicle
        self.user_riding = user
        self.last_renew_time = datetime.now()
        self.is_bill_settled = False
        self.is_trip_finished = False
        self.distance_travelled_in_km = 0.0
        self.pricing_strategy = pricing_strategy
        self.total_fine = 0.0

    def start_trip(self, vehicle, user, starting_time):
        pass

    def update_distance_travelled_in_km(self, updated_distance):
        self.distance_travelled_in_km += updated_distance

    def calculate_total_bill(self):
        pass

    def renew(self, current_time):
        pass

    def finish_trip(self):
        pass
