class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

car1 = Car("ABC-123",142)
print(f"Car1 \nRegistration number: {car1.registration_number} \nMaximum speed in km/h: {car1.maximum_speed} \nCurrent speed: {car1.current_speed} \nTravelled distance: {car1.travelled_distance}")