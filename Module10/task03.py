class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print("We are at floor", self.current_floor)

    def floor_down(self):
        self.current_floor-=1
        print("We are at floor", self.current_floor)

    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if target_floor > self.current_floor:
                self.floor_up()
            elif target_floor < self.current_floor:
                self.floor_down()
        print("We are at floor", self.current_floor)
        print("We reached the floor")


class Building:
    def __init__(self, bottom_floor, top_floor, amount_elevator):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.amount_elevator = amount_elevator
        self.elevators = []

        for i in range(amount_elevator):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, target_floor):
        if 1 <= elevator_number <= len(self.elevators):
            print(f"Running elevator {elevator_number} to floor {target_floor}")
            self.elevators[elevator_number - 1].go_to_floor(target_floor)
        else:
            print("Invalid elevator number.")

    def fire_alarm(self):
        print("Fire alarm triggered! Moving all elevators to the bottom floor.")
        for i, elevator in enumerate(self.elevators, start = 1):
            print(f"Moving elevator {i} to bottom floor...")
            elevator.go_to_floor(self.bottom_floor)
        print("All elevators are now at the bottom floor.")


# Example main program
building = Building(1, 10, 3)
building.run_elevator(1, 7)
building.run_elevator(2, 5)
building.fire_alarm()