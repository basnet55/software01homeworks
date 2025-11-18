class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        self.current_floor += 1
        print("Elevator is now on floor", self.current_floor)

    def floor_down(self):
        self.current_floor -= 1
        print("Elevator is now on floor", self.current_floor)

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()

e = Elevator(0, 10)

e.go_to_floor(5)
e.go_to_floor(0)
