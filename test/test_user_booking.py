import unittest
from User import User
from Student import Student
from Employee import Employee
from Wallet import Wallet
from SmartVehicle import SmartVehicle, VehicleCondition, VehicleType
from ParkingLotManagement import ParkingLotManagement
from UserPaymentManagement import UserPaymentManagement
from Trip import Trip, PricingStrategy
from datetime import datetime, date, time, timedelta

class TestUserBooking(unittest.TestCase):
    def setUp(self):
        self.parking_lot = ParkingLotManagement()
        self.vehicle = SmartVehicle("V001", "REG001", VehicleType.Bike, "Location1", VehicleCondition.ReadyToUse, "QR001")
        self.user_wallet = Wallet()
        self.student_user = Student("student_user", "hashed_password", "ID_CARD", "12345")
        self.employee_user = Employee("employee_user", "hashed_password", "DRIVING_LICENSE", "ABCDE1234")

        # Set up student user with wallet and initial funds
        self.student_user._User__wallet = self.user_wallet
        self.user_wallet.add_funds(20.0)  # Initial funds for the student

        # Set up employee user with wallet and initial funds
        self.employee_user._User__wallet = self.user_wallet
        self.user_wallet.add_funds(25.0)  # Initial funds for the employee

        self.user_payment_manager_student = UserPaymentManagement(self.student_user, False)
        self.user_payment_manager_employee = UserPaymentManagement(self.employee_user, False)

    def test_student_booking_vehicle(self):
        self.parking_lot.add_vehicle(self.vehicle)
        self.assertTrue(self.parking_lot.is_ready_to_ride(self.vehicle))

        # Initial wallet balance
        initial_balance = self.user_wallet.get_current_balance()

        # Student books a ride
        self.user_payment_manager_student.pay_for_trip(10.0, True)

        # Check if ride assigned
        self.assertTrue(self.parking_lot.is_ready_to_ride(self.vehicle))
        self.assertEqual(self.user_wallet.get_current_balance(), initial_balance - 10.0)

    def test_employee_booking_vehicle(self):
        self.parking_lot.add_vehicle(self.vehicle)
        self.assertTrue(self.parking_lot.is_ready_to_ride(self.vehicle))

        # Initial wallet balance
        initial_balance = self.user_wallet.get_current_balance()

        # Employee books a ride
        self.user_payment_manager_employee.pay_for_trip(15.0, True)

        # Check if ride assigned
        self.assertTrue(self.parking_lot.is_ready_to_ride(self.vehicle))
        self.assertEqual(self.user_wallet.get_current_balance(), initial_balance - 15.0)

    def test_trip_functionalities(self):
        pricing_strategy = PricingStrategy(5, 10, 2, 15)
        trip = Trip(self.vehicle, self.student_user, pricing_strategy)

        # Start the trip
        start_time = datetime(2022, 1, 1, 10, 0, 0)
        trip.start_trip(self.vehicle, self.student_user, start_time)

        # Check trip details
        self.assertEqual(trip.get_start_time(), start_time)
        self.assertFalse(trip.is_trip_finished())
        self.assertFalse(trip.is_bill_settled())

        # Renew the trip after 8 hours
        renew_time = start_time + timedelta(hours=9)
        trip.renew(renew_time)


        # Finish the trip with auto deduction
        trip.finish_trip(renew_time, self.user_payment_manager_student)

        # Check updated fine
        self.assertEqual(trip.get_total_fine(), 15.0)

        self.assertTrue(trip.is_trip_finished())


if __name__ == '__main__':
    unittest.main()
