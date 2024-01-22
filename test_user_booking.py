import unittest
from User import User
from Student import Student 
from Employee import Employee 
from Wallet import Wallet
from SmartVehicle import SmartVehicle, VehicleCondition, VehicleType
from ParkingLotManagement import ParkingLotManagement
from UserPaymentManagement import UserPaymentManagement

class TestUserBooking(unittest.TestCase):
    def setUp(self):
        self.parking_lot = ParkingLotManagement()
        self.vehicle = SmartVehicle("V001", "REG001", VehicleType.Bike, "Location1", VehicleCondition.ReadyToUse, "QR001")
        self.user_wallet = Wallet()

        self.student_user = Student("student_user", "hashed_password", "ID_CARD", "12345")
        self.student_user._User__wallet = self.user_wallet
        self.user_wallet.add_funds(20.0)  

        self.employee_user = Employee("employee_user", "hashed_password", "DRIVING_LICENSE", "ABCDE1234")
        self.employee_user._User__wallet = self.user_wallet
        self.user_wallet.add_funds(25.0) 

        self.user_payment_manager_student = UserPaymentManagement(self.student_user, False)
        self.user_payment_manager_employee = UserPaymentManagement(self.employee_user, False)

    def test_student_booking_vehicle(self):
        self.parking_lot.add_vehicle(self.vehicle)
        self.assertTrue(self.parking_lot.is_ready_to_ride(self.vehicle))

        initial_balance = self.user_wallet.get_current_balance()

        self.user_payment_manager_student.pay_for_trip(10.0, True)

        self.assertTrue(self.parking_lot.is_ready_to_ride(self.vehicle))
        self.assertEqual(self.user_wallet.get_current_balance(), initial_balance - 10.0)

    def test_employee_booking_vehicle(self):
        self.parking_lot.add_vehicle(self.vehicle)
        self.assertTrue(self.parking_lot.is_ready_to_ride(self.vehicle))

        initial_balance = self.user_wallet.get_current_balance()

        self.user_payment_manager_employee.pay_for_trip(15.0, True)

        self.assertTrue(self.parking_lot.is_ready_to_ride(self.vehicle))
        self.assertEqual(self.user_wallet.get_current_balance(), initial_balance - 15.0)

if __name__ == '__main__':
    unittest.main()
