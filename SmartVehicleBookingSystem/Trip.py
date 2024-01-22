from datetime import datetime
from SmartVehicle import SmartVehicle
from User import User
from PricingStrategy import PricingStrategy
import math


class Trip:
    '''
    This class is responsible for managing a trip.
    '''

    def __init__(self, vehicle, user, pricing_strategy):
        '''
        Initializes the trip with the vehicle, user and pricing strategy, etc.
        '''
        self.__vehicle_used = vehicle
        self.__user_riding = user
        self.__start_time = datetime.now()
        self.__last_renew_time = datetime.now()
        self.__bill_settled = False
        self.__trip_finished = False
        self.__distance_travelled_in_km = 0.0
        self.__pricing_strategy = pricing_strategy
        self.__total_fine = 0.0

    def start_trip(self, vehicle, user, starting_time):
        '''
        Sets the starting time, vehicle and user for the trip.
        '''
        self.__start_time = starting_time
        self.__vehicle_used = vehicle
        self.__user_riding = user
        self.__last_renew_time = starting_time

    def get_vehicle_used(self):
        return self.__vehicle_used

    def get_user_riding(self):
        return self.__user_riding

    def is_bill_settled(self):
        return self.__bill_settled

    def get_total_fine(self):
        return self.__total_fine

    def get_start_time(self):
        return self.__start_time

    def is_trip_finished(self):
        return self.__trip_finished

    def calculate_total_bill(self):
        '''
        Calculates the total bill for the trip.
        Formula:
        Case 1 (distance_travelled_in_km <= base_distance):
            total_bill = distance_travelled_in_km * base_price + total_fine
        Case 2 (distance_travelled_in_km > base_distance):
            total_bill = base_distance * base_price + (distance_travelled_in_km - base_distance) * per_km_price + total_fine
        '''
        self.__distance_travelled_in_km = self.__vehicle_used.get_distance_travelled_in_km(
        )
        if self.__distance_travelled_in_km <= self.__pricing_strategy.get_base_distance(
        ):
            return self.__distance_travelled_in_km * self.__pricing_strategy.get_base_price(
            ) + self.__total_fine
        return self.__pricing_strategy.get_base_distance() * self.__pricing_strategy.get_base_price() + \
            (self.__distance_travelled_in_km - self.__pricing_strategy.get_base_distance()) * self.__pricing_strategy.get_per_km_price()

    def update_fine(self, current_time):
        '''
        Updates the fine for the trip after renewal or finishing the trip.
        '''
        time_difference = current_time - self.__last_renew_time
        hours_difference = time_difference.total_seconds() / 3600
        if hours_difference > 8:
            self.__total_fine = self.__total_fine + math.ceil(
                hours_difference /
                24) * self.__pricing_strategy.get_fine_per_day()

    def renew(self, current_time):
        self.update_fine(current_time)
        self.__last_renew_time = current_time

    def finish_trip(self, current_time, user_payment_management):
        '''
        This method is called when the user finishes the trip.
        '''
        self.update_fine(current_time)
        self.__trip_finished = True
        if user_payment_management.is_auto_deduct():
            total_bill = self.calculate_total_bill()
            user_payment_management.pay_for_trip(total_bill)

    def update_bill_status(self, status):
        self.__bill_settled = status
