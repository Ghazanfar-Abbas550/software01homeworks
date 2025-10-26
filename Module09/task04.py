import random

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


cars = []
for i in range(1,11):
    a = "ABC-"+str(i)
    b = random.randint(100, 200)
    cars.append(Car(a, b))

for car in cars:
    print(car.registration_number)
    print(car.maximum_speed)
    print(car.current_speed)
    print(car.travelled_distance)
    print("\n")