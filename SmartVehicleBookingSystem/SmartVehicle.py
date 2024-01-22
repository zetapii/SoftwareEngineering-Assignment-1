from Location import Location
from enum import Enum 
from VehicleCondition import VehicleCondition

class VehicleType(Enum):
    Bike = 1
    Bicycle = 2
    Moped = 3

class SmartVehicle:
    def __init__(self, vehicle_number, registration_number, vehicle_type, docking_location, vehicle_condition, qr_code):
        self.__vehicle_number = vehicle_number
        self.__registration_number = registration_number
        self.__vehicle_type = vehicle_type
        self.__docking_location = docking_location
        self.__vehicle_condition = vehicle_condition
        self.__qr_code = qr_code
        self.__distance_travelled_in_km = 0.0

    def get_vehicle_number(self):
        return self.__vehicle_number

    def get_registration_number(self):
        return self.__registration_number

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_docking_location(self):
        return self.__docking_location

    def get_vehicle_condition(self):
        return self.__vehicle_condition

    def get_qr_code(self):
        return self.__qr_code

    def update_docking_location(self, new_location):
        self.__docking_location = new_location

    def update_vehicle_condition(self, updated_condition):
        self.__vehicle_condition = updated_condition

    def update_qr_code(self, updated_qr_code):
        self.__qr_code = updated_qr_code

    def get_distance_travelled_in_km(self):
        return self.__distance_travelled_in_km
