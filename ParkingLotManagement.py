from SmartVehicle import *
from LoggingService import LoggingService

class ParkingLotManagement:
    def __init__(self):
        self.vehicle_list = []
        self.vehicles_assigned_to_ride = []
        self.parking_lot_log = LoggingService()

    def add_vehicle(self, vehicle_to_add):
        if vehicle_to_add not in self.vehicle_list:
            self.vehicle_list.append(vehicle_to_add)
            self.parking_lot_log.log_event(f"Vehicle {vehicle_to_add.get_vehicle_number()} added to the parking lot.")

    def remove_vehicle(self, vehicle_to_remove):
        if vehicle_to_remove in self.vehicle_list:
            self.vehicle_list.remove(vehicle_to_remove)
            self.parking_lot_log.log_event(f"Vehicle {vehicle_to_remove.get_vehicle_number()} removed from the parking lot.")

    def assign_ride(self, vehicle_to_assign):
        if vehicle_to_assign in self.vehicle_list and vehicle_to_assign not in self.vehicles_assigned_to_ride and vehicle_to_assign.get_vehicle_condition() == VehicleCondition.ReadyToUse:
            self.vehicles_assigned_to_ride.append(vehicle_to_assign)
            self.parking_lot_log.log_event(f"Vehicle {vehicle_to_assign.get_vehicle_number()} assigned for a ride.")
        else:
            self.parking_lot_log.log_event(f"Cannot assign ride for Vehicle {vehicle_to_assign.get_vehicle_number()}.")

    def collect_completed_ride_vehicle(self, vehicle):
        if vehicle in self.vehicles_assigned_to_ride:
            self.vehicles_assigned_to_ride.remove(vehicle)
            self.parking_lot_log.log_event(f"Collected completed ride vehicle {vehicle.get_vehicle_number()}.")
        else:
            self.parking_lot_log.log_event(f"Vehicle {vehicle.get_vehicle_number()} not found in assigned rides.")

    def is_ready_to_ride(self, vehicle):
        return vehicle in self.vehicle_list and vehicle not in self.vehicles_assigned_to_ride and vehicle.get_vehicle_condition() == VehicleCondition.ReadyToUse

    def get_all_vehicle_for_repair(self):
        return [vehicle for vehicle in self.vehicle_list if vehicle.get_vehicle_condition() == VehicleCondition.NeedRepair]

    def get_vehicle_information(self, qr_code):
        for vehicle in self.vehicle_list:
            if vehicle.get_qr_code() == qr_code:
                return vehicle
        return None
