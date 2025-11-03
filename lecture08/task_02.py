class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0 , travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_of_speed):
        self.current_speed  += change_of_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
            print("⚠ Speed limited to maximum speed!")

        elif self.current_speed < 0:
            self.current_speed = 0
            print(" The car has stopped (speed can't go below 0).")

car1= Car("ABC-123",142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print(f"\n Speed after accelerations: {car1.current_speed} km/h")

car1.accelerate(-200)
print(f"Final speed after emergency brake: {car1.current_speed} km/h")

