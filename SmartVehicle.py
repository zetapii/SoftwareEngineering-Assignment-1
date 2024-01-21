from Location import Location
from enum import Enum

class VehicleCondition(Enum):
    ReadyToUse = 1
    NeedRepair = 2
    NeedReplacement = 3

class VehicleType(Enum):
    Bike = 1
    Bicycle = 2
    Moped = 3

class SmartVehicle:
    def __init__(self, vehicle_number, registration_number, vehicle_type, docking_location, vehicle_condition, qr_code):
        self.vehicle_number = vehicle_number
        self.registration_number = registration_number
        self.vehicle_type = vehicle_type
        self.docking_location = docking_location
        self.vehicle_condition = vehicle_condition
        self.qr_code = qr_code
        self.distance_travelled_in_km = 0.0

    def get_vehicle_number(self):
        return self.vehicle_number

    def get_registration_number(self):
        return self.registration_number

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_docking_location(self):
        return self.docking_location

    def get_vehicle_condition(self):
        return self.vehicle_condition

    def get_qr_code(self):
        return self.qr_code

    def update_docking_location(self, new_location):
        self.docking_location = new_location

    def update_vehicle_condition(self, updated_condition):
        self.vehicle_condition = updated_condition

    def update_qr_code(self, updated_qr_code):
        self.qr_code = updated_qr_code

    def get_distance_travelled_in_km(self):
        return self.distance_travelled_in_km 
