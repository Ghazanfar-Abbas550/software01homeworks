class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, new_speed):
        self.current_speed += new_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        distance_travelled = self.current_speed*hours
        self.travelled_distance += distance_travelled


car1 = Car("ABC-123",142, travelled_distance=2000)
update_car1 = car1
update_car1.accelerate(60)
car1.drive(1.5)
print(f"Car1\nRegistration number: {car1.registration_number} \nMaximum speed in km/h: {car1.maximum_speed} \nCurrent speed: {car1.current_speed}\nTravelled distance: {car1.travelled_distance}")