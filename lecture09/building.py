from elevator import Elevator

class Building:
     def __init__(self, bottom, top, num_elevators):
        self.elevators = []

        for i in range(num_elevators):
            new_elevator = Elevator(bottom, top)
            self.elevators.append(new_elevator)

     def run_elevator(self, elevator_number, destination_floor):
        print("\nRunning elevator", elevator_number)
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(destination_floor)

b = Building(0, 10, 2)
b.run_elevator(0, 5)
b.run_elevator(1, 8)
b.run_elevator(0, 0)
