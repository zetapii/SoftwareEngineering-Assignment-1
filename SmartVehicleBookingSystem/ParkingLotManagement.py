from SmartVehicle import *
from LoggingService import LoggingService


class ParkingLotManagement:
    '''
    This manages the parking lot, its vehicles and their status.
    '''

    def __init__(self):
        self.__vehicle_list = []
        self.__vehicles_assigned_to_ride = []
        self.__parking_lot_log = LoggingService()

    def add_vehicle(self, vehicle_to_add):
        '''
        Adds a vehicle to the parking lot checking if it is already present.
        '''
        if vehicle_to_add not in self.__vehicle_list:
            self.__vehicle_list.append(vehicle_to_add)
            self.__parking_lot_log.log_event(
                f"Vehicle {vehicle_to_add.get_vehicle_number()} added to the parking lot."
            )

    def remove_vehicle(self, vehicle_to_remove):
        '''
        Removes a vehicle from the parking lot checking if it is present.
        '''
        if vehicle_to_remove in self.__vehicle_list:
            self.__vehicle_list.remove(vehicle_to_remove)
            self.__parking_lot_log.log_event(
                f"Vehicle {vehicle_to_remove.get_vehicle_number()} removed from the parking lot."
            )

    def assign_ride(self, vehicle_to_assign):
        '''
        Assigns a vehicle for a ride checking if it is present and not already assigned.
        '''
        if vehicle_to_assign in self.__vehicle_list and vehicle_to_assign not in self.__vehicles_assigned_to_ride and vehicle_to_assign.get_vehicle_condition(
        ) == VehicleCondition.ReadyToUse:
            self.__vehicles_assigned_to_ride.append(vehicle_to_assign)
            self.__parking_lot_log.log_event(
                f"Vehicle {vehicle_to_assign.get_vehicle_number()} assigned for a ride."
            )
        else:
            self.__parking_lot_log.log_event(
                f"Cannot assign ride for Vehicle {vehicle_to_assign.get_vehicle_number()}."
            )

    def collect_completed_ride_vehicle(self, vehicle):
        '''
        Collects a vehicle after a ride is completed checking if it is present and assigned.
        '''
        if vehicle in self.__vehicles_assigned_to_ride:
            self.__vehicles_assigned_to_ride.remove(vehicle)
            self.__parking_lot_log.log_event(
                f"Collected completed ride vehicle {vehicle.get_vehicle_number()}."
            )
        else:
            self.__parking_lot_log.log_event(
                f"Vehicle {vehicle.get_vehicle_number()} not found in assigned rides."
            )

    def is_ready_to_ride(self, vehicle):
        '''
        Returns True if the vehicle is ready to ride, else False.
        '''
        return vehicle in self.__vehicle_list and vehicle not in self.__vehicles_assigned_to_ride and vehicle.get_vehicle_condition(
        ) == VehicleCondition.ReadyToUse

    def get_all_vehicle_for_repair(self):
        '''
        Gets all the vehicles that need repair by checking their condition.
        '''
        return [
            vehicle for vehicle in self.__vehicle_list
            if vehicle.get_vehicle_condition() == VehicleCondition.NeedRepair
        ]

    def get_vehicle_instance(self, qr_code):
        '''
        Gets the vehicle instance by checking the QR code.
        '''
        for vehicle in self.__vehicle_list:
            if vehicle.get_qr_code() == qr_code:
                return vehicle
        return None
