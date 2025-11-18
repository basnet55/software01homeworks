from building import Building
b = Building(0, 10, 2)

def fire_alarm(building):
    print("\nFire alarm! Moving all elevators to the bottom floor!")
    for i, elevator in enumerate(building.elevators):
        print("\nElevator", i)
        elevator.go_to_floor(elevator.bottom)

b.run_elevator(0, 5)
b.run_elevator(1, 8)

fire_alarm(b)
