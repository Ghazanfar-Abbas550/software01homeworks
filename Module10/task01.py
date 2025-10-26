class Elevator:
    def __init__(self, bottom_floor, top_floor, ):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def floor_up(self):
        new_floor = self.current_floor+1
        self.current_floor = new_floor
        print('We are at floor', self.current_floor)
        return self.current_floor

    def floor_down(self):
        new_floor = self.current_floor - 1
        self.current_floor = new_floor
        print('We are at floor', self.current_floor)
        return self.current_floor

    def go_to_floor(self,target_floor):
        while self.current_floor != target_floor:
            if target_floor > self.current_floor:
                self.floor_up()

            elif target_floor < self.current_floor:
                self.floor_down()
        print('We are at floor',self.current_floor)
        print("We reached the floor")

h = Elevator(0,20)
h.go_to_floor(5)