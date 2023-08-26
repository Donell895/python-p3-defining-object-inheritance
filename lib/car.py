from vehicle import Vehicle
from car import Car

class TestVehicleAndCar:
    def test_vehicle_attributes(self):
        vehicle = Vehicle(wheel_size=18, wheel_number=4)
        assert vehicle.wheel_size == 18
        assert vehicle.wheel_number == 4

    def test_vehicle_go_method(self):
        vehicle = Vehicle(wheel_size=18, wheel_number=4)
        assert vehicle.go() == "vrrrrrrrooom!"

    # ...similar tests for Car class...
