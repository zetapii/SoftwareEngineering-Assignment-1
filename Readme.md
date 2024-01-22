# Smart Vehicle Booking System

> By Team 19

## Project Structure

	SmartVehicleBookingSystem
	├── AuthenticationSystem.py
	├── CustomerSupport.py
	├── Employee.py
	├── ExternalPaymentManager.py
	├── IdentificationMethod.py
	├── __init__.py
	├── Location.py
	├── LoggingService.py
	├── ParkingLotManagement.py
	├── PricingStrategy.py
	├── SmartVehicle.py
	├── Student.py
	├── test
	│   ├── __init__.py
	│   ├── test_authentication_system.py
	│   ├── test_parking_lot_management.py
	│   └── test_user_booking.py
	├── Trip.py
	├── UserPaymentManagement.py
	├── User.py
	├── VehicleCondition.py
	└── Wallet.py

## How to test

To run the unit tests for the Smart Vehicle Booking System, follow these steps:

1. Navigate to the SmartVehicleBookingSystem directory.
2. Run the following command:

```bash
python3 -m unittest
```

## Assumptions

1. **Naming Convention:** The project follows the underscore (_) naming convention for variable and method names,
as opposed to the camel case convention depicted in the UML diagram. Camel case convention is used in class names as depicted
in the UML diagram. This decision was made for consistency within the python codebase.
