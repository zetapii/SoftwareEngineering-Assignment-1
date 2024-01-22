import unittest
from ParkingLotManagement import ParkingLotManagement
from SmartVehicle import SmartVehicle, VehicleCondition, VehicleType

class TestParkingLotManagement(unittest.TestCase):
    def setUp(self):
        # Create an instance of ParkingLotManagement and two SmartVehicle instances for testing
        self.parking_lot = ParkingLotManagement()
        self.vehicle1 = SmartVehicle("V001", "REG001", VehicleType.Bike, "Location1", VehicleCondition.ReadyToUse, "QR001")
        self.vehicle2 = SmartVehicle("V002", "REG002", VehicleType.Bicycle, "Location2", VehicleCondition.NeedRepair, "QR002")

    def test_add_vehicle(self):
        # Test the addition of a vehicle to the parking lot
        self.parking_lot.add_vehicle(self.vehicle1)
        self.assertIn(self.vehicle1, self.parking_lot._ParkingLotManagement__vehicle_list)

    def test_remove_vehicle(self):
        # Test the removal of a vehicle from the parking lot
        self.parking_lot.add_vehicle(self.vehicle1)
        self.parking_lot.remove_vehicle(self.vehicle1)
        self.assertNotIn(self.vehicle1, self.parking_lot._ParkingLotManagement__vehicle_list)

    def test_assign_ride(self):
        # Test assigning a ride to a vehicle
        self.parking_lot.add_vehicle(self.vehicle1)
        self.parking_lot.assign_ride(self.vehicle1)
        self.assertIn(self.vehicle1, self.parking_lot._ParkingLotManagement__vehicles_assigned_to_ride)

    def test_collect_completed_ride_vehicle(self):
        # Test collecting a completed ride vehicle
        self.parking_lot.add_vehicle(self.vehicle1)
        self.parking_lot.assign_ride(self.vehicle1)
        self.parking_lot.collect_completed_ride_vehicle(self.vehicle1)
        self.assertNotIn(self.vehicle1, self.parking_lot._ParkingLotManagement__vehicles_assigned_to_ride)

    def test_is_ready_to_ride(self):
        # Test checking if a vehicle is ready to ride
        self.parking_lot.add_vehicle(self.vehicle1)
        self.assertTrue(self.parking_lot.is_ready_to_ride(self.vehicle1))

    def test_get_all_vehicle_for_repair(self):
        # Test getting all vehicles that need repair
        self.parking_lot.add_vehicle(self.vehicle1)
        self.parking_lot.add_vehicle(self.vehicle2)
        repair_vehicles = self.parking_lot.get_all_vehicle_for_repair()
        self.assertIn(self.vehicle2, repair_vehicles)
        self.assertNotIn(self.vehicle1, repair_vehicles)

    def test_get_vehicle_information(self):
        # Test getting information about a specific vehicle using its QR code
        self.parking_lot.add_vehicle(self.vehicle1)
        vehicle_info = self.parking_lot.get_vehicle_information("QR001")
        self.assertEqual(vehicle_info, self.vehicle1)

if __name__ == '__main__':
    unittest.main()
