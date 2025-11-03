class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):

        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
            print("⚠️ Speed limited to maximum speed!")
        elif self.current_speed < 0:
            self.current_speed = 0
            print("🚨 The car has stopped (speed can't go below 0).")

    def drive(self, hours):

        self.travelled_distance += self.current_speed * hours
        print(f" The car drove for {hours} hours at {self.current_speed} km/h.")
        print(f" Total distance travelled: {self.travelled_distance} km")

car1 = Car("ABC-123", 142)

car1.accelerate(60)
car1.travelled_distance = 2000

car1.drive(1.5)

