# Base class
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def set_speed(self, speed):
        if 0 <= speed <= self.max_speed:
            self.current_speed = speed
        else:
            print("Speed out of range!")

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# Subclass for electric cars
class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


# Subclass for gasoline cars
class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


# Main program
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

# Set speeds
electric_car.set_speed(150)
gasoline_car.set_speed(120)

# Drive for 3 hours
electric_car.drive(3)
gasoline_car.drive(3)

# Print distances
print(f"{electric_car.registration_number} has travelled {electric_car.travelled_distance} km.")
print(f"{gasoline_car.registration_number} has travelled {gasoline_car.travelled_distance} km.")
